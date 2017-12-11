#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
import pyaudio
import pygame
import time
import threading

def re1():
	result=os.popen("webclower3.py").readlines()
	#print result[40]
	re2=result[40].split("v=")
	#print re2[1] #網址截斷測試
	re3="https://www.youtube.com/embed/"+re2[1]
	print re3
	#os.system("vlc "+re3)

def print_time( thre, delay):
	count = 0
	for i in range (1,thre):  
		time.sleep(delay)
		count += i
		print "%s: %d" % ( thre, count )	


thread1=re1()
thread2=print_time(6, 2)

#try:
re.search(cookieKey +'\w+',mf)
thread1.start()
thread2.start()
#except:
  # print "Error: unable to start thread"


threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"




