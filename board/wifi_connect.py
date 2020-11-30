from network import WLAN
from network import STA_IF
import machine


class Wifi_Client:

    def __init__(self, ssid, passphrase):

        wlan = WLAN(STA_IF)

        wlan.active(True)

        wlan.connect(ssid, passphrase)

        while not wlan.isconnected():
            machine.idle()

        print('Wifi connected:', wlan.ifconfig())

