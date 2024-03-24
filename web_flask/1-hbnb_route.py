#!/usr/bin/python3
"""Start a web app"""

from flask import Flask

app = Flask(__name__)

# define the route
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display hello world """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """diplay HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)