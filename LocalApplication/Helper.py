def getMAC(interface='eth0'):
    # Return the MAC address of the specified interface
    try:
        str_mac_address = open('/sys/class/net/%s/address' % interface).read()
    except:
        str_mac_address = "00:00:00:00:00:00"
    return str_mac_address[0:17]
