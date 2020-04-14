import RPi.GPIO as GPIO
import sensor_hy_srf05

GPIO.setmode(GPIO.BCM)

sensor = sensor_hy_srf05.SRF05(trigger_pin = 23, echo_pin = 25)
while True:
    print(sensor.measure())