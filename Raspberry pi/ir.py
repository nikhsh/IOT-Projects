'''
import RPi .GPIO as g
import time 

sensor = 3

g.setmode(g.BOARD)
g.setup(sensor, g.IN)
print("ready to detaction object..")

try:
	while True:
		if g.input(sensor):
			#print(sensor, True)
			#print("object is not detacted detaction ")
			if g.input(sensor):
				print("object ")
				time.sleep(1)
			else:
			#g.input(sensor, False)
				print(" all over object  detaction ")
				time.sleep(1)
except KeyboardInterrupt:
	g.clenup()

'''



import RPi.GPIO as g
import time
import sys

sensor = 3
g.setmode(g.BOARD)
g.setup(sensor,g.IN)

print("Ready to go .....")

class irs:
	def ma():
#		while True:
			try:
				if g.input(sensor):
					print("object not is detacetion ..")
					time.sleep(1)

				else:
					print("object is the detaction")
					time.sleep(1)

			except KeyboardInterrupt:
				g.cleanup()

class mas:
	def main():
		irs.ma()
irs.ma()
