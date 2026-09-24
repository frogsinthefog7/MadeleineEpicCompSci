
from gpiozero import Button
from gpiozero import LED
from signal import pause
import tm1637
from time import sleep
import numpy as np
import random


Green = LED(21)
button = Button(12)
button_two = Button(6)

tm = tm1637.TM1637(clk = 4, dio = 17)
clear = [0, 0, 0, 0]
tm.write(clear)

nums = [1,2,3,4]

while True:
    if button.is_pressed:
        nums = []
        x = 4
        while x > 0:
            nums.append(str(random.randint(1,5)))
            print(nums)
            x -= 1
        nums_int = ''.join(nums)
        nums_int = int(nums_int)
        tm.number(nums_int)

    elif button_two.is_pressed:
        nums = []
        x = 4
        while x > 0:
            nums.append(str(random.randint(1,5)))
            print(nums)
            x -= 1
        nums_int = ''.join(nums)
        nums_int = int(nums_int)
        tm.number(nums_int)
        x = str(random.randint(1,5))
        nums = [x,x,x,x]
        rigged_nums_int = ''.join(nums)
        rigged_nums_int = int(rigged_nums_int)
        tm.number(rigged_nums_int)

    else:
        if nums[0] == nums[1] and nums[1] == nums[2] and nums[2] == nums[3]:
            Green.blink()
            sleep(5)
            Green.off()
            sleep(1)
            nums = [1,2,3,4]
