import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	text = input('New data enter :')
	print(text)
	print("Now a place the tag of here..")
	#way = reader.write(text)

	data=reader.write(text)
	print(data)

#	if data =='730233248253':
#		print("the door is open..!!")

	#elif data == '730233248253':
	#	print("the door is close ..!!!")
#	else:

#		print("enter valid card")
#	print(way)

	print("wriiten..")

finally:
	GPIO.cleanup()
