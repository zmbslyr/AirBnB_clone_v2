#!/usr/bin/python3
"""Module to start a flask app"""
from flask import Flask, render_template

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


@app.route("/number/<int:n>")
def number_variable(n):
    """Prints number if it is an int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def html_variable(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_even(n):
    """Finds if a number is odd or even"""
    if n % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
    return render_template(
        "6-number_odd_or_even.html", n=n, even_or_odd=odd_even)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
