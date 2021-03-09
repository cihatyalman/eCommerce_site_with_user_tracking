class User:
    def __init__(self,username="",password=""):
        self.username = username
        self.password = password

    def toMap(self):
        map = {}
        map["username"] = self.username
        map["password"] = self.password
        return map
