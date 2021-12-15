from flask import Flask,render_template,request,jsonify
from flask import Flask,render_template,request,send_from_directory
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt

import jwt

import datetime
import bcrypt

import json

from db_con import get_db_instance, get_db

from db_con import get_db_instance, get_db

global_db_con = get_db()

JWT_SECRET = ""

def handle_request():
    cur = global_db_con.cursor()
    username = request.form['uname']
    print(username)
    validUser = False
    isLind = "False" #I promised my friend a birthday message

    cur.execute("select password from users where username = '{}'".format(username))
    for item in cur.fetchall():
        if bcrypt.checkpw(  bytes(request.form['pword'],'utf-8' )  , bytes(item[0], 'utf-8')):
            validUser = True

    if validUser:
        if username == "Lindsey":
            isLind = "True"
            #print(isLind)
        jwt_str = jwt.encode({"username" : username}, JWT_SECRET, algorithm="HS256")
        return json_response(jwt=jwt_str, lind=isLind)
    else:
        return json_response(jwt='BadRequest')
