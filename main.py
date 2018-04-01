#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
import pyaudio
import pygame
import time
import threading
import crow

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
	os.system("vlc "+re3)
"""
def print_time( thre, delay):
	count = 0
	for i in range (1,thre):  
		time.sleep(delay)
		count += i
		print "%s: %d" % ( thre, count )	
"""

def cv():
	crow.voice()

#thread1=re1()
#thread2=crow.voice

def main():
	added_thread=threading.Thread(target=re1,name='re')
	Thread2=threading.Thread(target=cv,name='cv')
	added_thread.start()
	added_thread.join()
	Thread2.start()
	Thread2.join()
	
	print 'all done\n'
if __name__=='__main__':
	main()


