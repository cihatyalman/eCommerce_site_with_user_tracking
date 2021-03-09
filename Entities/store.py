class Store:
    def __init__(self,name="",price="",link=""):
        self.name = name
        self.price = price
        self.link = link

    def toMap(self):
        map={}
        map["name"] = self.name
        map["price"] = self.price
        map["link"] = self.link
        return map

class StoreDetail:
    def __init__(self, image="", price="", link=""):
        self.image = image
        self.price = price
        self.link = link

    def toMap(self):
        map={}
        map["image"] = self.image
        map["price"] = self.price
        map["link"] = self.link
        return map
