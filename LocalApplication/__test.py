from led_bicolor import LedBicolor as bc

led = bc(_red_pin = 20, _blue_pin = 26)

led.light_led(_red_on=1, _blue_on= 0)
input("1 0")
led.light_led(_red_on=0, _blue_on= 1)
input("0 1")
led.light_led(_red_on=1, _blue_on= 1)
input("1 1")