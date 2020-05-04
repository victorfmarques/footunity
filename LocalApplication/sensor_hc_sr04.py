import RPi.GPIO as GPIO
import time
import helper as lib_helper


class hc_sr04(object):
    __trigger_pin = 0
    __echo_pin = 0
    __number_of_measures = 5

    def __init__(self, trigger_pin, echo_pin):

        self.__trigger_pin = trigger_pin
        self.__echo_pin = echo_pin

        # Setting trigger and echo pins
        # GPIO.setup(self.__trigger_pin, GPIO.OUT)
        # GPIO.setup(self.__echo_pin, GPIO.IN)

    def get_distance_cm(self):
        # Setting local variables
        start = 0
        end = 0
        sig_time = 0
        distance = 0
        measure_number = 0

    	# Setting GPIO mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__trigger_pin, GPIO.OUT)
        GPIO.setup(self.__echo_pin, GPIO.IN)

        try:
            for measure_number in range(self.__number_of_measures):
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
                #  speed_of_sound = lib_helper.get_speed_of_sound()
                # distance = sig_time * (speed_of_sound / 2)
                distance += sig_time * 17150

        except Exception as e:
            # Handling exception
            print(str(e))

        finally:
            # Clean GPIO pins
            GPIO.cleanup()
	print(str(measure_number))

        return distance / measure_number
