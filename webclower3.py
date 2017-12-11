#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
import lxml
import json
import os
import speech_recognition
import pyaudio
import pygame
import time

"""
r=speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
	audio=r.listen(source)
	#audio=r.record(source)
text = ""
text = r.recognize_google(audio, language='zh-TW')

#result2=os.popen("key.py").read()
result2=os.popen("key.py",'r')
print result2
key="ok音樂"
key2=key.decode('utf-8')	
"""


#while text==key2:
os.system('key.py')		
	
pygame.mixer.init()
#pygame.mixer.music.load("/var/www/html/video3/music/chosesong.mp3")
pygame.mixer.music.load("D:\py\music\chosesong.mp3")
pygame.mixer.music.play()
time.sleep(1)



r=speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
	audio=r.listen(source)
	#audio=r.record(source)
text = ""
text = r.recognize_google(audio, language='zh-TW')
#text = r.recognize_google(audio, language='en-US')

			
time.sleep(2)
r1=requests.get('https://www.youtube.com/results?search_query='+text)
soup=BeautifulSoup(r1.text,'lxml')
#print soup
#解析

#title=soup.select('a')
title=soup.find_all('div') #找所有的div區塊
#	print title
for d in title:
	if d.find('a'):        #再從div找a裡面的href  
		result='!'+d.find('a')['href']
		print result
	



