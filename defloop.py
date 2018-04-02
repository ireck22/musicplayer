#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import threading
import time
import os
import sys

sum=0

def loop():
	global sum
	#a=1
	#print a

	for i in range(1,10):
		sum+=i
		print sum
		#print i
	"""
	if a==1:
		res()
	"""
	if sum==180:
		res()
	time.sleep(1)	
	loop()   #再次呼叫loop

def res():
	os.system('pause')
	#os._exit()
	sys.exit()  #終止程序
	
loop()
