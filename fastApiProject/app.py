from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
import sqlite3

app = Flask(__name__)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = True, nullable=False)
    description = db.Column(db.string(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')

def index():
    return "hello"


@app.route('/drinks')
def get_drinks():
    return {'drinks': 'drink data'}