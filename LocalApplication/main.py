import RPi.GPIO as GPIO
import sensor_hy_srf05

GPIO.setmode(GPIO.BCM)

sensor = sensor_hy_srf05.SRF05(trigger_pin = 14, echo_pin = 15)
while True:
    print(sensor.measure())