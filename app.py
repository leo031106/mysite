
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Welcome to the Home Page!"