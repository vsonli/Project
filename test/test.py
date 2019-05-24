# -*- coding:utf-8 -*-
# @Time   :2019/5/17 12:26
# @File   :test.py
# @Author :Vsonli
from flask import Flask
import flask_restful
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
'''
以上是python2的写法，但是在python3中这个需要已经不存在了，这么做也不会什么实际意义。 
在Python2.x中由于str和byte之间没有明显区别，经常要依赖于defaultencoding来做转换。 
在python3中有了明确的str和byte类型区别，从一种类型转换成另一种类型要显式指定encoding。
'''

import importlib,sys
importlib.reload(sys)


#http://localhost:5000/   可以访问
app = Flask(__name__)
api = flask_restful.Api(app)

class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
