# import sqlite3
#
# # create a database
# db = sqlite3.connect("books-collection.db")
#
# # create a cursor for controlling the database
# cursor = db.cursor()
#
# # Create a table in the database
# cursor.execute(
#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
import SQLAlchemy
import flask_sqlalchemy

