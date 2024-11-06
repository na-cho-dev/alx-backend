#!/usr/bin/env python3
"""
Setup a basic Flask app in 4-app.py
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)


class Config(object):
    """
    Config class for Babel’s default locale ("en")
    and timezone ("UTC").
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale():
    """
    Determine the best match with our supported languages.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Returns the render of 4-index.html
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
