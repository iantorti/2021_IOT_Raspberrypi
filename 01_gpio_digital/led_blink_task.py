import RPi.GPIO as GPIO
import time

LED_PIN_red = 4
GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN_red, GPIO.OUT) # GPIO.OUT OR GPIO.IN

LED_PIN_yellow= 17
GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN_yellow, GPIO.OUT) # GPIO.OUT OR GPIO.IN

LED_PIN_green = 27
GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN_green, GPIO.OUT) # GPIO.OUT OR GPIO.IN

for i in range(10):
    GPIO.output(LED_PIN_red, GPIO.HIGH) # 1, True
    print("led on")
    time.sleep(2) # 1초 유지
    GPIO.output(LED_PIN_red, GPIO.LOW)
    print("led off")
    time.sleep(1)
    GPIO.output(LED_PIN_yellow, GPIO.HIGH) # 1, True
    print("led on")
    time.sleep(2) # 1초 유지
    GPIO.output(LED_PIN_yellow, GPIO.LOW)
    print("led off")
    time.sleep(1)
    GPIO.output(LED_PIN_green, GPIO.HIGH) # 1, True
    print("led on")
    time.sleep(2) # 1초 유지
    GPIO.output(LED_PIN_green, GPIO.LOW)
    print("led off")
    time.sleep(1)