from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'pythonlogin'

# Intialize MySQL
mysql = MySQL(app)
# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    return render_template('index.html', msg='welcome!')

# @app.route('/', methods=['GET'])
# def     route_index() :
#     return render_template("index.html",
#                             title="Test1",
#                             myContent="My SUPER content !!")

# @app.route('/user/<username>', methods=['GET'])
# def     route_user(username) :
#     return render_template("index.html",
#                             title="Hello" + username,
#                             myContent="My SUPER content for " + username + "!!!")