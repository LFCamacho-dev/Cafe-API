from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

#region CRUD COMMANDS
# CREATE RECORD
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# READ ALL RECORDS
# all_books = session.query(Book).all()

# READ A PARTICULAR RECORD BY QUERY
# book = Book.query.filter_by(title="Harry Potter").first()

# UPDATE A PARTICULAR RECORD BY QUERY
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# UPDATE A RECORD BY PRIMARY KEY
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()

# DELETE A PARTICULAR RECORD BY PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
#endregion


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
