#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return '<h1>Hola mundo</h1><p>Desde Flask</p>'
