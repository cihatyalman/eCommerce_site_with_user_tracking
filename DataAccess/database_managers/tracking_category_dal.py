from Core.data_access.sqlite_base import SqliteBase
from Entities.category import Category
from DataAccess.database_managers.category_dal import CategoryDal

class TrackingCategoryDal(SqliteBase):
    __table_name = "tracking_category"

    def __init__(self, db_name):
        self.category_dal = CategoryDal(db_name)
        super().__init__(db_name)
        self.__create_table()

    def __create_table(self):
        sql_code = """CREATE TABLE IF NOT EXISTS {} (username TEXT , category_id INTEGER, amount INTEGER)""".format(self.__table_name)
        return super()._create_table(sql_code)

    def add(self,category:Category):
        sql_code = """INSERT INTO {} (username,category_id,amount) VALUES (?,?,?)""".format(self.__table_name)
        return super()._add(sql_code,category.username,category.category_id,category.amount)
    
    def add_user(self,username):
        for index in range(len(self.category_dal.categories)):
            category = Category(username,index+1,0)
            self.add(category)
        return True

    def add_amount_plus_one(self,username,category_id):
        sql_code = """UPDATE {0} 
        SET amount=(SELECT amount FROM {0} WHERE username='{1}' AND category_id = {2})+1 
        WHERE username='{1}' AND category_id = {2}""".format(self.__table_name,username,category_id)
        return super()._update(sql_code)

    def delete(self,username,category_id):
        sql_code = """DELETE FROM {} WHERE username='{}' AND category_id={}""".format(self.__table_name,username,category_id)
        return super()._delete(sql_code)

    def delete_user(self,username):
        sql_code = """DELETE FROM {} WHERE username='{}' """.format(self.__table_name,username)
        return super()._delete(sql_code)

    def get(self,username,category_id):
        sql_code = """SELECT * FROM {} WHERE username = '{}' AND category_id={}""".format(self.__table_name,username,category_id)
        return self.convert_object_list(super()._get(sql_code))

    def get_user(self,username):
        sql_code = """SELECT * FROM {} WHERE username = '{}' """.format(self.__table_name,username)
        return self.convert_object_list(super()._get(sql_code))

    def get_max(self,username):
        sql_code = """SELECT username,category_id,max(amount) as amount FROM {} WHERE username = '{}' """.format(self.__table_name,username)
        return self.convert_object_list(super()._get(sql_code))

    def get_min(self,username):
        sql_code = """SELECT username,category_id,min(amount) as amount FROM {} WHERE username = '{}' """.format(self.__table_name,username)
        return self.convert_object_list(super()._get(sql_code))

    def convert_object_list(self,tuple_list):
        if(tuple_list):
            object_list = []
            for res in tuple_list:
                object_list.append(Category(res[0],res[1],res[2]).toMap())
            return object_list
        else:
            return []
