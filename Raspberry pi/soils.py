import RPi.GPIO as g
import time


led = 3

g.setmode(g.BOARD)
g.setup(led, g.IN)

while True:
	try:
		if g.input == True:
			g.input(led, True)
			print("water the detceted....")
			time.sleep(0.2)
		else:
	#		g.input(led, False)
			print("No water detected.....")
			time.sleep(0.2)

	except KeyboardInterrupt:
		g.cleanup()
