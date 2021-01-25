import RPi.GPIO as g
import time
channel = 18
g.setmode(g.BOARD)
g.setup(channel, g.IN)

def callback(channel):
	if g.input(channel):
		print("no water level detacted")
	else:
		print("water detected..")

g.add_event_detect(channel, g.BOTH, bouncetime=300)
g.add_event_callback(channel,callback)

while True:
	time.sleep(1)
