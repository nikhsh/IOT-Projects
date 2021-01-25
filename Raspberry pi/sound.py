#from RPi.GPIO as g
from RPi import GPIO as g
import time

global led
led = 8
sound = 7
g.setmode(g.BOARD)
g.setup(sound,g.IN)

g.setmode(g.BOARD)
g.setup(led,g.OUT)

try:
	while True:
		if g.input(sound):
			print("sound is detaction")
#			time.sleep(0.3)
			while True:
				led = 8
				g.output(led,True)
				print("led is on ")
				time.sleep(0.1)
			
				g.output(led,False)
				print("led is off ")
				time.sleep(0.2)
		else:
			print("not detaction")
			time.sleep(0.3)
except KeyboardInterrupt:
	g.cleanup()


