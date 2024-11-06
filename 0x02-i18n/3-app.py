#!/usr/bin/env python3
"""
Setup a basic Flask app in 3-app.py
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def index() -> str:
    """
    Returns the render of 3-index.html
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000)
