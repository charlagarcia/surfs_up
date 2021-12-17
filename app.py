from flask import Flask

app3 = Flask(__name__)

@app3.route('/')
def hello_world():
    return 'Hello world'