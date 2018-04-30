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
import monitor
import song
import sys

"""
STDERR = sys.stderr
def excepthook(*args):
    print >> STDERR, 'caught'
    print >> STDERR, args
"""
#sys.excepthook = excepthook

q=Queue.Queue()
q2=Queue.Queue()
#fp=open("url.txt","w")

def re1():
	"""
	os.system("python webcrawler3.py")
	print "ready"
	main()
	"""
	#result=os.popen("python webcrawler3.py").read()
	#res2=[]
	#res2.append(result)
	#res3=res2[0].split('!')
	#print res3[41]  #為了除復跑而用read()
	result = subp.Popen(["python", "webcrawler3.py"], stdout=subp.PIPE, stdin=subp.PIPE).communicate()[0]
	
	#result2=result.split('!')
	#print result2[41]  #supprocess的
	#re2=result2[41].split("v=")
	#print re2[1] #網址截斷測試
	#re3="https://www.youtube.com/embed/"+re2[1]
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
	main()
	#lock.release()
		
	
def cv():
	global lock
        lock2=threading.Lock()
	lock2.acquire()
	time.sleep(17)	
	print "start"
	rescro=os.getpid()
	q2.put(rescro)
	crow.voice()
	lock2.release()

def mo():
	#time.sleep(31) #三線呈
	time.sleep(17)  
	"""
	global lock
        lock3=threading.Lock()
        lock3.acquire()
	"""
	result=""
	while result !=[]:
		result=os.popen("pidof omxplayer.bin").readlines()
		#print result
	print "ok"
	result2=q2.get()
	print result2
	result3=str(result2)
	os.system("sudo kill -9 "+result3)
	#lock3.release()

def main():
	main_thread=threading.Thread(target=re1,name='re')
	Thread2=threading.Thread(target=player,name='player')
	Thread3=threading.Thread(target=cv,name='cv')
	Thread4=threading.Thread(target=mo,name='mo')
	main_thread.start()
	main_thread.join()
	Thread2.start()
	Thread3.start()	
	#Thread4.start()	
	
	"""
	threads=[]	
	#threads.append(added_thread)
	threads.append(Thread2)
	threads.append(Thread3)	
	#threads.append(Thread4)
	"""

	while Thread2.is_alive() or  Thread3.is_alive() or Thread4.is_alive():
		time.sleep(1) 
	#main()

if __name__=='__main__':
	main()

