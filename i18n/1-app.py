#!/usr/bin/env python3
"""
Basic babel flask app very useful.

Babel's default local <en>
and timezone <UTC>

class as config for flask app.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    Configure Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'