import RPi.GPIO as GPIO
import time

# GPIO pin with the red wire for the powerswitch tail II.
relay_pin = 5

# Water for 10 seconds.
water_time = 10

# Alternative pin numbering setup.
#GPIO.setmode(GPIO.BOARD)
# Pins numbering matches the Pi cobbler.
GPIO.setmode(GPIO.BCM)


GPIO.setup(relay_pin, GPIO.OUT)
print("Water on")
GPIO.output(relay_pin, GPIO.HIGH)
time.sleep(water_time)
print("Water off")
GPIO.output(relay_pin, GPIO.LOW)
print("Done")
