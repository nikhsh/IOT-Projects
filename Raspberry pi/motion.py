import RPi.GPIO as g
import time
pir = 5
led = 7

g.setmode(g.BOARD)

g.setup(led, g.OUT)
g.setup(pir, g.IN)

current_state = 0


try:
	while True:
		time.sleep(0.1)
		current_state = g.input(pir)
		if current_state == 1:
			print("GPIO PIN IS %s is %s" % (pir,current_state))
			g.output(led,True)
			time.sleep(0.2)
			g.output(led, False)
			time.sleep(0.2)


except KeyboardInterrupt:
	pass

finally:
	g.cleanup()
