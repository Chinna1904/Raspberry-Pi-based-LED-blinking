import time
import RPi.GPIO as GPIO
ledpin1 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin1,GPIO.OUT)
while True:
    try:
        GPIO.output(ledpin1,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(ledpin1,GPIO.LOW)
        time.sleep(1)
    except:
        print("some error")
        
    finally:
        GPIO.cleanup()
        