from network import WLAN
from network import STA_IF
import machine

wlan = WLAN(STA_IF)

wlan.active(True)

wlan.connect('','')

while not wlan.isconnected():
    machine.idle()

print('Wifi connected:', wlan.ifconfig())

