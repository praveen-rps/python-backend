from flask import Flask, render_template, url_for, request
import sqlite3


app = Flask(__name__)
database = "books.db"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books")
def displaybooks():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()  
    query = "select * from books"
    cursor.execute(query)
    books = cursor.fetchall()
    return render_template("books.html", books=books)

@app.route("/save", methods=["GET"])
def addData():
    bookid = request.form.get('bookid')
    print("Book Id is ", bookid)
    name = request.form.get('name')
    author = request.form.get('author')
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()  
    print(bookid,name,author)
    query = "insert into books(bookid,name,author) values(?,?,?)"
    data = (bookid,name,author)
    cursor.execute(query,data)
    return "Book details are added..!"



if __name__ == '__main__':
    app.run(debug=True)

