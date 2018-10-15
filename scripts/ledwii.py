#Max Sayer (c) 2018

# An easy method to turn on an LED with a wiimote.
# Use any ground GPIO and GPIO pin 4 for output.
# Cwiid can be found here: https://github.com/abstrakraft/cwiid

import RPi.GPIO as GPIO
import cwiid
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
button_delay = 0.1

 
print 'Press 1 + 2'
time.sleep(1)
time1 = 0 

try:
	wii=cwiid.Wiimote()
except RuntimeError:
	print "Remote failed to connect.."
	quit()

#wii.rumble = 1
time.sleep(1)
#wii.rumble = 0
wii.led = 4
print "Wii Remote connected..\n"
print "Press Home to disconnect..\n"
print "Welcome to LED testing..\n"
print "Press `A` to turn on an LED"
 
wii.rpt_mode = cwiid.RPT_BTN
 
def timeAdd():
	global time1
	time1+=1

while True:
 	global time1
	buttons = wii.state['buttons']
 
	if (buttons & cwiid.BTN_A):
  		GPIO.output(4,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(4,GPIO.LOW)
		print 'A pressed'
		time1 = 0
  		time.sleep(button_delay)
 	elif (buttons & cwiid.BTN_HOME):
		wii.rumble = 1
		time.sleep(0.1)
		wii.rumble = 0
		print "Quitting"
		quit()
	elif (time1 > 1000000):
		print "No actions performed in  too long..\n"
		print "Quitting.."
		wii.rumble = 1
		quit()
	else:
		timeAdd()
#		print time1
# time1 is used as a basic timeout clock, if the clock gets too high, the user is inactive. this is only for testing.
