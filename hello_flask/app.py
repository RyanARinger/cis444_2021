from flask import Flask,render_template,request,send_from_directory
from flask_json import FlaskJSON, JsonError, json_response, as_json

import jwt

import datetime


app = Flask(__name__)
FlaskJSON(app)

USER_PASSWORDS = { "cjardin": "strong password"}

IMGS_URL = {
            "DEV" : "/static",
            "INT" : "https://cis-444-fall-2021.s3.us-west-2.amazonaws.com/images",
            "PRD" : "http://d2cbuxq67vowa3.cloudfront.net/images"
            }

CUR_ENV = "DEV"

JWT_SECRET = None
with open("mysecret", "r") as f:
    JWT_SECRET = f.read()

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
    return render_template('backatu.html',input_from_browser= str(request.form) )

@app.route('/auth',  methods=['POST']) #endpoint
def auth():
        #print(request.form['username'])
        return json_response(data=request.form)



#Assigment 2
@app.route('/ss1') #endpoint
def ss1():
    return render_template('server_time.html', server_time= str(datetime.datetime.now()), img_url=IMGS_URL[CUR_ENV] )
    #return render_template('server_time.html', img_url=IMGS_URL[CUR_ENV] )

@app.route('/getTime') #endpoint
def get_time():
    return json_response(data={"password" : request.args.get('password'),
                                "class" : "cis44",
                                "serverTime":str(datetime.datetime.now())})

@app.route('/getClientTime') #endpoint
def get_client_time():
    return render_template('client_time.html', img_url=IMGS_URL[CUR_ENV])


@app.route('/easy') #endpoint
def twe():
    return render_template('thatWasEasy.html', img_url=IMGS_URL[CUR_ENV])



@app.route('/auth2') #endpoint
def auth2():
    jwt_str = jwt.encode({"username" : "Ryan", "age" : "twenty-three"}, JWT_SECRET, algorithm="HS256")
    #print(request.form['username'])
    return json_response(jwt=jwt_str)


@app.route('/exposejwt') #endpoint
def exposejwt():
    jwt_token = request.args.get('jwt')
    return json_response(output = jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"]))



app.run(host='0.0.0.0', port=80)

