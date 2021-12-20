import RPi.GPIO as GPIO

red = 4
yellow = 17
green = 22
SWITCH1 = 26
SWITCH2 = 19
SWITCH3 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(SWITCH1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        val1 = GPIO.input(SWITCH1)
        print(val1)
        GPIO.output(red, val1)
        val2 = GPIO.input(SWITCH2)
        print(val2)
        GPIO.output(yellow, val2)
        val3 = GPIO.input(SWITCH3)
        print(val3)
        GPIO.output(green, val3)
finally:
    GPIO.cleanup()
    print('cleanup and exit')