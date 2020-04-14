import RPi.GPIO as GPIO
import time


class SRF05:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        self.trigger_time = 0

        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.setup(self.trigger_pin, GPIO.OUT)

    def measure(self):
        now = self.time_us()
        start = 0
        end = 0

        # "The SRF05 can be triggered as fast as every 50mS, or 20 times each second.
        # You should wait 50ms before the next trigger, even if the SRF05 detects a close object and the echo pulse is shorter.
        # This is to ensure the ultrasonic "beep" has faded away and will not cause a false echo on the next ranging."
        pause = 50000 - (now - self.trigger_time)
        if pause > 0:
            self.sleep_us(pause)

        self.trigger()

        self.trigger_time = self.time_us()

        while GPIO.input(self.trigger_pin) == 0:
            start = self.time_us()

        while GPIO.input(self.trigger_pin) == 1:
            end = self.time_us()

        width = end - start

        # ...and by that logic we should not have real measurement with pulse longer than 30ms anyway
        # "If the width of the pulse is measured in uS, then dividing by 58 will give you the distance in cm,
        # or dividing by 148 will give the distance in inches. uS/58=cm or uS/148=inches."
        return int(width / 58)

    def trigger(self):
        # "You only need to supply a short 10uS pulse to the trigger input to start the ranging."
        GPIO.output(self.trigger_pin, 1)
        self.sleep_us(10)
        GPIO.output(self.trigger_pin, 0)

    # Return time in microseconds
    def time_us(self):
        return int(time.time() * 1000000)

    def sleep_us(self, us):
        time.sleep(us / 1000000.0)