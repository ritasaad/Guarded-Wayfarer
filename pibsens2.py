import RPi.GPIO as GPIO
import pibrella
import time


def beep(count):
    for i in range(count):
        pibrella.buzzer.note(1)
        time.sleep(.1)
        pibrella.buzzer.stop()
        time.sleep(.1)
def reading():
    GPIO.output(Trig, False)
    time.sleep(0.3)
    GPIO.output(Trig, True)
    time.sleep(0.001)
    GPIO.output(Trig, False)

    while GPIO.input(Echo)==0:
        signalOff=time.time()

    while GPIO.input(Echo)==1:
        signalOn=time.time()

    timePassed=signalOn-signalOff
    distance=timePassed*17150

    return distance
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Trig = 15
Echo = 14
RedLed = 27
RedPLed = 24
OrangeLed = 22
GreenLed = 9

GPIO.setup(Trig, GPIO.OUT)#sensor
GPIO.setup(Echo, GPIO.IN)#sensor
GPIO.setup(RedLed,GPIO.OUT)#red led
GPIO.setup(RedPLed,GPIO.OUT)#red led pediatran
GPIO.setup(OrangeLed,GPIO.OUT)#orange led
GPIO.setup(GreenLed,GPIO.OUT)#green led

#GPIO.output(21,True)
#GPIO.output(13,True)
while True:
    GPIO.output(GreenLed,True)
    GPIO.output(RedPLed,True)
    GPIO.output(RedLed,False)
    GPIO.output(OrangeLed,False)
    time.sleep(3)
    GPIO.output(GreenLed,False)
    GPIO.output(OrangeLed,True)
    GPIO.output(RedPLed,True)
    GPIO.output(RedLed,False)
    time.sleep(3)
    GPIO.output(RedLed,True)
    GPIO.output(RedPLed,False)
    GPIO.output(OrangeLed,False)
    GPIO.output(GreenLed,False)
    start_time=time.time()

    while((time.time() - start_time)< 5 ):
        distance = reading()
        print distance
        if distance<20:
            beep(1)
    GPIO.output(RedLed,False)    
    GPIO.output(OrangeLed,True)
    GPIO.output(RedPLed,True)
    GPIO.output(GreenLed,False)
    time.sleep(3)
    #GPIO.output(OrangeLed,False)
    #time.sleep(1)

    
