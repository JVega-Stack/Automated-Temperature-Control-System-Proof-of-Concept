import board
import adafruit_dht
import time

dht = adafruit_dht.DHT11(board.D4)

def read_temperature_c():
    try:
        temp_c = dht.temperature
        return temp_c
    except RuntimeError:
        time.sleep(0.5)
        return None
