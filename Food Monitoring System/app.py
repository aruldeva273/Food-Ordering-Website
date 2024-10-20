from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aruldeva@273",
        database="food_ordering_db"
    )

# Route for the home page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for the checkout page (checkout.html)
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Retrieve form data from checkout page
        name = request.form['name']
        address = request.form['address']
        item = request.form['item']
        quantity = request.form['quantity']

        # Save form data into MySQL database
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO orders (name, address, item, quantity) VALUES (%s, %s, %s, %s)"
        values = (name, address, item, quantity)
        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('order_success'))

    return render_template('checkout.html')

# Route for order success page
@app.route('/order-success')
def order_success():
    return "Your order has been successfully placed!"

if __name__ == '__main__':
    app.run(debug=True)


"""from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aruldeva@273",
    database="food_ordering_db"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        food_item = request.form['food_item']
        quantity = request.form['quantity']

        # Insert order into database
        cursor = db.cursor()
        query = "INSERT INTO orders (name, food_item, quantity) VALUES (%s, %s, %s)"
        values = (name, food_item, quantity)
        cursor.execute(query, values)
        db.commit()

        return redirect(url_for('success'))

    return render_template('checkout.html')

@app.route('/success')
def success():
    return "Order successfully placed!"

if __name__ == '__main__':
    app.run(debug=True)
"""