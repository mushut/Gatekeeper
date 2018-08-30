# Gatekeeper - Gateway application for sending data to IBM Cloud

# Import modules!
import RPi.GPIO as GPIO
import spidev
import ibmiotf.application

def main():
    print("Gatekeeper")
    spi = spidev.SpiDev()
    spi.open(bus, device)

    # SPI settings

    test_send = [0x01, 0x02, 0x03]
    spi.xfer(test_send)
    # Or xfer2

main()