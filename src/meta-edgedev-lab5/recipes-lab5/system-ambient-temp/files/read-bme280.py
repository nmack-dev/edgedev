#!/usr/bin/env python3
from pyftdi.i2c import I2cController, I2cPort
from bme280 import BME280
from time import sleep
import boto3
import botocore
import statistics

# A class that implements a not full ring buffer
class RingBuffer:
    def __init__(self,size_max):
        self.max = size_max
        self.data = []

    # A child class that implements a full ring buffer
    class Full(RingBuffer):
        # Append an element overwriting the oldest one
        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        
        # Return list of ring buffer elements in correct order
        def get(self):
            return self.data[self.cur:]+self.data[:self.cur]

    # Appends element to the ring buffer
    # Switches to full child class if full
    def append(self,x):
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0 
            # Permanently change self's class from non-full to full
            self.__class__ = self.Full

    # Returns elements from oldest to newest
    def get(self):
        return self.data

# Wrapper to add support for BME280 library
class FTDI_WRAPPER_I2C( I2cPort ):

    def read_i2c_block_data(self, i2c_addr, register, length):
        return self.read_from(register, length)

    def write_i2c_block_data(self, i2c_addr, register, data):
        self.write_to(register, data)

# FTDI I2C Bus Controller
pyftdi_i2c = I2cController()
pyftdi_i2c.configure('ftdi://ftdi:232h/1')

# Get FTDI I2C Port and override class with wrapper
bme280_i2c = pyftdi_i2c.get_port(0x76)
bme280_i2c.__class__ = FTDI_WRAPPER_I2C

# BME280 Sensor
bme280 = BME280(i2c_dev=bme280_i2c)

# Initializes AWS SNS
sns = boto3.client('sns')

# Minute Count
minute_count = 0

# The circular buffer structure that contains temperature data
temp_buffer = RingBuffer(1440)

# Phone number to send messages to
phone_number = '269-626-4355'

# A function that publishes a message to a specified phone number
def sms_pub(pn, msg):
    response = sns.publish(
        PhoneNumber=pn,
        Message=msg
    )
    print(response)

# Read data until stopped by Ctrl+c
try:
    while True:
        # Causes the system to sleep for a minute and then captures the temperature
        sleep(60)
        temperature = bme280.get_temperature() * 9.0 / 5.0 + 32.0
        # Appends the temperature to circular buffer
        temp_buffer.append(temperature)
        
        # Alerts when the ambient temperature is above or below a specific setpoint
        if (temperature > 176):
            sms_pub(phone_number, 'ALERT! Temperature Above 176°F')
        elif (temperature < 33):
            sms_pub(phone_number, 'ALERT! Temperature Below 32°F')

        # Iterates a minute count variable for program runtime
        minute_count += 1
        
        # Uses minute count to determine when 24 hours have passed
        if (minute_count == 1440):
            # The message to be sent to the specified phone number
            msg_payload = ''
            # Grabs a snapshot of the circular buffer in the form of a list
            buffer_list = temp_buffer.get()
            data_list = []

            # Iterates through the snapshot and generates hourly statistics
            for index in range(1440):
                if (index % 60 == 0):
                    # Hourly statistics
                    data_list.append(buffer_list[index])
                    hourly_mean = statistics.mean(data_list)
                    hourly_max = max(data_list)
                    hourly_min = min(data_list)
                    
                    # Creates the message payload to be sent
                    msg_payload += ('Hourly Mean: ' + str(hourly_mean))
                    msg_payload += (' Hourly Max: ' + str(hourly_max))
                    msg_payload += (' Hourly Min: ' + str(hourly_min))
                    msg_payload += '\n'

                    # Resets the data list and sends the message
                    data_list = []
                    sms_pub(phone_number, msg_payload)
                
                else:
                    data_list.append(buffer_list[index])
            
except KeyboardInterrupt:
    print('\nStopped')
