import Adafruit_DHT
import time


class dht11(object):

    def __init__(self, pin):
        self.__pin = pin

    def get_temperature(self):

        dht_sensor = Adafruit_DHT.DHT11
        print(str(self.__pin))
        humidity, temperature = Adafruit_DHT.read(dht_sensor, self.__pin)
        if temperature is not None:
            return temperature
        else:
            print("Temperature None")
            return None
