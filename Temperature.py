
import time
import board
import adafruit_dht
from datetime import datetime
from gpiozero import LED

sensor = adafruit_dht.DHT11(board.D16)

red = LED(19)
blue = LED(13)

print("time,celsius,fahrenheit")

def to_fahrenheit(c):

    f = (c * (9/5)) + 32
    return f

while True:
    try:
        celsius = sensor.temperature #get temp in clecius from censor
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()

        with open("temperature.csv", "a") as f:
            f.write("\n {0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit, ))

        if fahrenheit >= 72:
            blue.off()
            red.on()
        elif fahrenheit < 72:
            red.off()
            blue.on()

        time.sleep(3.0)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error