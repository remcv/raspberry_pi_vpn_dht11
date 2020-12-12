import time  
import adafruit_dht
import board
from datetime import datetime, date
    
dht = adafruit_dht.DHT11(board.D4)
    
while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        # Print what we got to the REPL
        current_date = date.today()
        current_time = datetime.now()
        current_datetime_formatted = current_date.strftime("%d/%m/%Y") + " " + current_time.strftime("%H:%M:%S")
        print(current_datetime_formatted + " - Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)
    
    time.sleep(4)