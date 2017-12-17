import time
import RPi.GPIO as GPIO

led_pin = 4

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.HIGH)

def blink():
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)

def destroy():
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    print('start program')
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()


