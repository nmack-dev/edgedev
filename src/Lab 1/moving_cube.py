#!/usr/bin/env python
# moving_cube.py
# Nathan Mack 2020

from luma.core.interface.serial import ftdi_i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from time import sleep

# Device String
ft232h_device = 'ftdi://ftdi:232h/1'

# Luma Core I2C Bus Controller
oled_i2c = ftdi_i2c(ft232h_device, 0x3C)
oled_dev = ssd1306(oled_i2c)

try:

    # Horizontal and vertical coordinates of the cube
    horz = 0
    vert = 0

    while True:

        # Draws the cube through each loop iteration
        with canvas(oled_dev) as draw:
            draw.rectangle((horz, vert, horz+8, vert+8), outline='white', fill='white')

            # Calculates the horizontal coordinates of the cube
            if (0 < (horz + 8) < 128):
                horz += 8
            elif (-128 < (horz + 8) <= 0):
                horz -= 8
            
            # Calculates the vertical coordinates of the cube
            # Resets the horizontal coordinates
            if ((horz + 8) == 128):
                vert += 8
                horz = -8
            elif ((horz + 8) == -120):
                vert += 8
                horz = 0
        
        sleep(1)

# Ends the program
except KeyboardInterrupt:
    print('Done')