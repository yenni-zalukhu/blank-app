# Import required libraries
import machine
import time
import urequests
import dht

# Set up the DHT11 sensor
d = dht.DHT11(machine.Pin(14))

# Server URL
url = "http://10.0.3.113:8502"

while True:
    try:
        # Read data from DHT11 sensor
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        
        # Create data payload
        data = {
            "temperature": temp,
            "humidity": hum
        }
        
        # Send data to server
        response = urequests.post(url, json=data)
        
        # Print server response
        print(response.text)
        
        # Wait for a minute before the next reading
        time.sleep(60)
        
    except Exception as e:
        print("Error: ", e)
        time.sleep(60)
