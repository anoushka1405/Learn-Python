from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Books API"

books = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear"
    },
    {
        "id": 2,
        "title": "Deep Work",
        "author": "Cal Newport"
    }
]

@app.route("/books")
def get_books():
    return books

@app.route("/books/<id>")
def get_book_from_id(id):
    for book in books:
        if book["id"]==int(id):
            return book
        
    return f"Book with id : {id} not found!"

data = {
    "title" : "Clean Code",
    "author": "Robert Martin"
}

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    new_id = len(books)+1
    
    new_book = {
        "id" : new_id,
        "title" : data["title"],
        "author" : data["author"]
    }
    books.append(new_book)
    print("Book Added successfuly!")
    return new_book


if __name__ == "__main__":
    app.run(debug = True)

