#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess as subp
import os
import pyaudio
import pygame
import time
import threading
import Queue
import crow
import song
import sys




q=Queue.Queue()
q2=Queue.Queue()
#fp=open("url.txt","w")

def re1():
	"""
	os.system("python webcrawler3.py")
	print "ready"
	main()
	"""
	
	result = subp.Popen(["python", "webcrawler3.py"], stdout=subp.PIPE, stdin=subp.PIPE).communicate()[0]	
	print result
	q.put(result)
	song.found()	

def player():
	"""
	global lock
	lock=threading.Lock()
	lock.acquire()
	"""
	res=q.get()
	os.system("omxplayer `youtube-dl -g -f 22 "+res+"`")	
	print res
	#main()
	#lock.release()
		
	
def cv():
	global lock
        lock2=threading.Lock()
	lock2.acquire()
	time.sleep(17)	
	#print "start"
	#rescro=os.getpid()
	#q2.put(rescro)
	#os.system("python crow.py")
	crow.voice()
	lock2.release()


def main():
	while True:
		main_thread=threading.Thread(target=re1,name='re')
		Thread2=threading.Thread(target=player,name='player')
		Thread3=threading.Thread(target=cv,name='cv')
		main_thread.start()
		main_thread.join()
		Thread2.start()
		Thread3.start()

		while Thread2.is_alive() or  Thread3.is_alive():
			time.sleep(2)
		print "yooo" #除錯用

if __name__=='__main__':
	main()

