import RPi.GPIO as GPIO

class LedBicolor(object):

    def __init__(self, _red_pin, _blue_pin):
        self.red_pin = _red_pin
        self.blue_pin = _blue_pin

    def light_led(self, _red_on=0, _blue_on=0 ):
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)

        try:
            GPIO.output(self.red_pin , _red_on )
            GPIO.output(self.blue_pin, _blue_on)
        except:
            GPIO.cleanup()
