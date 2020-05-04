import sensor_dht11 as lib_dht11


def getMAC(interface='eth0'):
    # Return the MAC address of the specified interface
    try:
        str_mac_address = open('/sys/class/net/%s/address' % interface).read()
    except:
        str_mac_address = "00:00:00:00:00:00"
    return str_mac_address[0:17]


def get_speed_of_sound():
    dht11 = lib_dht11.dht11(4)
    return 331 + 0.59 * dht11.get_temperature()

