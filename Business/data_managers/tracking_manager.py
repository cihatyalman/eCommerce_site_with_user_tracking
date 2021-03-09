from DataAccess.database_managers.category_dal import CategoryDal
from DataAccess.database_managers.sort_dal import SortDal

from DataAccess.database_managers.tracking_category_dal import TrackingCategoryDal
from DataAccess.database_managers.tracking_sort_dal import TrackingSortDal

from Business.constants.constant import Constant
from Business.constants.message import Message
from Core.utilities.results.success_result import SuccessResult
from Core.utilities.results.success_data_result import SuccessDataResult
from Core.utilities.results.error_result import ErrorResult
from Entities.category import Category
from Entities.sort import Sort

from Core.utilities.decorators.decorator import Decorator
from Business.helpers.decorator_helper import DecoratorHelper

class TrackingManager:
    category_dal = CategoryDal(Constant.DB_FILE)
    sort_dal = SortDal(Constant.DB_FILE)
    tracking_category_dal = TrackingCategoryDal(Constant.DB_FILE)
    tracking_sort_dal = TrackingSortDal(Constant.DB_FILE)


    @classmethod
    def db_configure(cls):
        "Run Once !"
        CategoryDal(Constant.DB_FILE).configure()
        SortDal(Constant.DB_FILE).configure()
        return SuccessResult().toMap()

#region plus_one 
    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def plus_one_category(cls,category:Category):
        cls.tracking_category_dal.add_amount_plus_one(category.username,category.category_id)
        return SuccessResult(Message.PROCESS_SUCCESSFUL).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def plus_one_sort(cls,sort:Sort):
        cls.tracking_sort_dal.add_amount_plus_one(sort.username,sort.sort_id)
        return SuccessResult(Message.PROCESS_SUCCESSFUL).toMap()
#endregion

#region get_category 
    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry_with_data)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def get_category(cls,category:Category):
        result = cls.tracking_category_dal.get(category.username,category.category_id)
        return SuccessDataResult(result,Message.PROCESS_SUCCESSFUL).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry_with_data)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def get_category_max(cls,category:Category):
        result = cls.tracking_category_dal.get_max(category.username)
        return SuccessDataResult(result,Message.PROCESS_SUCCESSFUL).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry_with_data)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def get_category_min(cls,category:Category):
        result = cls.tracking_category_dal.get_min(category.username)
        return SuccessDataResult(result,Message.PROCESS_SUCCESSFUL).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry_with_data)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def get_category_user(cls,category:Category):
        result = cls.tracking_category_dal.get_user(category.username)
        return SuccessDataResult(result,Message.PROCESS_SUCCESSFUL).toMap()
#endregion

#region get_sort 
    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry_with_data)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def get_sort(cls,sort:Sort):
        result = cls.tracking_sort_dal.get(sort.username,sort.sort_id)
        return SuccessDataResult(result,Message.PROCESS_SUCCESSFUL).toMap()
        
    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry_with_data)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def get_sort_max(cls,sort:Sort):
        result = cls.tracking_sort_dal.get_max(sort.username)
        return SuccessDataResult(result,Message.PROCESS_SUCCESSFUL).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry_with_data)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def get_sort_min(cls,sort:Sort):
        result = cls.tracking_sort_dal.get_min(sort.username)
        return SuccessDataResult(result,Message.PROCESS_SUCCESSFUL).toMap()

    @classmethod
    @Decorator.on_exception(DecoratorHelper.error_registry_with_data)
    @Decorator.on_before(DecoratorHelper.check_registry)
    def get_sort_user(cls,sort:Sort):
        result = cls.tracking_sort_dal.get_user(sort.username)
        return SuccessDataResult(result,Message.PROCESS_SUCCESSFUL).toMap()
#endregion

#region get_tag 
    @classmethod
    def get_category_tag(cls,category_id):
        if(category_id<1 or category_id>10):
            category_id=1
        return cls.category_dal.get(category_id)[0][1]

    @classmethod
    def get_sort_tag(cls,sort_id):
        if(sort_id<1 or sort_id>5):
            sort_id = 1
        return cls.sort_dal.get(sort_id)[0][1]
#endregion

