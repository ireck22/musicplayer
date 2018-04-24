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
	keyword=("切割").decode('utf-8')
	text = ""
	time.sleep(20)
	while text != keyword:
		r=speech_recognition.Recognizer()
		with speech_recognition.Microphone() as source:
			audio=r.listen(source)
			#audio=r.record(source)
		text = r.recognize_google(audio, language='zh-TW')
		print text
		time.sleep(1)

	os.system("sudo killall -9 omxplayer.bin")

#voice()

