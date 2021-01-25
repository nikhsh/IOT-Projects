import picamera
from time import sleep


camera = picamera.PiCamera()
camera.resolution = (1024,768)
camera.brightness = 60
camera.start_preview()

camera.capture('image2.jpg')
time.sleep(5)
camera.stop_preview()
