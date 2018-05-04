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
def voice():
	keyword=("切割").decode('utf-8')
	text = ""
	#time.sleep()
	while text != keyword:
		
		result=os.popen("pidof omxplayer.bin").readlines()
                print result
                if result==[]:
                        sys.exit()

		r=speech_recognition.Recognizer()
		with speech_recognition.Microphone() as source:
			audio=r.listen(source)
			#audio=r.record(source)
		try:
			text = r.recognize_google(audio, language='zh-TW')
			print text
			time.sleep(1)
			if text=="":
				print "null"
			if text!=keyword:
				song.error()
		except speech_recognition.UnknownValueError:
   			 print("Google Speech Recognition could not understand audio")
		except speech_recognition.RequestError as e:
    			print("Could not request results from Google Speech Recognition service; {0}".format(e))		
		
		
	os.system("sudo killall -9 omxplayer.bin")

#voice()

