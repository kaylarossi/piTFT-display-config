#
# kmr262 2/24/22 four_button.py
# initialize four buttons on piTFT
#
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  #set broadcom numbering
#set up piTFT buttons with pull up
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


code_run = True
while code_run:
    time.sleep(0.2)
    if (not GPIO.input(22)):
        print(" ")
        print("Button 22 has been pressed")

    elif (not GPIO.input(27)):
        print(" ")
        print("Button 27 has been pressed")

    #button edge button quits program when pressed
        code_run=False

    elif (not GPIO.input(17)):
        print(" ")
        print("Button 17 has been pressed")

    elif (not GPIO.input(23)):
        print(" ")
        print("Button 23 has been pressed")
