#!/usr/bin/python3
"""Module to start a flask app"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """Function to print hello"""
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """Function to print HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def variables(text):
    """Function to display text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/")
@app.route("/python/<text>")
def python_variable(text="is cool"):
    """Function to print more text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
