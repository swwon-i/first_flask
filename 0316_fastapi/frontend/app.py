from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login-jquery.html')

@app.route('/register')
def register():
    return render_template('register-jquery.html')

@app.route('/products')
def product():
    return render_template('products.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/orders')
def order():
    return render_template('orders.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)