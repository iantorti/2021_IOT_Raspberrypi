import RPi.GPIO as GPIO
import time

LED_PIN = 6
GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN, GPIO.OUT) # GPIO.OUT OR GPIO.IN

for i in range(100):
    GPIO.output(LED_PIN, GPIO.HIGH) # 1, True
    print("led on")
    time.sleep(0.1) # 1초 유지
    GPIO.output(LED_PIN, GPIO.LOW)
    print("led off")
    time.sleep(0.1)
