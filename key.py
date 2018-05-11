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
import song


def start():
	 while True: 
		r=speech_recognition.Recognizer()
		with speech_recognition.Microphone() as source:
			audio=r.listen(source)
			#audio=r.record(source)
		text = ""
		try:
			text = r.recognize_google(audio, language='zh-TW')

			#text2=text.encode('utf_8')
			print text
	

			key="ok音樂"
			key2=key.decode('utf-8')

			while text == key2:
				#song.found()
				sys.exit()
	
		except speech_recognition.UnknownValueError:
    			print("Google Speech Recognition could not understand audio")
		except speech_recognition.RequestError as e:
    			print("Could not request results from Google Speech Recognition service; {0}".format(e))
	


start()	

