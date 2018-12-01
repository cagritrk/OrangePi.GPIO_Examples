import OPi.GPIO as GPIO
from time import sleep          # this lets us have a time delay

port = 7                        # set BCM7 (pin 26) as port (7)
GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering

GPIO.setup(port, GPIO.OUT)      # set BCM7 (pin 26) as an output (LED)

print ("Press CTRL+C to exit")

while True:
    GPIO.output(port, 1)       # set port/pin value to 1/HIGH/True
    sleep(0.05)
    GPIO.output(port, 0)       # set port/pin value to 0/LOW/False
    sleep(0.05)
