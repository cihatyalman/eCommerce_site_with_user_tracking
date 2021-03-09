import requests
from bs4 import BeautifulSoup

from Business.data_managers.tracking_manager import TrackingManager
from Core.utilities.results.success_data_result import SuccessDataResult

from Entities.product import Product, ProductDetail
from Entities.store import Store, StoreDetail

class ScrapingManager:

    __base_link = "https://www.cimri.com/"

    @classmethod
    def search_by_text(cls,search_text="",sort_id=0,return_object=False):
        request_link = "{}arama?q={}{}&page=1".format(cls.__base_link,search_text.replace(" ","+"),TrackingManager.get_sort_tag(sort_id))
        print(request_link)
        return cls.__get_product_list(request_link,return_object)

    @classmethod
    def search_by_category(cls,category_id=0,sort_id=0,return_object=False):
        request_link = "{}{}?{}&page=1".format(cls.__base_link,TrackingManager.get_category_tag(category_id),TrackingManager.get_sort_tag(sort_id))
        print(request_link)
        return cls.__get_product_list(request_link,return_object)

    @classmethod
    def __get_product_list(cls,link,return_object=False):
        soup = BeautifulSoup(requests.get(link).content,"html.parser")
        soup_data = soup.find_all("div",{"class":"s1cegxbo-1 cACjAF"})[0]
        data_list = soup_data.find_all("div",{"id":"cimri-product"})
        search_list = []
        for product_data in data_list:
            product = Product()
            product.name = product_data.find_all("h3",{"class":"product-title"})[0].text.strip()
            product.link = cls.__base_link+product_data.find_all("a",{"class":"link-detail"})[0]["href"]
            try:
                product.image = "https:"+product_data.find_all("div",{"class":"image-wrapper"})[0].div.img["data-src"]
            except:
                product.image = ""
            store_list = product_data.find_all("div",{"class":"top-offers"})[0].find_all("a")
            stores = []
            for store_data in store_list:
                store = Store()
                store.name = store_data.div.text.strip()
                store.price = store_data.text.replace(store.name,"")
                store.link = store_data["href"]
                stores.append(store.toMap())
            product.stores = stores
            if(return_object):
                search_list.append(product)
            else:
                search_list.append(product.toMap())
        return search_list

    @classmethod
    def get_product_detail(cls,product:Product):
        product_detail = ProductDetail(product.name,product.link,product.image)

        soup = BeautifulSoup(requests.get(product.link).content,"html.parser")
        soup_data = soup.find_all("div",{"class":"s1a29zcm-9 fpThqT"})[0]
        try:
            product_detail.detail = soup_data.find_all("div",{"class":"s1vwbahk-0 jdshGN"})[0].ul.text.strip()
        except:
            product_detail.detail = ""
        store_list = soup_data.find_all("table",{"class":"s17f9cy4-2 bJnpmt"})[0].find_all("tr",{"class":"s17f9cy4-3"})
        stores = []
        for store_data in store_list:
            store_detail = StoreDetail()
            store_detail.image = store_data.find_all("img",{"class":"s17f9cy4-10"})[0]["src"]
            try:
                tag = store_data.find_all("div",{"class":"s17f9cy4-0"})[0].text.strip()
                store_detail.price = store_data.find_all("div",{"class":"s17f9cy4-14 ifXJMM"})[0].text.strip().replace(tag,"")
            except:
                store_detail.price = store_data.find_all("div",{"class":"s17f9cy4-14 ifXJMM"})[0].text.strip()
            store_detail.link = store_data.find_all("a",{"class":"s17f9cy4-5 hhrBHG"})[0]["href"]
            stores.append(store_detail.toMap())
        
        product_detail.stores = stores
        return product_detail.toMap()
