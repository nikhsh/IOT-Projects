import RPi.GPIO as g
#import RPi.GPIO as gpio
import time


pin = 3
led = 40
g.setmode(g.BOARD)
g.setwarnings(False)
g.setup(led,g.OUT)





while True:
	g.setup(pin, g.OUT)
	g.output(pin,g.LOW)
	time.sleep(0.1)

	g.setup(pin,g.IN)
	currentTime = time.time()
	diff = 1000

	while (g.input(pin) == g.LOW):
		diff = time.time() - currentTime

		print(diff * 1000)
		time.sleep(1)

		if diff <= 100000:

			while True:
				g.output(led,True)
				print("Ligt ON")
				time.sleep(1)

				g.output(led,False)
				print("ligt is OFF")
				time.sleep(1)

		else:
			print("nooo")

	print(diff * 1000)
	time.sleep(1)
