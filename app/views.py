from app import app
from flask import jsonify
import pymysql as sql
from flask import render_template, Flask, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = '1234'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'lyvia'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'epytodo'

mysql = MySQL(app)

# @app.route('/pythonlogin/', methods=['GET', 'POST'])
# def login():
#     return render_template('index.html', msg='welcome!')
#     # Output message if something goes wrong...
#     msg = 'This doesnt work try again'
#     # Check if "username" and "password" POST requests exist (user submitted form)
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         # Create variables for easy access
#         username = request.form['username']
#         password = request.form['password']
#         # Check if account exists using MySQL
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
#         # Fetch one record and return result
#         account = cursor.fetchone()
#     # If account exists in accounts table in out database
#     if account:
#         # Create session data, we can access this data in other routes
#         session['loggedin'] = True
#         session['id'] = account['id']
#         session['username'] = account['username']
#         # Redirect to home page
#         return 'Logged in successfully!'
#     else:
#         # Account doesnt exist or username/password incorrect
#         msg = 'Incorrect username/password!'

@app.route('/pythonlogin/', methods=['GET', 'POST'])
def route_index():
    # Output message if something goes wrong...
    msg = 'Ca ne fonctionne pas'
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/pythonlogin/logout')
def logout():
     # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))

# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
            # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/pythonlogin/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('acceuil.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# @app.route('/', methods=['GET'])
# def     route_index() :
#     return render_template("connexion.html",
#                             title="Test1",
#                             myContent="My SUPER content !!")

# @app.route('/user/<username>', methods=['GET'])
# def     route_user(username) :
#     return render_template("connexion.html",
#                             title="Hello" + username,
#                             myContent="My SUPER content for " + username + "!!!")


# @app.route('/user')
# def route_all_users():
#     result = "corentin"
#     try:
#     ## We ’re creating connection between our mysql server and our app
#         connect = sql.connect(host = 'localhost',
#                             unix_socket = 'path_to_our_mysql_socket',
#                             user = '_user',
#                             passwd = '_password',
#                             db = 'name_of_your_database'
#                             )
#     ## We ’re retrieving a " pointer " aka " cursor " to our database
#         cursor = connect.cursor()
#         ## We ’re executing a SQL command ,
#         ## assuming that all tables are already created
#         cursor.execute(" SELECT * from user ")
#         ## We ’re retrieving all results
#         result = cursor.fetchall()
#         ## We ’re closing our cursor and our connection
#         cursor.close()
#         connect.close()
#     except Exception as e :
#         print(" Caught an exception : ", e )
#     ## We ’re sending the data
#     return jsonify(result)