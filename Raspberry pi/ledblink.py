from RPi import GPIO as g
import time
led = 40

g.setmode(g.BOARD)
g.setup(led,g.OUT)

while True:
	g.output(led, True)
	print("led is on ")
	time.sleep(1)

	g.output(led,False)
	print("led is off ...")
	time.sleep(1)
