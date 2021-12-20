import RPi.GPIO as GPIO

LED_PIN = 17
SWITCH_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
# 누르지 않았을 떄 0, 눌렀을 떄 : 2
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN, val)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
    