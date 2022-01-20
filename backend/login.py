from flask import Flask, Blueprint
import requests
from flask_sqlalchemy import SQLAlchemy #for database
import bcrypt

app = Flask(__name__) 
login_api = Blueprint('login_api', __name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # define location of database to be, in relative path
db = SQLAlchemy(app) #wrap app 

# @login_api.record
# def record(state):
#     db = state.app.config.get("database.db")

#     if db is None:
#         raise Exception("oops")

@ login_api.route('/login', methods=['POST'])
def login():
    db = app.config["SQLALCHEMY_DATABASE_URI"]
    result = db.UserModel.find_one({'id': requests.form['id']})
    hashed_password = result['password']
    password = requests.form['password']
    finalResult = bcrypt.checkpw(password.encode('utf8'), hashed_password)
    if finalResult == True:
        return {'message': 'logged in'}
    else:
        return {'message': 'login failed'}