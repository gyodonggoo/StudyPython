import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT) #red
GPIO.setup(20, GPIO.OUT) #green
GPIO.setup(21, GPIO.OUT) #blue

try:
    while True: # loop
        GPIO.output(19, True) # on
        GPIO.output(20, False) # off
        GPIO.output(21, False) # off
        time.sleep(1)

        GPIO.output(19, False) # off
        GPIO.output(20, True) # on
        GPIO.output(21, False) # off
        time.sleep(1)

        GPIO.output(19, False) # off
        GPIO.output(20, False) # off
        GPIO.output(21, True) # on
        time.sleep(1)

except Exception as e:
    print(e)
finally:
    GPIO.cleanup()