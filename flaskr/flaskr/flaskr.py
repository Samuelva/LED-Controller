import os
from flask import Flask, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

@app.route("/")
def main():
    return(render_template("main.html"))
