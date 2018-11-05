from flask import *
from databases import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop', methods = ['POST', 'GET'])
def shop_page():
    # phones = ["Samsung Galaxy 8", "Samsung Galaxy 9", "Samsung Galaxy 7+", "iPhone 7"] 
    if request.method == 'POST':
        phones = get_all_products()
        result = request.form['search']
        phones = prod_by_name(result)
        return render_template("shop.html", phones=phones, result = result)
    else:
        phones = get_all_products()
        return render_template("shop.html", phones=phones, result = "null")


if __name__ == '__main__':
   app.run(debug = True)