from LedControl import LedControl
from neopixel import Color
from flask import Flask, session, g, redirect, url_for, abort, render_template, flash, request, jsonify

app = Flask(__name__)
led = LedControl()

@app.route('/boot')
def boot():
    if led.getStatus() == "Off":
        led.setStatus("On")
        led.boot(Color(0, 0, 0, 255))
        return jsonify(status="Aan", buttonLabel="Uit")
    elif led.getStatus() == "On":
        led.setStatus("Off")
        led.shutdown()
        return jsonify(status="Uit", buttonLabel="Aan")


@app.route("/")
def main():
    return(render_template("main.html"))


# export FLASK_APP=flaskr
# export FLASK_DEBUG=true
# flask run

# sudo PYTHONPATH=".:build/lib.linux-arm7l-2.7" python/examples/test2.py
