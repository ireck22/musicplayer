import wx
import MplayerCtrl as mpc
import os
import wx.lib.buttons as buttons


class Frame(wx.Frame):
    def __init__(self, parent, id, title, mplayer, media_file):
        wx.Frame.__init__(self, parent, id, title)
        
        
        self.mpc = mpc.MplayerCtrl(self, -1, mplayer, media_file)
        self.Bind(mpc.EVT_PROCESS_STARTED, self.on_process_started)
        self.Bind(mpc.EVT_MEDIA_STARTED, self.on_media_started)
        self.Bind(mpc.EVT_MEDIA_FINISHED, self.on_media_finished)
        self.Bind(mpc.EVT_PROCESS_STOPPED, self.on_process_stopped)
        
        #self.Bind(mpc.EVT_STDERR,self.on_stderr)
        self.Show()

    def on_process_started(self, evt):
        print 'Process started'
    def on_media_started(self, evt):
        print 'Media started'
        print 'volume'
        #self.mpc.SetProperty('volume', 90)
        ANS_ERROR=PROPERTY_UNAVAILABLE
        volume = self.mpc.volume
        stream_pos = self.mpc.stream_pos
        # now set a property
        self.mpc.volume = 50
        self.mpc.time_pos = 20
        # now de/increase a property
        self.mpc.volume -= 10
        self.mpc.time_pos += 5

    def on_media_finished(self, evt):
        print 'Media finished'
        self.mpc.Quit()
    def on_process_stopped(self, evt):
        print 'Process stopped'
        os_exit()
    def on_stderr(self,evt):
        print 'oh oh some errors:'
        print '==>', evt.data
   


if __name__ == '__main__':
    app = wx.App(redirect=False)
    #result='https://www.youtube.com/embed/qIF8xvSA0Gw'
    #frame = Frame(None, -1, 'Hello MplayerCtrl', 'C:\Users\jacky\Desktop\MPlayer-rtm-svn-31170\mplayer.exe','test2.mkv')
    frame = Frame(None, -1, 'Hello MplayerCtrl', 'C:\Users\jacky\Desktop\MPlayer-rtm-svn-31170\mplayer.exe','love.mkv')
    app.MainLoop()