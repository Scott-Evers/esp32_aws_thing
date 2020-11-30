import utils, usocket as socket, os
from network import WLAN, AP_IF


ap = WLAN(AP_IF)
ap.config(essid=utils.get_machine_id(), channel=11)

ap.active(True)


print('Wifi connected:', ap.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)


def process_file(conn,addr):
    path = conn.recv(4096).decode('ascii')
    utils.mkdir(path)
    file = conn.recv(4096)
    with open(path, 'wb') as f:
        f.write(file)
    
    
    conn.close()

while 1:
    conn, addr = s.accept()
    process_file(conn,addr)
    print('got a connection from {}'.format(str(addr)))
    








