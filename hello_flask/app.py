<<<<<<< HEAD
from flask import Flask,render_template,request,jsonify
=======
from flask import Flask,render_template,request,send_from_directory
>>>>>>> 1e808fdf2545ee096a12772117dff75fdd0c0aaf
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt

import jwt

import datetime
import bcrypt

import json

from db_con import get_db_instance, get_db

from db_con import get_db_instance, get_db

app = Flask(__name__)
FlaskJSON(app)

USER_PASSWORDS = { "cjardin": "strong password"}

IMGS_URL = {
            "DEV" : "/static",
            "INT" : "https://cis-444-fall-2021.s3.us-west-2.amazonaws.com/images",
            "PRD" : "http://d2cbuxq67vowa3.cloudfront.net/images"
            }

CUR_ENV = "DEV"
<<<<<<< HEAD
JWT_SECRET = None

global_db_con = get_db()


with open("secret", "r") as f:
    JWT_SECRET = f.read()
=======

JWT_SECRET = None
with open("mysecret", "r") as f:
    JWT_SECRET = f.read()

global_db_con = get_db()

>>>>>>> 1e808fdf2545ee096a12772117dff75fdd0c0aaf

@app.route('/') #endpoint
def index():
    return 'Web App with Python Ryan!' + USER_PASSWORDS['cjardin']
    #return render_template('/ryanssite/index.html')

@app.route('/buy') #endpoint
def buy():
    return 'Buy'

@app.route('/hello') #endpoint
def hello():
    return render_template('hello.html',img_url=IMGS_URL[CUR_ENV] ) 

@app.route('/back',  methods=['GET']) #endpoint
def back():
    return render_template('backatu.html',input_from_browser=request.args.get('usay', default = "nothing", type = str) )

@app.route('/backp',  methods=['POST']) #endpoint
def backp():
    print(request.form)
    salted = bcrypt.hashpw( bytes(request.form['fname'],  'utf-8' ) , bcrypt.gensalt(12))
    print(salted)

    print(  bcrypt.checkpw(  bytes(request.form['fname'],  'utf-8' )  , salted ))

    return render_template('backatu.html',input_from_browser= str(request.form) )

@app.route('/auth',  methods=['POST']) #endpoint
def auth():
        print(request.form)
        return json_response(data=request.form)



#Assigment 2
@app.route('/ss1') #endpoint
def ss1():
    return render_template('server_time.html', server_time= str(datetime.datetime.now()), img_url=IMGS_URL[CUR_ENV] )
    #return render_template('server_time.html', img_url=IMGS_URL[CUR_ENV] )

@app.route('/getTime') #endpoint
def get_time():
<<<<<<< HEAD
    #return json_response(data={"password" : request.args.get('password'),
    #                           "class" : "cis44",
    #                          "serverTime":str(datetime.datetime.now())
    #                     }
    #        )
    return render_template('client_time.html', server_time= str(datetime.datetime.now()), img_url=IMGS_URL[CUR_ENV] )

@app.route('/auth2') #endpoint
def auth2():
    jwt_str = jwt.encode({"username" : "cary",
                            "age" : "so young",
                            "books_ordered" : ['f', 'e'] } 
                            , JWT_SECRET, algorithm="HS256")
    #print(request.form['username'])
    return json_response(jwt=jwt_str)

@app.route('/exposejwt') #endpoint
def exposejwt():
    jwt_token = request.args.get('jwt')
    print(jwt_token)
    return json_response(output=jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"]))


@app.route('/hellodb') #endpoint
def hellodb():
    cur = global_db_con.cursor()
    cur.execute("insert into music values( 'dsjfkjdkf', 1);")
    global_db_con.commit()
    return json_response(status="good")
=======
    return json_response(data={"password" : request.args.get('password'),
                                "class" : "cis44",
                                "serverTime":str(datetime.datetime.now())})

@app.route('/getClientTime') #endpoint
def get_client_time():
    return render_template('client_time.html', img_url=IMGS_URL[CUR_ENV])
>>>>>>> 1e808fdf2545ee096a12772117dff75fdd0c0aaf


@app.route('/easy') #endpoint
def twe():
    return render_template('thatWasEasy.html', img_url=IMGS_URL[CUR_ENV])



#assignment 3
@app.route('/authUser', methods=['POST']) #endpoint
def authUser():
    
    cur = global_db_con.cursor()
    username = request.form['uname']
    validUser = False
    isLind = "False" #I promised my friend a birthday message

    cur.execute("select password from users where username = '{}'".format(username))
    for item in cur.fetchall():
        if bcrypt.checkpw(  bytes(request.form['pword'],'utf-8' )  , bytes(item[0], 'utf-8')):
            validUser = True
    
    if validUser:
        if username == "Lindsey":
            isLind = "True"
            print(isLind)
        jwt_str = jwt.encode({"username" : username}, JWT_SECRET, algorithm="HS256")
        return json_response(jwt=jwt_str, lind=isLind)
    else:
        return json_response(jwt='BadRequest')

@app.route('/bookStore') #endpoint
def bookStore():
    return render_template('login_buy_confirm.html', img_url=IMGS_URL[CUR_ENV])

@app.route('/makeUser', methods=['POST']) #endpoint
def makeUser():

    cur = global_db_con.cursor()
    
    salted = bcrypt.hashpw( bytes(request.form['pword'],  'utf-8' ) , bcrypt.gensalt(12))
    username = request.form['uname'] 
    cur.execute("insert into users (username, password) values ('{}','{}')".format(username, salted.decode("utf-8")))
        
    global_db_con.commit()

    cur.execute("select password from users where username = '{}'".format(username))
    for item in cur.fetchall():
        print(item[0])
        print(  bcrypt.checkpw(  bytes(request.form['pword'],  'utf-8' )  , bytes(item[0], 'utf-8') ))  
    return "User Added"

@app.route('/getBooks', methods=['GET']) #endpoint
def getBooks():

    cur = global_db_con.cursor()

    cur.execute("select title, price from book") 

    return json_response(bookList=cur.fetchall())
=======

@app.route('/auth2') #endpoint
def auth2():
    jwt_str = jwt.encode({"username" : "Ryan", "age" : "twenty-three"}, JWT_SECRET, algorithm="HS256")
    #print(request.form['username'])
    return json_response(jwt=jwt_str)


@app.route('/exposejwt') #endpoint
def exposejwt():
    jwt_token = request.args.get('jwt')
    return json_response(output = jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"]))


@app.route('/hellodb') #endpoint
def hellodb():
    cur = global_db_con.cursor()
    cur.execute("select 5+5, 1+1")
    first, second = cur.fetchone()
    return json_response(a=first, b=second)
>>>>>>> 1e808fdf2545ee096a12772117dff75fdd0c0aaf

app.run(host='0.0.0.0', port=80)

