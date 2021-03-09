from Core.utilities.results.error_result import ErrorResult
from Core.utilities.results.error_data_result import ErrorDataResult
from Business.constants.constant import Constant
from DataAccess.database_managers.user_dal import UserDal
from Business.constants.message import Message

class DecoratorHelper:

    user_dal = UserDal(Constant.DB_FILE)

    @classmethod
    def error_registry(cls,*args):
        return ErrorResult(Message.REGISTRATION_NOT_FOUND).toMap()
    
    @classmethod
    def error_registry_with_data(cls,*args):
        return ErrorDataResult(Message.REGISTRATION_NOT_FOUND).toMap()

    @classmethod
    def check_registry(cls,*args):
        registry = cls.user_dal.get(args[1].username)
        if(not registry):
            raise Exception()
