from flask import Flask, jsonify, request

from Entities.user import User
from Entities.category import Category
from Entities.sort import Sort
from Entities.product import Product

from Business.data_managers.user_manager import UserManager
from Business.data_managers.tracking_manager import TrackingManager
from Business.web_scraping.scraping_manager import ScrapingManager

app = Flask(__name__)

@app.route('/')
def home():
    return "home"

#region User 
@app.route('/login', methods=["POST"])
def login():
    user = User()
    user.username = request.json.get("username")
    user.password = request.json.get("password")
    result = UserManager.check_password(user)
    return jsonify(result)

@app.route('/register', methods=["POST"])
def register():
    user = User()
    user.username = request.json.get("username")
    user.password = request.json.get("password")
    result = UserManager.add(user)
    return jsonify(result)

@app.route('/delete', methods=["POST"])
def delete():
    user = User()
    user.username = request.json.get("username")
    user.password = request.json.get("password")
    result = UserManager.delete(user)
    return jsonify(result)
#endregion

#region Tracking.plus_one 
@app.route('/plus_one_category',methods=["POST"])
def plus_one_category():
    category = Category()
    category.username = request.json.get("username")
    category.category_id = request.json.get("category_id")
    result = TrackingManager.plus_one_category(category)
    return jsonify(result)

@app.route('/plus_one_sort',methods=["POST"])
def plus_one_sort():
    sort = Sort()
    sort.username = request.json.get("username")
    sort.sort_id = request.json.get("sort_id")
    result = TrackingManager.plus_one_sort(sort)
    return jsonify(result)
#endregion

#region Tracking.get_category
@app.route('/get_category',methods=["POST"])
def get_category():
    category = Category()
    category.username = request.json.get("username")
    category.category_id = request.json.get("category_id")
    result = TrackingManager.get_category(category)
    return jsonify(result)

@app.route('/get_category_max',methods=["POST"])
def get_category_max():
    category = Category()
    category.username = request.json.get("username")
    category.category_id = request.json.get("category_id")
    result = TrackingManager.get_category_max(category)
    return jsonify(result)

@app.route('/get_category_min',methods=["POST"])
def get_category_min():
    category = Category()
    category.username = request.json.get("username")
    category.category_id = request.json.get("category_id")
    result = TrackingManager.get_category_min(category)
    return jsonify(result)

@app.route('/get_category_user',methods=["POST"])
def get_category_user():
    category = Category()
    category.username = request.json.get("username")
    category.category_id = request.json.get("category_id")
    result = TrackingManager.get_category_user(category)
    return jsonify(result)
#endregion

#region Tracking.get_sort
@app.route('/get_sort',methods=["POST"])
def get_sort():
    sort = Sort()
    sort.username = request.json.get("username")
    sort.sort_id = request.json.get("sort_id")
    result = TrackingManager.get_sort(sort)
    return jsonify(result)

@app.route('/get_sort_max',methods=["POST"])
def get_sort_max():
    sort = Sort()
    sort.username = request.json.get("username")
    sort.sort_id = request.json.get("sort_id")
    result = TrackingManager.get_sort_max(sort)
    return jsonify(result)

@app.route('/get_sort_min',methods=["POST"])
def get_sort_min():
    sort = Sort()
    sort.username = request.json.get("username")
    sort.sort_id = request.json.get("sort_id")
    result = TrackingManager.get_sort_min(sort)
    return jsonify(result)

@app.route('/get_sort_user',methods=["POST"])
def get_sort_user():
    sort = Sort()
    sort.username = request.json.get("username")
    sort.sort_id = request.json.get("sort_id")
    result = TrackingManager.get_sort_user(sort)
    return jsonify(result)
#endregion

#region Search
@app.route('/search_by_text', methods=["POST"])
def search_by_text():
    text = request.json.get("text","cep telefonu")
    if(text==""):
        text="cep telefonu"
    sort_id = int(request.json.get("sort_id",1))
    result = ScrapingManager.search_by_text(text,sort_id)
    return jsonify(result)

@app.route('/search_by_category', methods=["POST"])
def search_by_category():
    category_id = int(request.json.get("category_id",1))
    sort_id = int(request.json.get("sort_id",1))
    result = ScrapingManager.search_by_category(category_id,sort_id)
    return jsonify(result)

@app.route('/get_product', methods=["POST"])
def get_product():
    product = Product()
    product.name = request.json.get("name")
    product.link = request.json.get("link")
    product.image = request.json.get("image")
    result = ScrapingManager.get_product_detail(product)
    return jsonify(result)
#endregion


if '__main__' == __name__:
    #result = TrackingManager.db_configure()
    #print(result)

    app.run()
