#!/usr/bin/env python3
"""
Setup a basic Flask app in 1-app.py
"""
from flask import Flask, render_template
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


@app.route('/', methods=['GET'])
def home():
    """Returns the render of 1-index.html"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000)
