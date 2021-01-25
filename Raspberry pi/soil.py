
import RPi.GPIO as g
import time


pin = 3

g.setmode(g.BOARD)
g.setup(pin, g.IN)

def callback(pin):
	if g.input(pin):
		print("no water detected..!!!! ")
		time.sleep(0.2)
	else:
		print("water detacted..")
		time.sleep(0.2)
g.add_event_detect(pin,g.BOTH, bouncetime=300)
g.add_event_callback(pin, callback)

#while True:
#	time.sleep(0.1)


'''



import RPi.GPIO as g
import time


g.setmode(g.BOARD)
g.setup(3,g.IN)

while True:
	if (g.input(g==1)
		print("Water soil")
		time.sleep(0.1)

	else:
		print("Dry Soil...!!!!")
		time.sleep(0.1)

'''

