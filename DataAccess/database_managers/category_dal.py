from Core.data_access.sqlite_base import SqliteBase

class CategoryDal(SqliteBase):
    categories = [
        {"tag":"elektronik","name":"Elektronik"},
        {"tag":"gida","name":"Gıda"},
        {"tag":"ev-yasam-ofis-kirtasiye","name":"Ev, Yaşam, Kırtasiye"},
        {"tag":"anne-bebek-oyuncak","name":"Anne, Bebek, Oyuncak"},
        {"tag":"saat-moda-taki","name":"Giyim"},
        {"tag":"kitap-muzik-hobi","name":"Kitap"},
        {"tag":"spor-outdoor","name":"Spor"},
        {"tag":"saglik-bakim-kozmetik","name":"Sağlık"},
        {"tag":"oto-bahce-yapi-market","name":"Yapı Market"},
        {"tag":"supermarket-petshop","name":"Süper Market"}
    ]

    __table_name="categories"

    def __init__(self,db_name):
        super().__init__(db_name)

    def __create_table(self):
        sql_code = """CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, tag TEXT, name TEXT)""".format(self.__table_name)
        super()._create_table(sql_code)
        self.__add()
    
    def __add(self):
        sql_code = """INSERT INTO {} (tag, name) VALUES (?,?)""".format(self.__table_name)
        for category in self.categories:
            super()._add(sql_code, category["tag"],category["name"])

    def get(self,id):
        sql_code = """SELECT * FROM {} WHERE id={}""".format(self.__table_name,str(id))
        return super()._get(sql_code)

    def configure(self):
        "Run once !"
        self.__create_table()
