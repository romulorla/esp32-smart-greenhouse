from MyKitSwitch import mySwitch
import time
import json
import machine
import upip
import picoweb
import network
import wifiConnect
import random

sw = mySwitch(22)
led = machine.Pin(13, machine.Pin.OUT)
btn_press_counter = 0

wifiConnect.connect()


def debounce(pin):
    global btn_press_counter
    if sw.pressReleased():
        btn_press_counter += 1
        print(btn_press_counter)
        time.sleep_ms(100)


p22 = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)
p22.irq(trigger=machine.Pin.IRQ_FALLING, handler=debounce)

app = picoweb.WebApp(__name__)


@ app.route("/")
def index(req, resp):
    yield from app.sendfile(resp, '/assets/main.html')


@ app.route('/leituras')
def leituras(req, resp):
    random.seed(8)
    numero = random.randrange(0, 30)
    leituras = {"temperatura": numero, "umidade": 60}
    yield from picoweb.jsonify(resp, leituras)


app.run(host='192.168.0.105', debug=True)
