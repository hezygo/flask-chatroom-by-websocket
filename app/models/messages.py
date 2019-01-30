#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 14:37
@author : Kay Lee
@file   : messages.py 
@email  : wolflikai@163.com
@detail : None
'''
from app.extensions import db
import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))