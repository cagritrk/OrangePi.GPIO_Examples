import OPi.GPIO as GPIO
import datetime
from time import sleep          # this lets us have a time delay

port = 7                        # set BCM7 (pin 26) as port (7)
GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering
GPIO.setwarnings(False)         # just for ingnore the bord already using warning

GPIO.setup(port, GPIO.OUT)      # set BCM7 (pin 26) as an output (LED)

date = datetime.datetime.now()

print "Current time is ", date.hour , ":" , date.minute
if int(date.minute) == 59:
    minute = 0
    hour = int(date.hour)+1
else:
    minute = int(date.minute)+1
    hour = int(date.hour)
print "It`ll be exit and set LED OFF automaticly on ", hour , ":" , minute

print "Press CTRL+C to exit"
while True:
    date = datetime.datetime.now()
    if int(date.minute) == minute:
        GPIO.output(port, 0)       # set port/pin value to 1/HIGH/True
        print "bye :) "
        quit()
    else:
        GPIO.output(port, 1)       # set port/pin value to 0/LOW/False
