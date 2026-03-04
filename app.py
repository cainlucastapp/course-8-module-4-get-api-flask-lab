from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    # TODO: Return a welcome message
    return jsonify({"message": "welcome"})

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products")
def get_products():
    # TODO: Return all products or filter by ?category=
    category = request.args.get("category")
    if category:
        filtered_products = [product for product in products if product["category"] == category]
        return jsonify(filtered_products)
    return jsonify(products)


# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    # TODO: Return product by ID or 404
    product = next((product for product in products if product["id"] == id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
