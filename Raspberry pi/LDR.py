import RPi.GPIO as g
#from ldr_pr import LDR
import LDR
import time



while True:
	try:
		g.setmode(g.BOARD)
		g.setwarnings(False)
		g.setup(3,g.OUT)

		p = 5
#		for i in range(0,3):
#			p=p+LDR(11,13)
#		p_avg = p/5
#		p=diff = 500 - p_avg


		if p >= 0:
			g.output(3, g.HIGH)
			time.sleep(0.2)

		else:
			g.output(3,g.LOW)
			time.sleep(0.2)


	except KeyboardInterrupt:
			g.cleanup()
