import os

from flask import render_template, request, json, url_for, flash, redirect, jsonify
from werkzeug.utils import secure_filename
from . import app, db, forms, basic_auth,api, login_manager, paynow
from .security import authenticate, identity
from flask_login import current_user
from .models import *
from .models import User
from .oauth import *
from rauth import OAuth2Service
from .resources.user import UserRegister
from .helper_functions import ServerResponse, allowed_file
from flask_restful import Resource, Api
from paynow import Paynow
from flask_jwt import JWT

jwt = JWT(app, authenticate, identity)





@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('home'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email= oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    print("=============== Social ID=================", social_id, username, email)
    user = User.get_by_social_id(social_id)
    if user:
        print("========================= User =============", user)
        return redirect(url_for('home'))
    # def signup():
    else: 
    
        user = User(social_id=social_id, username=username, email=email)
        user.save()       
        print("========================= User =============", user)
        return redirect(url_for('home'))
    
   

@app.route('/pay', methods=['POST', 'GET'])
def pay():
    phone_number = request.form.get('phone_number')
   
    print("Phone Number", phone_number)
    payment = paynow.create_payment('Order', 'test@example.com')
    payment.add('Payment for stuff', '1')
    response = paynow.send_mobile(payment, phone_number, 'ecocash') 
    if(response.success):
        poll_url = response.poll_url        
        status = paynow.check_transaction_status(poll_url)        
        created = status.status
        if(status == 'created' ):
            print("Created")
        print("Payment Status: ", created)
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
    
    