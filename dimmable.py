from gpiozero import PWMLED
from time import sleep
from gpiozero import RotaryEncoder

rotor = RotaryEncoder(5, 6, wrap=True, max_steps=180)

led = PWMLED(18)

while True:
    led.value = (rotor.steps / 180) ** 2
    print(rotor.steps)
