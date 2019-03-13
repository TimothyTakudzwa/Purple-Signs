import os

from flask import (flash, json, jsonify, redirect, render_template, request,
                   url_for)
from flask_jwt import JWT
from flask_login import current_user
from flask_restful import Api, Resource
from paynow import Paynow
from rauth import OAuth2Service
from werkzeug.utils import secure_filename

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
   
    payment = paynow.create_payment('Order', 'test@example.com')

    payment.add('Payment for stuff', 1)

    response = paynow.send_mobile(payment, '0774231343', 'ecocash')

    print("Payment Status: ", response.status.error)
    if(response.success):
        poll_url = response.poll_url

        print("Poll Url: ", poll_url)

        status = paynow.check_transaction_status(poll_url)

        time.sleep(30)

        print("Payment Status: ", status.status)
    return ''

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/login')
def login():
    print("------------------------", current_user)
    return render_template('login-5.html')



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
