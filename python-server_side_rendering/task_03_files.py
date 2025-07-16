from flask import Flask, render_template, request
import json
import csv
import os

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
            return data.get("products", [])
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


@app.route('/products')
def product():
    source = request.args.get("source")
    product_id = request.args.get("id")
    file_path=''

    if source == "json":
        file_path = 'products.json'

    elif source == "csv":
        file_path = 'pructs.csv'
    else:
        return render_template("product_display.html", error="Wrong source")

    if not os.path.exists(file_path):
        return render_template('product_display.html', error="File not found")

    if source == 'json':
        products = read_product_json(file_path)

    if source == 'csv':
        products = read_product_csv(file_path)

    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p["id"] == product_id]
            if not products:
                return render_template(
                    "product_display.html",
                    error="Product not found"
                )
        except ValueError:
            return render_template("product_display.html", error="Invalid ID")
    return render_template("product_display.html", products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
