from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with  # rest api
from flask_sqlalchemy import SQLAlchemy  # for database
from login import login_api
import json

app = Flask(__name__)
api = Api(app)  # wrap app in an API, init the fact that app is an API
# define location of database to be, in relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)  # wrap app


class UserModel(db.Model):
    # primary key true -> this field has to be unique
    USER_ID = db.Column(db.Integer, primary_key=True)
    #password = db.Column(db.String(100), nullable=False)
    # nullable false -> this field has to have info
    Name = db.Column(db.String(100), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Birthday = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Phone = db.Column(db.Integer, nullable=False)
    City = db.Column(db.String(100), nullable=False)
    Country = db.Column(db.String(100), nullable=False)

    def __repr__(self):  # wrapper method, so when print this out, get valid json format
        return f"User(name = {name}, age = {age}, birthday = {birthday}, email = {email}, phone = {phone}, city = {city}, country = {country})"


# class PostModel(db.Model):
#     Post_ID = db.Column(db.Integer, primary_key=True)
#     Post_Title = db.Column(db.String(100), nullable=False)
#     Post_Description = db.Column(db.String(100), nullable=False)
#     Post_Image = db.Column(db.String(100), nullable=False)

#     def __repr__(self):
#         return f"Video(title = {title}, description = {description})"


#############
# ONLY once
#############
db.create_all()  # only call once to instantiate, if keep calling, overrides what we alr have
#db.session.commit()


users = [
    {
        "USER_ID": 1,
        "Name": 'Brose McCreery',
        "Age": 22,
        "Birthday": '1993-03-01',
        "Email": 'bmccreery0@bloomberg.com',
        "Phone": '(858) 1604103',
        "City": 'Gujba',
        "Country": 'Nigeria'
    },
    {
        "USER_ID": 2,
        "Name": 'Darla Joret',
        "Age": 23,
        "Birthday": '1996-09-08',
        "Email": 'djoret1@latimes.com',
        "Phone": '(859) 9667080',
        "City": 'Zoumaping',
        "Country": 'China'
    },
    {
        "USER_ID": 3,
        "Name": 'Marcia Ivasyushkin',
        "Age": 16,
        "Birthday": '2000-06-17',
        "Email": 'mivasyushkin2@nydailynews.com',
        "Phone": '(412) 6782559',
        "City": 'Três de Maio',
        "Country": 'Brazil'
    },
    {
        "USER_ID": 4,
        "Name": 'Sherlock Ryde',
        "Age": 22,
        "Birthday": '1991-06-08',
        "Email": 'sryde3@ed.gov',
        "Phone": '(190) 6466427',
        "City": 'Baroh',
        "Country": 'Indonesia'
    },
    {
        "USER_ID": 5,
        "Name": 'Quintus Mahaddy',
        "Age": 22,
        "Birthday": '1996-08-26',
        "Email": 'qmahaddy4@123-reg.co.uk',
        "Phone": '(567) 3310071',
        "City": 'Cruz das Almas',
        "Country": 'Brazil'
    },
    {
        "USER_ID": 6,
        "Name": 'Garwood Dumingos',
        "Age": 18,
        "Birthday": '1999-07-26',
        "Email": 'gdumingos5@wufoo.com',
        "Phone": '(779) 6222613',
        "City": 'Tabuaço',
        "Country": 'Portugal'
    },
    {
        "USER_ID": 7,
        "Name": 'Laural Wallach',
        "Age": 30,
        "Birthday": '1998-01-11',
        "Email": 'lwallach6@github.com',
        "Phone": '(283) 8439630',
        "City": 'Périgueux',
        "Country": 'France'
    },
    {
        "USER_ID": 8,
        "Name": 'Christen Purchon',
        "Age": 28,
        "Birthday": '1992-04-24',
        "Email": 'cpurchon7@umich.edu',
        "Phone": '(872) 8312472',
        "City": 'Przasnysz',
        "Country": 'Poland'
    },
    {
        "USER_ID": 9,
        "Name": 'Eunice Kirk',
        "Age": 19,
        "Birthday": '1992-10-06',
        "Email": 'ekirk8@hatena.ne.jp',
        "Phone": '(847) 8038365',
        "City": 'Bassar',
        "Country": 'Togo'
    },
    {
        "USER_ID": 10,
        "Name": 'Kessia Landeg',
        "Age": 28,
        "Birthday": '1990-04-06',
        "Email": 'klandeg9@bluehost.com',
        "Phone": '(280) 8616457',
        "City": 'Bratsigovo',
        "Country": 'Bulgaria'
    }
]

# db.session.bulk_save_objects(users)
# db.session.commit()
for elem in users:
    jsonstr =  elem
    jsonobj =  json.dumps(jsonstr)
    db.session.add(jsonobj)
    db.session.commit()



@app.route('/')
def home():
    return {"message": "test TT3_5"}


@app.route('/home', methods=['GET'])
def testhome():

    return {"message": "hello TT3_5"}


app.register_blueprint(login_api)

if __name__ == "__main__": 
	app.run(debug=True)   # debug info for logging, only run in development environment
