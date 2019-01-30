#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 10:51
@author : Kay Lee
@file   : model.py 
@email  : wolflikai@163.com
@detail : None
'''

import hashlib
from flask_login.mixins import UserMixin
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.messages import Message


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    nickname = db.Column(db.String(30))
    password_hash = db.Column(db.String(128))
    github = db.Column(db.String(256))
    website = db.Column(db.String(256))
    bio = db.Column(db.String(256))
    messages = db.relationship('Message', backref='author')
    email_hash = db.Column(db.String(32))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.generate_email_hash()

    def generate_email_hash(self):
        if self.email and not self.email_hash:
            self.email_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, raw):
        self.password_hash = generate_password_hash(raw)

    def check_password(self, raw):
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, raw)


    @property
    def gravatar(self):
        return 'https://gravatar.com/avatar/%s?d=monsterid&size=200' % self.email_hash



