import spidev
import time
import RPi.GPIO as GPIO


led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

spi = spidev.SpiDev()

spi.open(0, 0)

spi.max_speed_hz = 1000000


# 0~7까지 채널에서 SPI 데이터 읽기
def analog_read(channel):
  # [byte_1, byte_2, byte_3]
  # byte_1 : 1
  # byte_2 : channel(0) + 8 -> 0000 1000 << 4 -> 1000 0000
  # byte_3 : 0
  ret = spi.xfer2([1, (channel + 8) << 4, 0])
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out

try:
    while True:
        ldr_value = analog_read(0)
        print("LDR Value: %d" % ldr_value)
        if(ldr_value<600):
            GPIO.output(led_pin, GPIO.HIGH)
            print("led on")
        elif(ldr_value>600):
            GPIO.output(led_pin, GPIO.LOW)
            print("led off")
        time.sleep(0.5)
finally:
    spi.close()