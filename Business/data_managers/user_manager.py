from DataAccess.database_managers.user_dal import UserDal
from DataAccess.database_managers.tracking_category_dal import TrackingCategoryDal
from DataAccess.database_managers.tracking_sort_dal import TrackingSortDal
from Entities.user import User
from Core.utilities.results.success_result import SuccessResult
from Core.utilities.results.error_result import ErrorResult
from Business.constants.constant import Constant
from Business.constants.message import Message

from Core.utilities.decorators.decorator import Decorator
from Business.helpers.decorator_helper import DecoratorHelper

class UserManager:
    user_dal = UserDal(Constant.DB_FILE)
    tracking_category_dal = TrackingCategoryDal(Constant.DB_FILE)
    tracking_sort_dal = TrackingSortDal(Constant.DB_FILE)

    @classmethod
    def add(cls, user:User):
        registry = cls.user_dal.get(user.username)
        if(not registry):
            cls.user_dal.add(user)
            cls.tracking_category_dal.add_user(user.username)
            cls.tracking_sort_dal.add_user(user.username)
            return SuccessResult(Message.REGISTRATION_SUCCESSFULLY).toMap()
        else:
            return ErrorResult(Message.REGISTRATION_ALREADY_EXISTS).toMap()
            
    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def delete(cls,user:User):
        cls.user_dal.delete(user)
        cls.tracking_category_dal.delete_user(user.username)
        cls.tracking_sort_dal.delete_user(user.username)
        return SuccessResult(Message.REGISTRATION_DELETION_SUCCESSFULLY).toMap()
        
    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def check_password(cls,user:User):
        user_info = cls.user_dal.get(user.username)[0]
        if(user_info.password == user.password):
            return SuccessResult().toMap()
        else:
            return ErrorResult(Message.PASSWORD_ERROR).toMap()
