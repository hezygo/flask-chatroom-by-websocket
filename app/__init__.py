#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 10:51
@author : Kay Lee
@file   : __init__.py 
@email  : wolflikai@163.com
@detail : None
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login.login_manager import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    login_manager.init_app(app)
    return app




