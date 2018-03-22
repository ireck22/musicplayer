#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
import pyaudio
import pygame
import time
import threading
#import main

result=os.popen("pidof vlc").readlines()
len(result[0])
result2=len(result[0])
print result2
#os.system("sudo killall -9 vlc")
#print "end"

#print main.x
#main.re1()
#print main.re4
re2="https://www.youtube.com/embed/LWV-f6dMN3Q"
if result2==5:
	os.system("youtube-dl "+re2)
