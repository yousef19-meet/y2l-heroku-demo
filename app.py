
from flask import Flask, flash, render_template, url_for, redirect, request
from flask import session as login_session
from flask_session import *
import requests,json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('temre_bday.html')

if __name__ == '__main__':
    app.run(debug=True)

