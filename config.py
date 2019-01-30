#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 11:04
@author : Kay Lee
@file   : config.py 
@email  : wolflikai@163.com
@detail : None
'''


SECRET_KEY = 'stringtohardguess'
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/chat_flask'
HOST = '127.0.0.1'
PORT = 5000