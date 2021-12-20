from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 6
LED_PIN_BLUE = 19
# Flask 객체 생성
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN_BLUE, GPIO.OUT)

# 0.0.0.0:5000/
@app.route("/")
def hello():
    return '''
    <p>Hello, Flask!!</p>
    <a href = "/led/red/on">RED LED ON  </a>
    <hr>
    <a href = "/led/red/off">RED LED OFF  </a>
    <hr>
    <a href = "/led/blue/on">BLUE LED ON  </a>
    <hr>
    <a href = "/led/blue/off">BLUE LED OFF  </a>
    '''
@app.route("/led/<color>/<op>")
def led_op(color,op):
    if color == "red":
        if op == "on":
            GPIO.output(LED_PIN, GPIO.HIGH)
            return '''
            <p>RED LED ON</p>
            <a href="/">Go back home</a>'''    
        elif op == "off":
            GPIO.output(LED_PIN, GPIO.LOW)
            return '''
            <p>RED LED OFF</p>
            <a href="/">Go back home</a>'''
    elif color == "blue":
        if op == "on":
            GPIO.output(LED_PIN_BLUE, GPIO.HIGH)
            return '''
            <p>BLUE LED ON</p>
            <a href="/">Go back home</a>'''    
        elif op == "off":
            GPIO.output(LED_PIN_BLUE, GPIO.LOW)
            return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go back home</a>'''

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