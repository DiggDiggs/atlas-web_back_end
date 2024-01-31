#!/usr/bin/env python3
"""
Basic babel flask app.

Uses Config to set Babel's default local <en>
and timezone <UTC>

Uses that class as config for flask app.

Uses gettext to parameterize templates using message IDS
'home_title' and 'home_header'.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext