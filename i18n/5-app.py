#!/usr/bin/env python3
"""
Basic babel flask app.

Uses Config to set Babel's default local <en>
and timezone <UTC>

Uses that class as config for flask app.
"""
from flask import Flask, request, g
from flask_babel import Babel
from flask_babel import gettext as _
from flask.templating import render_template