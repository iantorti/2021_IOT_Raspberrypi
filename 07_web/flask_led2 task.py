from flask import Flask, render_template
from werkzeug.utils import redirect
import RPi.GPIO as GPIO

BLUE_LED_PIN = 19
RED_LED_PIN = 6

# Flask 객체 생성
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)
GPIO.setup(RED_LED_PIN, GPIO.OUT)

# 0.0.0.0:5000/
@app.route("/")
def home():
    return render_template("led2.html")
@app.route("/led/<op1>/<op2>")

def led_op(op1, op2):
    if op1 == "BLUE": 
        if op2 == "on":
            GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
            return "BLUE LED ON"

        elif op2 == "off":
            GPIO.output(BLUE_LED_PIN, GPIO.LOW)
            return "BLUE LED OFF"
        else:
            return "Error"
    elif op1 == "RED":
        if op2 == "on":
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            return "RED LED ON"

        elif op2 == "off":
            GPIO.output(RED_LED_PIN, GPIO.LOW)
            return "RED LED OFF"
        else:
            return "Error"
# @app.route("/led/on")
# def on():
#     return '''
#     <p>LED ON</p>
#     <a href="/">Go home</a>'''

# @app.route("/led/off")
# def off():
#     return '''
#     <p>LED OFF</p>
#     <a href="/">Go home</a>'''
# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    try:
        app.run(host = "0.0.0.0")
    finally:
        GPIO.cleanup()