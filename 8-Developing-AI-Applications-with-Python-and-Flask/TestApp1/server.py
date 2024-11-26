# Import the Flask class from the flask module
from flask import Flask, request, jsonify
import requests

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
# @app.route("/")
# def home():
#     return "Hello, World!"


# return a JSON
@app.route("/")
def home():
    return {'message': 'Hello, World!'}

@app.route("/health", methods=["GET", "POST"])
def health():
    if request.method == "GET":
        return jsonify(status="OK", method="GET"), 200
    if request.method == "POST":
        return jsonify(status="OK", method="POST"), 200

@app.route('/')
def get_course_info():
    course = request.args["course"]
    rating = request.args.get("rating")
    return {"message": f"{course} with rating {rating}"}

@app.route("/favorite-author")
def get_favorite_author():
    res = requests.get('https://openlibrary.org/authors/OL19981A/Stephen_King')
    if res.status_code == 200:
        return {'message': res}
    elif res.status_code == 404:
        return {'message': 'Something went wrong!'}, 400
    else:
        return {'message': 'Server error'}, 500


@app.route("/book/<isbn>")
def get_author(isbn):
    res = requests.get("https://openlibrary.org/isbn/{escape(isbn)}.JSON")

    if res.status_code == 200:
        return {'message': res.JSON()}
    elif res.status_code == 404:
        return {'message': 'Something went wrong!'}, 404
    else:
        return {'message': 'Server error'}, 500


