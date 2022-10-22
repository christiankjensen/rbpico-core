import network
import umachine
import utime
import ujson

ob_led = umachine.Pin("LED", machine.Pin.OUT)
wifi = network.WLAN(network.STA_IF)
    
with open('net-cache.json') as f:
    data = ujson.load(f)
    netcache = data.get('networks')
    
active_network = netcache[0] # change this as necessary if json file has multiple networks
ssid = active_network.get('ssid','No ssid found')
password = active_network.get('password','No password found')
print('')

def do_connect():
    if not wifi.isconnected():
        print('connecting to network ' + active_network['ssid'])
        ob_led.on()
        wifi.active(True)
        wifi.connect(ssid, password)
        now = ticks_ms()
        diff = 
        while not wifi.isconnected() and diff > 10000 :
            print(f'Connecting to {ssid}...')
            pass
    if wifi.isconnected():
        print('Connected')
        ob_led.off()
        utime.sleep_ms(100)
        ob_led.on() # 1
        utime.sleep_ms(100)
        ob_led.off()
        utime.sleep_ms(100)
        ob_led.on() # 2
        utime.sleep_ms(100)
        ob_led.off()

def print_connection():
    if 'No ssid found' in name:
        print('Not connected to wifi')
    else:
        print('Network:\t' + ssid)
        print('Configuration:\t', wifi.ifconfig())
        print('')

do_connect()
print_connection()
