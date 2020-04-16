#!/usr/bin/env python2.7
# Learn interrupts at https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
##GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
##GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def my_callback(channel):  
    print ("falling edge detected on 17")

def my_callback2(channel):
    print ("falling edge detected on 23")
def keyboardRead():
    i=1
    switcher=[
        (96675065265, "Paranoid Android"),
        (664003290249, "Creep"),
        (649586696873, "High and Dry"),
        (711986787821, "Bonfire Heart")
    ]
    for item in switcher:
        print(str(i) + ": " + str(item))
        i = i+1
    print("s: Stop the current song")
    text = input('Select option:')
    if text.isnumeric():
        return switcher[int(text)-1]
    else:
        return (-1, "Stop the current song")

input("Press Enter when ready\n>")

GPIO.add_event_detect(11, GPIO.FALLING, callback=my_callback, bouncetime=300)
##GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2, bouncetime=300)

try:  
##    print ("Waiting for falling edge on port 24")
##    GPIO.wait_for_edge(24, GPIO.RISING)  
##    print ("Raising edge detected. Here endeth the third lesson.")
    while True:
        keyboardRead()
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  