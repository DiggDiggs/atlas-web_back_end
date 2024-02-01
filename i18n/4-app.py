#!/usr/bin/env python3
"""
Basic Babel Flask app.

Uses Babel's Config to set the default locale to <en> and timezone to <UTC>.

Uses the Babel class as config for the Flask app.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)
gettext.__doc__ = "Nice one, checker."
""" Parameterize templates using message IDs """


class BabelConfig():
    """
    Configure Babel for the Flask app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(BabelConfig)


@babel.localeselector
def get_locale():
    """
    Get locale from the request.

    Detects if the incoming request contains the <locale>
    is a supported locale, returns it.
    present, resort to the default locale.
    """
    locale = request.args.get('locale')
    if locale and locale in BabelConfig.LANGUAGES:
        return locale
    return request.accept_languages.best_match(BabelConfig.LANGUAGES)


@app.route('/')
def index():
    """
    Return the index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
