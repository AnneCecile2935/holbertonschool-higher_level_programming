from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open("items.json") as f:
        data = json.load(f)
    items_list = data.get("items", [])
    return render_template('items.html', items=items_list)


def read_product_json(filename="products.json"):
    try:
        with open(filename) as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Error JSON: {e}")
        return []


def read_product_csv(filename="products.csv"):
    products = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
                products.append(product)
    except Exception as e:
        print(f"Error CSV : {e}")
    return products

def read_sqlite(db_path="products.db"):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row['id'],
                "name": row['name'],
                "category": row['category'],
                "price": row['price']
            })
            conn.close()
    except Exception as e:
        print("Database error: {e}")
    return products


@app.route('/products')
def product():
    source = request.args.get("source")
    id_str = request.args.get("id")

    if source == "json":
        data = read_product_json()
    elif source == "csv":
        data = read_product_csv()
    elif source == "sql":
        data = read_sqlite()
    else:
        return render_template("product_display.html", error="Wrong source")

    if id_str:
        try:
            product_id = int(id_str)
        except ValueError:
            return render_template(
                'product_display.html',
                error="Invalid id format",
                products=None
            )
        filtered = [p for p in data if p['id'] == product_id]
        if not filtered:
            return render_template(
                'product_display.html',
                error="Product not found",
                products=None
            )
        return render_template(
            'product_display.html',
            products=filtered,
            error=None
            )

    return render_template('product_display.html', products=data, error=None)




if __name__ == '__main__':
    app.run(debug=True, port=5000)
