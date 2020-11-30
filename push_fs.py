import os
import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect(('192.168.4.1',80))

skt.send(b'/flash/key')
skt.sendfile(open('flash/key','rb'))
