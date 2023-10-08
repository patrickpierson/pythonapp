from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/json')
def json_hw():
    data = {"name": "John Doe", "age": 30}
    return jsonify(data)
