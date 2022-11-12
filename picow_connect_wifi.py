import network
import umachine
import utime
import ujson
import gc

ob_led = umachine.Pin('LED', machine.Pin.OUT)
wifi = network.WLAN(network.STA_IF)
    
with open('net-cache.json') as f:
    data = ujson.load(f)
    netcache = data.get('networks')
    
active_network = netcache[0]
ssid = active_network.get('ssid','No ssid found')
password = active_network.get('password','No password found')
print('')

def do_connect():
    if not wifi.isconnected():
        start = utime.ticks_ms()
        utime.sleep_ms(10)
        print('Connecting to network {active_network['ssid']}')
        ob_led.on()
        wifi.active(True)
        wifi.connect(ssid, password)
        print(f'Connecting to {ssid}...')
        now = utime.ticks_ms()
        diff = now - start
        while not wifi.isconnected() and diff <= 10000:
            now = utime.ticks_ms()
            diff = now - start
            print(f'Elapse: {round(diff/1000, 2)} seconds\n')
        if wifi.isconnected():
            print(f'Connected in {round(diff/1000, 2)} seconds\n')
            ob_led.off()
            utime.sleep_ms(100)
            ob_led.on() # 1
            utime.sleep_ms(100)
            ob_led.off()
            utime.sleep_ms(100)
            ob_led.on() # 2
            utime.sleep_ms(100)
            ob_led.off()
            utime.sleep_ms(100)
            ob_led.on() # 3
            utime.sleep_ms(100)
            ob_led.off()
            utime.sleep_ms(100)
        else:
            print('ConnectionError: Timeout (10s)\n')
    else:
        ob_led.on() # 1
        utime.sleep_ms(100)
        ob_led.off()
        utime.sleep_ms(100)

def do_disconnect():
    if wifi.isconnected():
        start = utime.ticks_ms()
        utime.sleep_ms(10)
        print(f'Disconnecting from {ssid}...')
        wifi.disconnect()
        now = utime.ticks_ms()
        diff = now - start
        while wifi.isconnected() and diff <= 10000:        
            now = utime.ticks_ms()
            diff = now - start
            print(f'Elapse: {round(diff/1000, 2)} seconds\n')
        if wifi.isconnected():
            print('DisconnectError: Timeout (10s)\n')
        else:
            wifi.active(False)
            print('Disconnected successfully.\n')
    else:       
        print('Not connected to wifi')
        
def print_connection():
    if wifi.isconnected():
        print('----------------------------------------------------------------------------------')
        print(f'      Network:\t{ssid}')
        print(f'Configuration:\t{wifi.ifconfig()}')
        print('----------------------------------------------------------------------------------')
        print('')
    else:
        print('Not connected to wifi')
        
do_connect()
print_connection()
print(f'  Free Memory:\t{str(gc.mem_free())} bytes\n')
