import time
from wifi_connect import Wifi_Client
from simple import MQTTClient
from machine import Pin


import ujson as json
import uasyncio




INDICATOR_PIN = Pin(2, Pin.OUT)



CONFIG_FILE = "/flash/creds.json"



# read configuration values from file
with open(CONFIG_FILE, 'r') as f:
    config = json.loads(f.read())
MQTT_CLIENT_ID = config['iot']['client_id']
MQTT_PORT = 8883
MQTT_TOPIC = config['iot']['topic_prefix'] + MQTT_CLIENT_ID
MQTT_HOST = config['iot']['endpoint']
WIFI_SSID = config['wifi']['ssid']
WIFI_PP = config['wifi']['passphrase']



#read device credentials
with open(config['iot']['cert_file'],'r') as f:
    MQTT_CERT = f.read()
with open(config['iot']['key_file'],'r') as f:
    MQTT_KEY = f.read()


# connect to WIFI
wifi = Wifi_Client(WIFI_SSID, WIFI_PP)


mqtt_client = None




def connect():
    global mqtt_client
    global MQTT_CERT
    global MQTT_KEY
    try:
        mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, server=MQTT_HOST, port=MQTT_PORT, keepalive=0, ssl=True, ssl_params={"cert":MQTT_CERT, "key":MQTT_KEY, "server_side":False, "server_hostname":MQTT_HOST, "do_handshake":True},debug=True)
        mqtt_client.connect()
        print('MQTT Connected')

        
    except Exception as e:
        print('Cannot connect MQTT: ' + str(e))
        raise



async def keep_alive():
    while 1:
        global mqtt_client
        print('pinging mqtt broker')
        mqtt_client.ping()
        await uasyncio.sleep(60)
        
async def poll():
    global mqtt_client
    while 1:
        mqtt_client.check_msg()
        await uasyncio.sleep(1)


def fire(duration):
    INDICATOR_PIN.on()
    time.sleep_ms(duration)
    INDICATOR_PIN.off()


def receive_msg(topic,msg):
    print(topic,msg)
    fire(1000)

def subscribe():
    global mqtt_client
    try:
        mqtt_client.set_callback(receive_msg)
        mqtt_client.subscribe(MQTT_TOPIC)
    except Exception as e:
        print("Erros subscribing to ",MQTT_TOPIC,": ",str(e))


connect()
subscribe()

loop = uasyncio.get_event_loop()
loop.create_task(keep_alive())
loop.create_task(poll())
loop.run_forever()

print('running forever')
