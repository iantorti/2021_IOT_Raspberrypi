from lcd import drivers
import datetime
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4


display = drivers.Lcd()

try:
    while True:
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"),1)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if humidity is not None and temperature is not None:
            display.lcd_display_string(f"{temperature:.1f}C,{humidity:.1f}%",2)
finally:
    display.lcd_clear() 



                       