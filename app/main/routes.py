from flask import redirect, request
from flask.templating import render_template
from . import bp
from app.models import Book
from app import db

@bp.route("/")
def index():
    books = Book.query.all()
    return render_template("main/home.html", books=books)

@bp.route("/delete_book", methods=["POST"])
def delete_book():
    id = request.form["id"]
    book = Book.query.filter(Book.id == id).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return redirect("/")
    else:
        return redirect("/")


@bp.route("/create_book", methods=["GET", "POST"])
def create_book():
    if request.method == "GET":
        return render_template("main/create_book.html")
    else:
        title = request.form["title"]
        book = Book(title=title)
        db.session.add(book)
        db.session.commit()
        return redirect("/")


@bp.route("/edit_book/<id>", methods=["GET", "POST"])
def edit_book(id):
    book = Book.query.filter(Book.id == id).first()
    if request.method == "GET":
        return render_template("main/create_book.html", book=book)
    else:
        title = request.form["title"]
        book.title = title
        db.session.add(book)
        db.session.commit()
        return redirect("/")