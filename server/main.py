import json
import machine
from machine import UART
import upip
import picoweb
import network
import uasyncio as asyncio

import wifiConnect
import random

led = machine.Pin(13, machine.Pin.OUT)
app = picoweb.WebApp(__name__)
wifiConnect.connect()
station = network.WLAN(network.STA_IF)
uart = UART(2, baudrate=9600, rx=16, tx=17, timeout=10)


@ app.route("/")
def index(req, resp):
    yield from app.sendfile(resp, '/assets/main.html', content_type="text/html")


@ app.route('/leituras')
def leituras(req, resp):
    leituras = json_data
    yield from picoweb.jsonify(resp, leituras)


async def read_arduino_data():
    while True:
        await asyncio.sleep(1)
        try:
            received_data = uart.read().decode('utf-8')
            global json_data
            json_data = json.loads(received_data)
            print(json_data)
        except:
            print('no data received')


asyncio.create_task(read_arduino_data())
ip = str(station.ifconfig()[0])
app.run(host='{0}'.format(ip), debug=-1)
