from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 6
# Flask 객체 생성
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# 0.0.0.0:5000/
@app.route("/")
def hello():
    return '''
    <p>Hello, Flask!!</p>
    <a href = "/led/on">LED ON  </a>
    <a href = "/led/off">LED OFF  </a>
    '''
@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
        <p>LED ON</p>
        <a href="/">Go back home</a>'''    
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
        <p>LED OFF</p>
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