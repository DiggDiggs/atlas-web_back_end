#!/usr/bin/env python3
"""
 babel flask app.

"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():