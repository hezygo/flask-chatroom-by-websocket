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
from app.bp import chat
from app.extensions import db, moment, login_manager, socketio, csrf



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    _create_db_table(app)
    _register_extension(app)
    _register_blueprint(app)
    return app


def _register_extension(app):
    db.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)
    socketio.init_app(app)

def _create_db_table(app):
    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)

def _register_blueprint(app):
    from app.bp import chat
    app.register_blueprint(chat)
