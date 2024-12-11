import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 17
while True:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    sig = GPIO.input(pin)
    if sig == GPIO.HIGH:
        print("HIGH")    
    
    else:
        print("LOW")    
    time.sleep(2)