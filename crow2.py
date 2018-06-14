#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
import pyaudio
import pygame
import time
import threading
import speech_recognition
import song
import sys
import codecs

def voice():
	keyword=("我要切歌").decode('utf-8')
	text = ""
	
	#while text != keyword:

	r=speech_recognition.Recognizer()
	r.energy_threshold = 4000
	with speech_recognition.Microphone() as source:
		r.adjust_for_ambient_noise(source,duration=0.5)
		audio=r.listen(source)
		#audio=r.record(source)
	try:
		text = r.recognize_google(audio, language='zh-TW')
		print text
		#time.sleep(1)
		if text=="":
			print "ss"	
		if text==keyword:
			os.system("sudo killall -9 omxplayer.bin")
		else:
			song.error()
		result=os.popen("pidof omxplayer.bin").readlines()
		print result
		if result==[]:
			sys.exit()
	except speech_recognition.UnknownValueError:
		text=""
		print("Google Speech Recognition could not understand audio")
		f=codecs.open('cro.log','a',"utf-8" )
		localtime = time.asctime(time.localtime(time.time()))
		f.write(localtime+':')
		f.write('Google Speech Recognition could not understand audio\n')
		f.close()		
	except speech_recognition.RequestError as e:
		text=""
    		print("Could not request results from Google Speech Recognition service; {0}".format(e))		
		
	
	voice()

#voice()

