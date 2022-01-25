# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask.globals import request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.php')


# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello():
#     return "Hello world!"

