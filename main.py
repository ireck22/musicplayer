#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
import pyaudio
import pygame
import time
import threading
import Queue
import crow

q=Queue.Queue()

fp=open("url.txt","w")
#crow.voice()

def re1():
	result=os.popen("python webcrawler3.py").readlines()
	#print result[40]
	re2=result[40].split("v=")
	#print re2[1] #網址截斷測試
	re3="https://www.youtube.com/embed/"+re2[1]
	fp.write(re3)
	fp.close()
	print re3
	#os.system("vlc "+re3)
	q.put(re3)

def player():
	res=q.get()
	os.system("omxplayer `youtube-dl -g -f 22 "+res+"`")	
	print res

def cv():
	print 333
	crow.voice()

def main():
	added_thread=threading.Thread(target=re1,name='re')
	Thread2=threading.Thread(target=player,name='player')
	Thread3=threading.Thread(target=cv,name='cv')
	added_thread.start()
	added_thread.join()
	Thread2.start()
	#Thread2.join()
	Thread3.start()	

if __name__=='__main__':
	main()


