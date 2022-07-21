#!/bin/bash
#
# kmr262 2/28/22 start_video.sh
#
# bash script to launch mplayer and 'video_control.py'
#
python3 video_control.py & 
sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -vo sdl -framedrop -input file=/home/pi/video_fifo /home/pi/bigbuckbunny320p.mp4 
