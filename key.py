#!/usr/bin/python
# -*- coding: utf8 -*-
# coding: utf8
import time
import sys
import os
import speech_recognition
import pyaudio
import pygame
import wave
from datetime import datetime
from threading import Timer




	 
r=speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
	audio=r.listen(source)
	#audio=r.record(source)
text = ""
text = r.recognize_google(audio, language='zh-TW')

#print text
key="ok音樂"
key2=key.decode('utf-8')

while text == key2:
	#print "yes"
	break
	
"""	
while text == key2 :
	#print "111"

	pygame.mixer.init()
	#pygame.mixer.music.load("/var/www/html/video3/music/chosesong.mp3")
	pygame.mixer.music.load("D:\py\music\chosesong.mp3")
	pygame.mixer.music.play()
	time.sleep(1)
		
	

	with speech_recognition.Microphone() as source:
		audio=r.listen(source)
		#audio=r.record(source)
	text = ""
	text = r.recognize_google(audio, language='zh-TW')
		#text = r.recognize_google(audio, language='en-US')

	time.sleep(6)	
	print text

"""