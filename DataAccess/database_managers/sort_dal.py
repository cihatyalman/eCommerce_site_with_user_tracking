from Core.data_access.sqlite_base import SqliteBase

class SortDal(SqliteBase):
    sort_info = [
        {"tag":"","name":"En Popüler Ürünler"},
        {"tag":"&sort=price%2Casc","name":"En Düşük Fiyat"},
        {"tag":"&sort=price%2Cdesc","name":"En Yüksek Fiyat"},
        {"tag":"&sort=new%2Cdesc","name":"En Yeni Ürünler"},
        {"tag":"&sort=discount%2Cdesc","name":"Fiyatı Düşenler"}
    ]

    __table_name="sort"

    def __init__(self,db_name):
        super().__init__(db_name)

    def __create_table(self):
        sql_code = """CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, tag TEXT, name TEXT)""".format(self.__table_name)
        super()._create_table(sql_code)
        self.__add()
    
    def __add(self):
        sql_code = """INSERT INTO {} (tag, name) VALUES (?,?)""".format(self.__table_name)
        for sort in self.sort_info:
            super()._add(sql_code, sort["tag"], sort["name"])
    
    def get(self,id):
        sql_code = """SELECT * FROM {} WHERE id={}""".format(self.__table_name,str(id))
        return super()._get(sql_code)

    def configure(self):
        "Run once !"
        self.__create_table()
