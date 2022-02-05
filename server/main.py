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
estadoBomba = False
wifiConnect.connect()


def debounce(pin):
    global btn_press_counter
    if sw.pressReleased():
        btn_press_counter += 1
        print(btn_press_counter)
        time.sleep_ms(100)


p22 = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(2, machine.Pin.OUT)
p22.irq(trigger=machine.Pin.IRQ_FALLING, handler=debounce)

app = picoweb.WebApp(__name__)


@ app.route("/")
def index(req, resp):
    yield from app.sendfile(resp, '/assets/main.html', content_type="text/html")


@ app.route('/leituras')
def leituras(req, resp):
    random.seed(8)
    numero = random.randrange(0, 30)
    leituras = {"temperatura": numero, "umidade": 60, "luminosidade": 85.4}
    yield from picoweb.jsonify(resp, leituras)


@app.route('/ligabomba')
def ligabomba(req, resp):
    yield from picoweb.jsonify(resp, {'bomba': True})
    led.value(1)
    global estadoBomba
    estadoBomba = True


@app.route('/desligabomba')
def desligabomba(req, resp):
    yield from picoweb.jsonify(resp, {'bomba': False})
    led.value(0)
    global estadoBomba
    estadoBomba = False


@app.route('/estadobomba')
def estadobomba(req, resp):
    global estadoBomba
    yield from picoweb.jsonify(resp, {'bomba': estadoBomba})


app.run(host='192.168.0.105', debug=True)
