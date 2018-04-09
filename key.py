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



def start():
	 
	r=speech_recognition.Recognizer()
	with speech_recognition.Microphone() as source:
		audio=r.listen(source)
		#audio=r.record(source)
	text = ""
	text = r.recognize_google(audio, language='zh-TW')

	#text2=text.encode('utf_8')
	print text


	key="ok音樂"
	key2=key.decode('utf-8')

	while text == key2:
		sys.exit()
	
	start()

start()	

