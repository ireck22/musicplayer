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

q=Queue.Queue()
q2=Queue.Queue()
#fp=open("url.txt","w")

def re1():
	#result=os.popen("python webcrawler3.py").read()
	#res2=[]
	#res2.append(result)
	#res3=res2[0].split('!')
	#print res3[41]  #為了除復跑而用read()
	result = subp.Popen(["python", "webcrawler3.py"], stdout=subp.PIPE, stdin=subp.PIPE).communicate()[0]
	result2=result.split('!')
	#print result2[41]  #supprocess的
	re2=result2[41].split("v=")
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
	print "start"
	rescro=os.getpid()
	q2.put(rescro)
	crow.voice()
	lock2.release()

def mo():
	time.sleep(17)
	result=""
	while result !=[]:
		result=os.popen("pidof omxplayer.bin").readlines()
		print result
	print "ok"
	result2=q2.get()
	print result2
	result3=str(result2)
	os.system("sudo kill -9 "+result3)


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


