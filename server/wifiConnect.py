import network


def connect():
    ssid = 'GARAGEM (2.4GHz)'
    password = 'joaovitorlindo'
    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print('Já conectado')
        return

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print('Conectado')
    print(station.ifconfig())
