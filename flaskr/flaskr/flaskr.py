import subprocess
import os
from flask import Flask, session, g, redirect, url_for, abort, render_template, flash, request, jsonify

app = Flask(__name__)
ledStatus = "Uit"

@app.route('/boot')
def boot():
    if ledStatus == "Uit":
        ledStatus = "Aan"
        return jsonify(status="Aan", buttonLabel="Uit")
    else:
        ledStatus = "Uit"
        return jsonify(status="Uit", buttonLabel="Aan")


@app.route("/")
def main():
    return(render_template("main.html"))


# export FLASK_APP=flaskr
# export FLASK_DEBUG=true
# flask run

# sudo PYTHONPATH=".:build/lib.linux-arm7l-2.7" python/examples/test2.py