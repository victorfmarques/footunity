import RPi.GPIO as GPIO
import sensor_hy_srf05

GPIO.setmode(GPIO.BCM)

sensor = sensor_hy_srf05.SRF05(trigger_pin = 8, echo_pin = 10)
while True:
    print(sensor.measure())