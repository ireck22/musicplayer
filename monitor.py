#!/usr/bin/python
# -*- coding: utf8 -*-
# coding: utf8
import subprocess
import os
import pyaudio
import pygame
import time
import threading
import sys 

def mon():
	time.sleep(17)
	result=""
	while result !=[]:
		result=os.popen("pidof omxplayer.bin").readlines()
		#print result
	print "ok"
	#os.system("sudo kill -9"+result2)




