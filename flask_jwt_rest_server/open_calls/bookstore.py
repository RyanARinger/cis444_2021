from flask import Flask,render_template,request, redirect, url_for, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt

def handle_request():
    return render_template('login_buy_confirm.html', img_url="/static")
