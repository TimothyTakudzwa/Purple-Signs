import os

from flask import (flash, json, jsonify, redirect, render_template, request,
                   url_for)
from flask_jwt import JWT
from flask_login import current_user
from flask_restful import Api, Resource
from paynow import Paynow
from rauth import OAuth2Service
from werkzeug.utils import secure_filename
import time 
from . import api, app, basic_auth, db, forms, login_manager, paynow
from .helper_functions import ServerResponse, allowed_file
from .models import *
from .models import User
from .oauth import *
from .resources.user import UserRegister
from .security import authenticate, identity

jwt = JWT(app, authenticate, identity)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



@app.route('/pay', methods=['POST', 'GET'])
def pay():
    data = request.get_json()   
    phone_number = data['phone_number']
    user_id = data['id']   
    payment = paynow.create_payment('Subscription Payment', 'admin@purplesigns.co.zw')
    payment.add('Payment for stuff', 1)
    response = paynow.send_mobile(payment, phone_number, 'ecocash')

    if(response.success):
        poll_url = response.poll_url          
        time.sleep(30)   
        status = paynow.check_transaction_status(poll_url)             
        if (status.status=='paid'):
            paid=False
            update_payment_status(user_id, paid, poll_url, status.status)
        if (status.status=='sent'):
            paid=False
            update_payment_status(user_id, paid, poll_url , status.status)
        return jsonify({'status':status.status }), 200
    return jsonify({'status':0 }), 400

@app.route('/check_transaction', methods=['POST', 'GET'])
def check():
    data = request.get_json()
    user_id = data['id']  
    try:
        user = Billing.get_by_id(user_id)
        print("User: ", user.poll_url)
        poll_url = user.poll_url
        status = paynow.check_transaction_status(poll_url)             
        if (status.status=='paid'):
            paid = True
            User.update_payment(user_id, paid)
            billing = Billing(user_id=user_id,poll_url=poll_url,amount=1, status=status.status)
            billing.save()       
        return jsonify({'status':status.status }), 200 
    except:
        return jsonify({'status':0 }), 200


@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/login')
def login():
    print("------------------------", current_user)
    return render_template('login-5.html')

@app.route('/get_users')
def users():
    user_schema = UserSchema(many=True)
    users = user_schema.dump(Billing.query.all()).data    
    return  jsonify(users)



@app.route('/update_payment')
def payment():
    data = request.get_json()
    user_id = data['id']  
    paid = data['paid']  
    User.update_payment(user_id, paid)
    return  ''

@app.route('/home', methods=['GET', 'POST'])
def home():   
    course_schema = CourseSchema(many=True)
    words_schema = AlphabetSchema(many=True)
    class_schema = ClassSchema(many=True)
    phrase_schema = PhraseSchema(many=True)
    classes = class_schema.dump(Classes.query.all()).data
    courses = course_schema.dump(Course.query.all()).data
    words = words_schema.dump(Alphabet.query.all()).data
    phrases = phrase_schema.dump(Phrases.query.all()).data
   
    return render_template('user.html', courses=courses, words=words, phrases=phrases, classes=classes)

def update_payment_status(user_id, paid, poll_url, status):    
    User.update_payment(user_id, paid)
    user = Billing.get_by_id(user_id)
    if user is None:
        billing = Billing(user_id=user_id,poll_url=poll_url,amount=1,status=status)
        billing.save() 
    else: 
        Billing.update_payment(user_id, poll_url)        