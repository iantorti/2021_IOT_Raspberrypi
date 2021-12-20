import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if humidity is not None and temperature is not None:
            print(f"Temperature={temperature:.1f}C, Humidity:{humidity:.1f}%")
        else:
            print('Read Error')
finally:
    print("bye")    