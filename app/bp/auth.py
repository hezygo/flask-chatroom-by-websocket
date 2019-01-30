#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 14:05
@author : Kay Lee
@file   : auth.py 
@email  : wolflikai@163.com
@detail : None
'''

from flask import render_template, request
from . import chat
from app.extensions import db
from app.models.users import User

@chat.route('/signUp', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('passwd1')
        password2 = request.form.get('passwd2')
        print(email, nickname, password1, password2)
        try:
            user = User(
                nickname=nickname,
                email=email,
                password=password1,
            )
            db.session.add(user)
            db.session.commit()
        except Exception as err:
            db.session.rollback()
            raise err
    return render_template('auth/register.html')

@chat.route('/signIn')
def signin():
    return render_template('auth/login.html')

