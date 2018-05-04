#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
import pyaudio
import pygame
import time


def found():
	pygame.mixer.init()
	pygame.mixer.music.load("/home/pi/musicplayer/music/songfound.mp3")
	pygame.mixer.music.play()
	time.sleep(2)



def error():
        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/musicplayer/music/voiceerror.mp3")
        pygame.mixer.music.play()
        time.sleep(3)




