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
import song	

os.system('python /home/pi/musicplayer/key.py')
	
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/musicplayer/music/chosesong.mp3")
#pygame.mixer.music.load("D:\py\music\chosesong.mp3")
pygame.mixer.music.play()
time.sleep(0.5)



r=speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
	audio=r.listen(source)
	#audio=r.record(source)
text = ""
try:	
	text = r.recognize_google(audio, language='zh-TW')

except speech_recognition.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except speech_recognition.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

resusp=[]			
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
		#print result
		resusp.append(result)		

re2=resusp[41]
#print re2
re3=re2.split('v=')
#print re3[1]
re4="https://www.youtube.com/embed/"+re3[1]
print re4
#song.found()
#os.system("omxplayer `youtube-dl -g -f 22 "+re4+"`")

