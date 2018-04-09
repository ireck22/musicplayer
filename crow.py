#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
import pyaudio
import pygame
import time
import threading
import speech_recognition

def voice():
	r=speech_recognition.Recognizer()
	with speech_recognition.Microphone() as source:
		audio=r.listen(source)
		#audio=r.record(source)
	text = ""
	text = r.recognize_google(audio, language='zh-TW')

	#if text is None:
	#	voice()

	print text
	keyword="切割"
	keyword2=keyword.decode('utf-8')


	while text==keyword2:
 		os.system("sudo killall -9 vlc")
  		#os.system("python main.py")
		time.sleep(5)
		voice()
	voice()

voice()

