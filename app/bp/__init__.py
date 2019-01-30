#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 14:02
@author : Kay Lee
@file   : __init__.py 
@email  : wolflikai@163.com
@detail : None
'''
from flask import Blueprint

chat = Blueprint('chat', __name__)

from . import auth
from . import main