#!/usr/bin/env python3
"""
Setup a basic Flask app in 2-app.py
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class for Babel’s default locale ("en")
    and timezone ("UTC").
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """
    Determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.locale_selector_func = get_locale


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Returns the render of 2-index.html
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000)
