import OPi.GPIO as GPIO
import sys
from time import sleep          # this lets us have a time delay

port = 7                        # set BCM7 (pin 26) as port (7)
GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering

GPIO.setup(port, GPIO.OUT)      # set BCM7 (pin 26) as an output (LED)

print ("Press CTRL+C to exit")

time = int(sys.argv[0])

while True:
    GPIO.output(port, 1)       # set port/pin value to 1/HIGH/True
    sleep(time)
    GPIO.output(port, 0)       # set port/pin value to 0/LOW/False
    sleep(time)
