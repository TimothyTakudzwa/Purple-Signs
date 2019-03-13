from . import auth
from ..import  api
from flask import render_template
from ..models import *
from ..resources.user import UserRegister, LoginRegister
from flask import render_template, request, json, url_for, flash, redirect, jsonify

api.add_resource(UserRegister, '/register')
api.add_resource(LoginRegister, '/login')

@auth.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login-5.html')

@auth.route('/web_auth', methods=['POST', 'GET'])
def web():
    data = request.get_json()
    username =data['username']
    password =data['password']  
     
    user = User.get_by_username(username)
    print(username)
    print(user)
    if user is not None and user.check_password(password):
        print(user.id)
        return  jsonify(id=user.id)
    else : 
        print("incorrect Password or email")
        return  jsonify(id=0)