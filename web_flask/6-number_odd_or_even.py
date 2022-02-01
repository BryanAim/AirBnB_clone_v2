#!/usr/bin/python3
"""
A python script that starts a Flask web application
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """index page"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route"""
    return("HBNB")


@app.route('/c/<text>/', strict_slashes=False)
def c(text):
    """c route"""
    return("C {}".format(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>/', strict_slashes=False)
def python(text="is cool"):
    """python route"""
    if text != "is cool":
        new_text = text.replace("_", " ")
        return("Python {}".format(new_text))
    return("Python {}".format(text))


@app.route('/number/<int:n>/', strict_slashes=False)
def number(n):
    """number route"""
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>/', strict_slashes=False)
def number_template(n=None):
    """number_template route"""
    return(render_template("5-number.html", n=n))


@app.route('/number_odd_or_even/<int:n>/', strict_slashes=False)
def odd_or_even(n=None):
    """number_odd_or_even route"""
    return(render_template("6-number_odd_or_even.html", n=n))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
