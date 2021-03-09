class Sort:
    
    def __init__(self,username="",sort_id=0,amount=0):
        self.username = username
        self.sort_id = sort_id
        self.amount = amount

    def toMap(self):
        map = {}
        map["username"] = self.username
        map["sort_id"] = self.sort_id
        map["amount"] = self.amount
        return map
