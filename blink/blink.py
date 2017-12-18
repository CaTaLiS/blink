import time
import RPi.GPIO as GPIO
import sys

led_pin = 4
default_delay_in_sec = 1

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.HIGH)
    
def get_delay_in_sec(arg):
    if arg is not None:
        try:
            delay_in_sec = float(arg)
            print('Setting delay between blinks to {0} sec').format(delay_in_sec)
            return delay_in_sec
        except TypeError:
            print('Not a float delay argument. Setting to default value of {0} sec').format(default_delay_in_sec)
            return default_delay_in_sec
    print('Not entered a delay argument. Setting to default value of {0} sec').format(default_delay_in_sec)
    return default_delay_in_sec

def blink(delay_in_sec):
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(delay_in_sec)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(delay_in_sec)

def destroy():
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    print('Starting blink program...')
    setup()
    try:
        blink(get_delay_in_sec(sys.argv[1]))
    except KeyboardInterrupt:
        destroy()


