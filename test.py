#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess as subp
import time

#i=0
#for i in range(10):
#	print "%d進呈id:%d"%(i,os.getpid())


proc = subp.Popen(["python", "webcrawler3.py"], stdout=subp.PIPE, stdin=subp.PIPE).communicate()[0]
 
qwe=proc.split('!')
print qwe[41]


"""

res=os.popen("python webcrawler3.py").read()
res2=[]
res2.append(res)
#print res2[0]
res3=res2[0].split('!')
print res3[41]
"""
