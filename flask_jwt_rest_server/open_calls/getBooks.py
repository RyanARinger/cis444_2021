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

    cur.execute("select title, price from book")

    return json_response(bookList=cur.fetchall())
