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

@app.route('/web_auth', methods=['POST', 'GET'])
def web():
    data = request.get_json()
    username =data['username']
    password =data['password']  
     
    user = User.get_by_username(username)
    print(username)
    print(password)
    if user is not None and user.check_password(password):
        print(user.id)
        return  jsonify( id=user.id )

    else : 
        print("incorrect Password or email")
        return  jsonify( id=0)




@app.route('/home', methods=['GET', 'POST'])
def home():   
    gid = request.args.get('id')       
    print(gid)
    course_schema = CourseSchema(many=True)
    words_schema = AlphabetSchema(many=True)
    phrase_schema = PhraseSchema(many=True)
    courses = course_schema.dump(Course.query.all()).data
    words = words_schema.dump(Alphabet.query.all()).data
    phrases = phrase_schema.dump(Phrases.query.all()).data
    print(phrases)
    return render_template('user.html', courses=courses, words=words, phrases=phrases)
    
    


@app.route('/admin/save_course', methods=['GET', 'POST'])
def save():
    course_name = request.form['course_name']
    new_course = Course(name=course_name)
    new_course.save()
    return render_template('login-5.html')


@app.route('/get_courses')
def courses():
    courses_schema = CourseSchema(many=True)
    result = courses_schema.dump(Course.get_all()).data
    print(Course.get_all())
    return jsonify(result)


@app.route('/admin/upload_content', methods=['GET', 'POST'])
@basic_auth.required
def upload_content():
    if request.method == 'POST':
        section_name = request.form['section_name']
        course_id = request.form['course_id']

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_section = Section(
                course_id=course_id, section_name=section_name, file_name=filename)
            new_section.save()
            flash('Content successfully added!')
            return render_template('add_content.html')
    else:
        return render_template('add_content.html')


@app.route('/admin/upload_alphabet', methods=['GET', 'POST'])
def upload_alphabet():
    if request.method == 'POST':
        word = request.form['word']

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_phrase = Content(
                name=word, file_name=filename)
            new_phrase.save()
            flash('Content successfully added!')
            return render_template('add_content.html')
    else:
        return render_template('add_content.html')
