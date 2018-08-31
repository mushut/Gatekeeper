# Gatekeeper - Gateway application for sending data to IBM Cloud

# Import modules! Needs to be run on raspberry pi to work.
import RPi.GPIO as GPIO # Is this needed at all?
import spidev
import ibmiotf.application

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

main()