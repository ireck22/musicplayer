#!/usr/bin/python
# -*- coding: utf-8 -*-

import vlc
import time

instance = vlc.Instance()

#Create a MediaPlayer with the default instance
player = instance.media_player_new()

#Load the media file
media = instance.media_new('test.mp3')

#Add the media to the player
player.set_media(media)

#Play for 10 seconds then exit
player.play()
time.sleep(10)