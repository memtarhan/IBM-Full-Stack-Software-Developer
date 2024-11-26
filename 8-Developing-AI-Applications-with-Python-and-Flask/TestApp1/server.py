# Import the Flask class from the flask module
from flask import Flask, request, jsonify

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