from app import app
from flask import jsonify
import pymysql as sql
from flask import render_template

# @app.route('/', methods=['GET'])
# @app.route('/index', methods=['GET'])
# def     route_home() :
#     return "Hello world\n"

# @app.route('/user/<username>', methods=['POST'])
# def     route_add_user(username) :
#     return "User added\n"
# from app import app

@app.route('/', methods=['GET'])
def     route_index() :
    return render_template("index.html",
                            title="Test1",
                            myContent="My SUPER content !!")

@app.route('/user/<username>', methods=['GET'])
def     route_user(username) :
    return render_template("index.html",
                            title="Hello" + username,
                            myContent="My SUPER content for " + username + "!!!")


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