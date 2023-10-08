"""Module providing an example python app."""
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Function returning hello world."""
    return 'Hello, World!'

@app.route('/json')
def json_hw():
    """Function returning json data."""
    data = {"name": "John Doe", "age": 30}
    return jsonify(data)
