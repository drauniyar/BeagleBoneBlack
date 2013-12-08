import Adafruit_BBIO.GPIO as GPIO

GPIO.setup(P9_11, GPIO.OUT)
while true:
	GPIO.output(P9_11, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(P9_11, GPIO.LOW)
	time.sleep(1)
