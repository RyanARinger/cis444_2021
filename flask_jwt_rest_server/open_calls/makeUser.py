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

def handle_request():
    cur = global_db_con.cursor()

    salted = bcrypt.hashpw( bytes(request.form['pword'],  'utf-8' ) , bcrypt.gensalt(12))
    username = request.form['uname']
    cur.execute("insert into users (username, password) values ('{}','{}')".format(username, salted.decode("utf-8")))

    global_db_con.commit()

    cur.execute("select password from users where username = '{}'".format(username))
    #for item in cur.fetchall():
        #print(item[0])
        #print(  bcrypt.checkpw(  bytes(request.form['pword'],  'utf-8' )  , bytes(item[0], 'utf-8') ))
    return "User Added"
