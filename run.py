#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019/1/30 11:40
@author : Kay Lee
@file   : run.py 
@email  : wolflikai@163.com
@detail : None
'''
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])