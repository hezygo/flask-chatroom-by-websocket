#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 11:47
@author : Kay Lee
@file   : migrate.py 
@email  : wolflikai@163.com
@detail : None
'''

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from run import app
from app import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
