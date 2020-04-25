import RPi.GPIO as GPIO
import time
import helper as lib_helper


class hc_sr04(object):
    __trigger_pin = 0
    __echo_pin = 0

    def __init__(self, trigger_pin, echo_pin):
        # Choosing BCM setmode
        # GPIO.setmode(GPIO.BCM)
        self.__trigger_pin = trigger_pin
        self.__echo_pin = echo_pin

        print(str(self.__trigger_pin))

        # Setting trigger and echo pins
        # GPIO.setup(self.__trigger_pin, GPIO.OUT)
        # GPIO.setup(self.__echo_pin, GPIO.IN)

    def get_distance_cm(self):
        # Setting local variables
        start = 0
        end = 0
        sig_time = 0
        distance = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__trigger_pin, GPIO.OUT)
        GPIO.setup(self.__echo_pin, GPIO.IN)

        print("GPIO -> " + str(GPIO))
        print("get_distance " + str(self.__trigger_pin))

        try:
            # Forcing trigger pin to low
            GPIO.output(self.__trigger_pin, False)
            time.sleep(2)

            # Triggering a pulse
            GPIO.output(self.__trigger_pin, True)
            time.sleep(0.00001)
            GPIO.output(self.__trigger_pin, False)

            # Setting start time until the pulse is not captured back
            while not GPIO.input(self.__echo_pin):
                start = time.time()

            # Setting end time until the pulse is listened
            while GPIO.input(self.__echo_pin):
                end = time.time()

            # Calculating the pulse time
            sig_time = end - start
            dht11 = lib_dht11.dht11(4)

            distance = sig_time * (int(lib_helper.get_speed_of_sound()) / 2)

        except Exception as e:
            # Handling exception
            print(str(e))

        finally:
            # Clean GPIO pins
            GPIO.cleanup()

        return distance
