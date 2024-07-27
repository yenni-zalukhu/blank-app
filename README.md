import dht
from machine import Pin
import time

# Set up DHT11 sensor on GPIO4
dht_sensor = dht.DHT11(Pin(4))

while True:
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        print('Temperature: %3.1f C' %temp)
        print('Humidity: %3.1f %%' %humidity)
    except OSError as e:
        print('Failed to read sensor.')
    
    time.sleep(2)
