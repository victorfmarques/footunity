import sensor_hc_sr04 as lib_hc_sr04

sensor = lib_hc_sr04.hc_sr04(trigger_pin=23, echo_pin=24)
while True:
    print(str(sensor.get_distance_cm()))
