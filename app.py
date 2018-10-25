from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop')
def shop_page():
    phones = ["Samsung Galaxy 8", "Samsung Galaxy 9", "Samsung Galaxy 7+", "iPhone 7"] 
    return render_template("shop.html", phones=phones)

if __name__ == '__main__':
   app.run(debug = True)