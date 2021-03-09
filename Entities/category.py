class Category:
    
    def __init__(self,username="",category_id=0,amount=0):
        self.username = username
        self.category_id = category_id
        self.amount = amount

    def toMap(self):
        map = {}
        map["username"] = self.username
        map["category_id"] = self.category_id
        map["amount"] = self.amount
        return map
