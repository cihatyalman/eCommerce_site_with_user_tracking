from Core.data_access.sqlite_base import SqliteBase
from Business.constants.constant import Constant
from Entities.user import User

class UserDal(SqliteBase):

    __table_name = "registries"

    def __init__(self, db_name):
        super().__init__(Constant.DB_FILE)
        self.__create_table()
    
    def __create_table(self):
        sql_code = """CREATE TABLE IF NOT EXISTS {} (username TEXT, password TEXT)""".format(self.__table_name)
        return super()._create_table(sql_code)

    def add(self,user:User):
        sql_code = """INSERT INTO {} (username,password) VALUES (?,?)""".format(self.__table_name)
        return super()._add(sql_code,user.username,user.password)

    def delete(self,user:User):
        sql_code = """DELETE FROM {} WHERE username='{}'""".format(self.__table_name,user.username)
        return super()._delete(sql_code)

    def get(self,username):
        sql_code = """SELECT * FROM {} WHERE username = '{}'""".format(self.__table_name,username)
        return self.convert_object_list(super()._get(sql_code))

    def convert_object_list(self,tuple_list):
        if(tuple_list):
            object_list = []
            for res in tuple_list:
                object_list.append(User(res[0],res[1]))
            return object_list
        else:
            return []
