# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:03:51 2020

@author: Sankhasubhra Mandal
"""


from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()