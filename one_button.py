#
#   kmr262 2/24/22 one_button.py
# initalize one button on piTFT
#
#buttons on piTFT in order: GPIO 22, 27, 17, 23

import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)  #set broadcom numbering
#set up one button on piTFT with pull up
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(0.2)
    if (not GPIO.input(17)):
        print (" ")
        print ("Button 17 has been pressed")
