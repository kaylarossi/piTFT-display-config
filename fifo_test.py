#
# kmr262 2/24/22 fifo_test.py
#
# use user input to control mplayer

import subprocess
import os

#convert input into string
p_text = "Enter command: "

#commands: pause, quit, fast-forward, re-wind
code_run = True

while code_run:
    user_in = input(p_text)
    user_str = str(user_in)
    if user_str == 'pause':
        #pause mplayer
        u_in = 'echo "pause" > /home/pi/video_fifo'
        subprocess.check_output(u_in, shell=True)

    elif user_str == 'forward':
        #fast forward 10 seconds
        u_in = 'echo "seek 10 0" > /home/pi/video_fifo'
        subprocess.check_output(u_in, shell=True)

    elif user_str == 'backward':
        #rewind 10 seconds
        u_in= 'echo "seek -10 0" > /home/pi/video_fifo'
        subprocess.check_output(u_in, shell=True)

    elif user_str == 'quit':
        #quit mplayer
        u_in = 'echo "quit" > /home/pi/video_fifo'
        subprocess.check_output(u_in, shell=True)
        if 'quit':
            code_run = False

    else:
        print ('not valid...')
