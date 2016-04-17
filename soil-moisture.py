from time import sleep
import RPi.GPIO as GPIO
from pi_sht1x import SHT1x

# With BCM the pin numbering should match the GPIO header.
#gpio_mode = GPIO.BOARD
gpio_mode = GPIO.BCM

data_pin = 17
clock_pin = 14

with SHT1x(data_pin, clock_pin, gpio_mode=gpio_mode) as sensor:
    temp = sensor.read_temperature()
    humidity = sensor.read_humidity(temp)
    sensor.calculate_dew_point(temp, humidity)
    print(sensor)
