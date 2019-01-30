#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 10:51
@author : Kay Lee
@file   : model.py 
@email  : wolflikai@163.com
@detail : None
'''
import datetime
import hashlib

from flask_login.mixins import UserMixin
from app import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    nickname = db.Column(db.String(30))
    password_hash = db.Column(db.String(128))
    github = db.Column(db.String(256))
    website = db.Column(db.String(256))
    bio = db.Column(db.String(256))
    messages = db.relationship('Message', backref='author', cascade='all')
    email_hash = db.Column(db.String(32))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.generate_email_hash()


    def generate_email_hash(self):
        if self.email and not self.email_hash:
            self.email_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()

    @property
    def gravatar(self):
        return 'https://gravatar.com/avatar/%s?d=monsterid&size=200' % self.email_hash



class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login_manager.user_loader
def load_user(userid):
    return User.get(userid)
