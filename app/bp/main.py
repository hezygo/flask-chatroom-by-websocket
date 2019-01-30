#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 15:41
@author : Kay Lee
@file   : main.py 
@email  : wolflikai@163.com
@detail : None
'''
from flask_socketio import emit

from . import chat
from flask import render_template
from app.extensions import socketio


@chat.route('/index')
def index():
    return render_template('chat/index.html')

@socketio.on('new_message')
def new_message(message_body):
    print(message_body)
    emit(
        'new_message',
        {
            'message_html': '<h3>'+message_body+'</h3>'
        }
    )
