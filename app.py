# Name: Asmaa Ali
# Module: 4 – Python APIs Case Study
# Assignment : CRUD API for Book Model
# Date: April 10, 2025
# Description:For this project, I developed a CRUD API using Flask and SQLAlchemy to manage a Book model 
# with the fields: id, book_name, author, and publisher. The application supports create, 
# read, and delete operations. I tested all endpoints using Postman to ensure functionality. 
# The completed project was uploaded to GitHub as required for submission.

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))

# Create DB
with app.app_context():
    db.create_all()

# Routes

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(
        book_name=request.json['book_name'],
        author=request.json['author'],
        publisher=request.json['publisher']
    )
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return {
        "book_name": book.book_name,
        "author": book.author,
        "publisher": book.publisher
    }

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted"}

if __name__ == '__main__':
    app.run(debug=True)
