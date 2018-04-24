#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
import pyaudio
import pygame
import time
import threading
import Queue
import crow2
import monitor
import song

q=Queue.Queue()
#fp=open("url.txt","w")

def re1():
	result=os.popen("python webcrawler3.py").readlines()
	#print result[40]
	re2=result[40].split("v=")
	#print re2[1] #網址截斷測試
	re3="https://www.youtube.com/embed/"+re2[1]
	print re3
	q.put(re3)
	song.found()	

def player():
	global lock
	lock=threading.Lock()
	lock.acquire()
	res=q.get()
	os.system("omxplayer `youtube-dl -g -f 22 "+res+"`")	
	print res
	main()
	lock.release()	
	
def cv():
	global lock
	lock2=threading.Lock()
	lock2.acquire()
	time.sleep(5)
	print "22"
	crow2.voice()
	lock2.release()
def mo():
	monitor.mon()

def main():
	added_thread=threading.Thread(target=re1,name='re')
	Thread2=threading.Thread(target=player,name='player')
	Thread3=threading.Thread(target=cv,name='cv')
	Thread4=threading.Thread(target=mo,name='mo')
	added_thread.start()
	added_thread.join()
	Thread2.start()
	#Thread2.join()
	Thread3.start()	
	Thread4.start()	

if __name__=='__main__':
	main()


