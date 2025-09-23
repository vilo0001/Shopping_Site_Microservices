from flask import Flask, jsonify, request, make_response
import requests

app = Flask(__name__)

products_db = []
data = requests.get('https://dummyjson.com/products')
products_db = data.json()["products"]


@app.route('/products', methods=['GET'])
def getProducts():
    result = products_db

    title = request.args.get("title")
    category = request.args.get("category")
    sortBy = request.args.get("sortBy")
    sortType = request.args.get("sortType")
    availabilityStatus = request.args.get("availabilityStatus")

    # ?name=Essence%20Mascara%20Lash%20Princess
    if title:
        result = list(filter(lambda x: x["title"] == title, result))

    if category:
        result = list(filter(lambda x: x["category"] == category, result))

    if sortBy:
        match sortBy:
            case "name":
                # Virker ikke.
                result.sort(key=result["name"])
            case "price":
                result.sort(key=result["price"])

        # If an exact match is not confirmed, this last case will be used if provided
            case _:
                return "Something's wrong with the internet"

    return jsonify(result), 200

app.run(port=5004)