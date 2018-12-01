import OPi.GPIO as GPIO
import datetime
from time import sleep          # this lets us have a time delay

port = 7                        # set BCM7 (pin 26) as port (7)
GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering

GPIO.setup(port, GPIO.OUT)      # set BCM7 (pin 26) as an output (LED)

print "Press CTRL+C to exit"

date = datetime.datetime.now()

print "Current time is ", date.hour , ":" , date.minute
if int(date.minute) == 59:
<<<<<<< HEAD
    minute = 00
=======
    minute = 0
>>>>>>> 7723607ca1a926d8e8314aab331725c1c8df7090
    hour = int(date.hour)+1
else:
    minute = int(date.minute)+1
    hour = int(date.hour)
<<<<<<< HEAD
print "It`ll be exit and set LED OFF automaticly on ", hour , ":" , minute
=======
print "It`ll be exit automaticly on ", hour , ":" , minute
>>>>>>> 7723607ca1a926d8e8314aab331725c1c8df7090

while True:
    date = datetime.datetime.now()
    if int(date.minute) == minute:
        GPIO.output(port, 0)       # set port/pin value to 1/HIGH/True
<<<<<<< HEAD
        quit()
    else:
        GPIO.output(port, 1)       # set port/pin value to 0/LOW/False
=======
    else:
        GPIO.output(port, 1)       # set port/pin value to 0/LOW/False


#_______________________________
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
import datetime
#initialize the gpio module
gpio.init()

#setup the port (same as raspberry pi's gpio.setup() function)
gpio.setcfg(port.PA6, gpio.OUTPUT)
date = datetime.datetime.now()
while True:
	date = datetime.datetime.now()
	if int(date.minute) == 45:
#now we do something (light up the LED)
		gpio.output(port.PA6, gpio.HIGH)
#turn off the LED after 2 seconds
	if int(date.minute) == 46:
		gpio.output(port.PA6, gpio.LOW)
	sleep(0.1)
	print(date.second)
>>>>>>> 7723607ca1a926d8e8314aab331725c1c8df7090
