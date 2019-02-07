from . import admin

from flask import render_template

@admin.route('/', methods=["GET", "POST"])
def login():
    return render_template('admin/login.html')

@admin.route('/home', methods=["GET", "POST"])
def home():
    return render_template('admin/index.html')