import boot
import os
from flask import Flask, session, g, redirect, url_for, abort, render_template, flash, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.form == "POST":
        print("lol")
        # boot.boot(strip, Color(0, 0, 0, 255), 0)
    return(render_template("main.html"))


# export FLASK_APP=flaskr
# export FLASK_DEBUG=true
# flask run

