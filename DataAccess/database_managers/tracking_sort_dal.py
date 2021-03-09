from Core.data_access.sqlite_base import SqliteBase
from Entities.sort import Sort
from DataAccess.database_managers.sort_dal import SortDal

class TrackingSortDal(SqliteBase):
    __table_name = "tracking_sort"

    def __init__(self, db_name):
        self.sort_dal = SortDal(db_name)
        super().__init__(db_name)
        self.__create_table()

    def __create_table(self):
        sql_code = """CREATE TABLE IF NOT EXISTS {} (username TEXT , sort_id INTEGER, amount INTEGER)""".format(self.__table_name)
        return super()._create_table(sql_code)

    def add(self,sort:Sort):
        sql_code = """INSERT INTO {} (username,sort_id,amount) VALUES (?,?,?)""".format(self.__table_name)
        return super()._add(sql_code,sort.username,sort.sort_id,sort.amount)
    
    def add_user(self,username):
        for index in range(len(self.sort_dal.sort_info)):
            sort = Sort(username,index+1,0)
            self.add(sort)
        return True
        
    def add_amount_plus_one(self,username,sort_id):
        sql_code = """UPDATE {0} 
        SET amount=(SELECT amount FROM {0} WHERE username='{1}' AND sort_id = {2})+1 
        WHERE username='{1}' AND sort_id = {2}""".format(self.__table_name,username,sort_id)
        return super()._update(sql_code)

    def delete(self,username,sort_id):
        sql_code = """DELETE FROM {} WHERE username='{}' AND sort_id={}""".format(self.__table_name,username,sort_id)
        return super()._delete(sql_code)

    def delete_user(self,username):
        sql_code = """DELETE FROM {} WHERE username='{}' """.format(self.__table_name,username)
        return super()._delete(sql_code)

    def get(self,username,sort_id):
        sql_code = """SELECT * FROM {} WHERE username = '{}' AND sort_id={}""".format(self.__table_name,username,sort_id)
        return self.convert_object_list(super()._get(sql_code))

    def get_user(self,username):
        sql_code = """SELECT * FROM {} WHERE username = '{}' """.format(self.__table_name,username)
        return self.convert_object_list(super()._get(sql_code))

    def get_max(self,username):
        sql_code = """SELECT username,sort_id,max(amount) as amount FROM {} WHERE username = '{}' """.format(self.__table_name,username)
        return self.convert_object_list(super()._get(sql_code))

    def get_min(self,username):
        sql_code = """SELECT username,sort_id,min(amount) as amount FROM {} WHERE username = '{}' """.format(self.__table_name,username)
        return self.convert_object_list(super()._get(sql_code))

    def convert_object_list(self,tuple_list):
        if(tuple_list):
            object_list = []
            for res in tuple_list:
                object_list.append(Sort(res[0],res[1],res[2]).toMap())
            return object_list
        else:
            return []
