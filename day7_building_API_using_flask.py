'''
Project: Recipe API using Flask

Description:
This project involves building a simple REST API using Flask that allows users
to view and add recipes. The API handles HTTP requests and returns data in JSON format.

Features:
- Retrieve all recipes (GET request)
- Add a new recipe (POST request)
- Store data temporarily using a Python list

Concepts Used:
- Flask web framework
- API development (REST)
- HTTP methods (GET, POST)
- JSON handling in Python

Goal:
To understand how APIs are built and how client-server communication works.
'''

from flask import Flask, jsonify, request

app = Flask(__name__)
recipes = [
    {"name": "Pasta", "ingredients": ["noodles", "sauce"]},
    {"name": "Tea", "ingredients": ["water", "tea leaves"]}
]


@app.route("/")
def home():
    return "Recipe API is running!"

@app.route("/recipes")
def get_recipes():
    return jsonify(recipes)

@app.route("/recipes",methods = ["POST"])
def add_recipe():
    data = request.get_json()
    recipes.append(data)
    return jsonify({"message" : "Recipe Added!"})

if __name__ == "__main__":
    app.run(debug = True)

'''
Project Explanation: Recipe API using Flask

In this project, we built a simple REST API using Flask that allows users
to store and retrieve recipe data.

1. Flask Setup:
We imported Flask and created an application instance using:
    app = Flask(__name__)
This initializes the web server.

2. Data Storage:
We used a Python list called "recipes" to store recipe data.
Each recipe is a dictionary containing:
    - name (string)
    - ingredients (list)

Note: This data is temporary and resets when the server restarts.

3. Routes (Endpoints):

a) Home Route ("/"):
This route is used to check if the API is running.
It returns a simple message.

b) GET /recipes:
This route returns all stored recipes.
We use jsonify() to convert Python data into JSON format.

c) POST /recipes:
This route allows users to add a new recipe.
- We use request.get_json() to get data sent by the user.
- The new recipe is appended to the recipes list.
- A success message is returned.

4. HTTP Methods:
- GET → used to retrieve data
- POST → used to send data

5. JSON Handling:
Flask uses jsonify() to return responses in JSON format,
which is the standard format for APIs.

6. Running the Server:
The app runs locally using:
    app.run(debug=True)

This starts a development server at:
    http://127.0.0.1:5000/

7. Limitations:
- Data is not stored permanently
- No validation for incorrect input
- No unique IDs for recipes

8. Learning Outcome:
This project demonstrates how APIs are created,
how requests and responses work, and how data flows
between client and server.
'''