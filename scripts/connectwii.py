# Max Sayer (c) 2018
# To find other wiimote button names, use the python command dir(cwiid)
# Cwiid can be found here: https://github.com/abstrakraft/cwiid

import cwiid
import time
 
button_delay = 0.1
tries = 0
 
print 'Press 1 + 2'
time.sleep(1)
 
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

 
wii.rpt_mode = cwiid.RPT_BTN
 

while True:
 
	buttons = wii.state['buttons']
 
	if (buttons & cwiid.BTN_LEFT):
  		print 'Left pressed'
  		time.sleep(button_delay)
 
	if (buttons & cwiid.BTN_HOME):
#		wii.rumble = 1
		print "Quitting"
		quit()
	
