from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with #rest api
from flask_sqlalchemy import SQLAlchemy #for database
from login import login_api

app = Flask(__name__) 
api = Api(app) #wrap app in an API, init the fact that app is an API
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # define location of database to be, in relative path
db = SQLAlchemy(app) #wrap app 

class UserModel(db.Model):
    USER_ID = db.Column(db.Integer, primary_key=True) #primary key true -> this field has to be unique
    #password = db.Column(db.String(100), nullable=False)
    Name = db.Column(db.String(100), nullable=False) #nullable false -> this field has to have info
    Age = db.Column(db.Integer, nullable=False)
    Birthday = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Phone = db.Column(db.Integer, nullable=False)
    City = db.Column(db.String(100), nullable=False)
    Country = db.Column(db.String(100), nullable=False)


    def __repr__(self): #wrapper method, so when print this out, get valid json format
        return f"Video(name = {name}, age = {age}, birthday = {birthday}, email = {email}, phone = {phone}, city = {city}, country = {country})"

class PostModel(db.Model):
    Post_ID = db.Column(db.Integer, primary_key=True)
    Post_Title = db.Column(db.String(100), nullable=False)
    Post_Description = db.Column(db.String(100), nullable=False)
    Post_Image = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Video(title = {title}, description = {description})"


#############
# ONLY once
#############
#db.create_all() #only call once to instantiate, if keep calling, overrides what we alr have

@app.route('/')
def home():
    return {"message": "test TT3_5"}


@app.route('/home', methods=['GET'])
def testhome():

    return {"message": "hello TT3_5"}

app.register_blueprint(login_api)

if __name__ == "__main__": 
	app.run(debug=True)   # debug info for logging, only run in development environment
