class Product:
    def __init__(self,name="",link="",image="",stores=[]):
        self.name = name
        self.link = link
        self.image = image
        self.stores = stores

    def toMap(self):
        map = {}
        map["name"] = self.name
        map["link"] = self.link
        map["image"] = self.image
        map["stores"] = self.stores
        return map


class ProductDetail(Product):
    def __init__(self, name='', link='', image='', stores=[], detail=""):
        super().__init__(name, link, image, stores)
        self.detail = detail

    def toMap(self):
        map = super().toMap()
        map["stores"] = self.stores
        map["detail"] = self.detail
        return map
