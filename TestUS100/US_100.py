import RPi.GPIO as GPIO
import time
import logging
import wiringpi

LOG_FILENAME='US_100.log'
logging.basicConfig(format='%(asctime)s %(message)s',filename=LOG_FILENAME,
level=logging.DEBUG)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 17
ECHO = 18
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
while True:
	GPIO.output(TRIG,False)
	time.sleep(1.5)
	print("Waiting for sensor to settle")
	GPIO.output(TRIG,True)
	wiringpi.delayMicroseconds(50)
	GPIO.output(TRIG, False)
	pulse_start=wiringpi.micros()

	while GPIO.input(ECHO) == 0:
		pulse_start = wiringpi.micros()
		
	while GPIO.input(ECHO) == 1:
		pulse_end = wiringpi.micros()
	
	pulse_duration = (pulse_end-pulse_start)
	print("Pulse duration =%1f " %pulse_duration)
	distance = (pulse_duration/1000*34.3/2)
	if distance > 2 and distance < 450:
		print("Distance = %1f cm" %distance)
	else:
		print("Out of Range")
		
	logging.debug(distance)
