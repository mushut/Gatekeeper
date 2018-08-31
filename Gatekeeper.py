# Gatekeeper - Gateway application for sending data to IBM Cloud

# Import modules! Needs to be run on raspberry pi to work.
import RPi.GPIO as GPIO # Is this needed at all?
import spidev
import ibmiotf.application
import time

def test_cloud_connection():
    # Send integer value from 0 to 255 in interval of 1 second to IBM Cloud for testing purposes
    value = 0

    # Add options
    test_client = ibmiotf.application.Client()
    test_client.connect()

    while True:
        # send value
        test_client.publishEvent() # Remember to add testing info

        value += 1

        if value > 255:
            value = 0

        time.sleep(1)   # Change if different time interval needed.

def main():
    print("Gatekeeper")

    # Open SPI connection
    # bus = ?
    # device = ?
    spi = spidev.SpiDev()
    spi.open(bus, device)

    # SPI settings

    # Send test data
    test_send = [0x01, 0x02, 0x03]
    spi.xfer(test_send)
    # Or xfer2

    # Send data to IBM Cloud with testing function
    test_cloud_connection()

main()