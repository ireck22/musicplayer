#!/usr/bin/python
# -*- coding: utf8 -*-
# coding: utf8
import subprocess
import os
import pyaudio
import pygame
import time
import threading



fp=open('url.txt','r')

result=os.popen("pidof vlc").readlines()
len(result[0])
result2=len(result[0])
print result2

if result2==5:
        restxt=fp.read()
        print restxt
        #os.system('youtube-dl -f 22 -o "music/%(title)s.%(ext)s" '+restxt)
        res3=os.popen('youtube-dl -f 22 -o "music/%(title)s.%(ext)s" '+restxt).readlines()
        #print res3[3]
        res4=res3[3].split(":")
        #res4=res3[3].split("]") #已下載
        print res4[1]
        #os.system("vlc "+res4[1])

fp.close()

