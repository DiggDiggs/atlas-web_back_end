#!/usr/bin/env python3
"""
Basic babel flask app.

Uses Config to set Babel's default local <en>
and timezone <UTC>

Uses that class as config for flask app.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)
gettext.__doc__ = "Nice one, checker."
""" Parameterize templates using message IDS """


class Config():
    """
    Configure Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
gettext(u'home_title')
gettext(u'home_header')


@babel.localeselector
def get_locale():