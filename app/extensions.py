#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 14:56
@author : Kay Lee
@file   : extensions.py 
@email  : wolflikai@163.com
@detail : None
'''
from flask_socketio import SocketIO
from flask_moment import Moment
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO()
moment = Moment()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(userid):
    from app.models.users import User
    return User.query.get(int(userid))

login_manager.login_view = 'chat.signin'
