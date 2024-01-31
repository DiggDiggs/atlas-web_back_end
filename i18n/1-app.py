#!/usr/bin/env python3
"""
Basic babel flask app very useful.

Babel's default local <en>
and timezone <UTC>

class as config for flask app.
"""
from flask import Flask, render_template, request
from flask_babel import Babel