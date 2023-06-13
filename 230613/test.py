import Adafruit_DHT as dht
import time


sensor = dht.DHT11
rcv_pin = 10

try:
    while True:
        humid, temp = dht.read_retry(sensor, rcv_pin)
        print(f'temp : {temp} / humid : {humid}')

        time.sleep(1)
except Exception as ex:
    print(ex)
finally:
    print('Program fin')