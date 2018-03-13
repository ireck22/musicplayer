import MplayerCtrl as mpc
import wx

class Frame(wx.Frame):
    def __init__(self, parent, id, size=(-1,-1)):
        wx.Frame.__init__(self, parent, id, size=size)
        self.mpc = mpc.MplayerCtrl(self, -1, 'C:\Users\jacky\Desktop\MPlayer-rtm-svn-31170\mplayer.exe','love.mkv')

        self.Bind(mpc.EVT_MEDIA_STARTED, self.media_started)
        self.Bind(mpc.EVT_MEDIA_FINISHED, self.media_finished)
        self.Bind(mpc.EVT_PROCESS_STARTED, self.process_started)
        self.Bind(mpc.EVT_PROCESS_STOPPED, self.process_stopped)
        self.mpc.Bind(wx.EVT_KEY_DOWN, self.key_down)

        self.Center()
        self.Show()

    def media_started(self, evt):
        print '----------> Media started'
    def media_finished(self, evt):
        print '----------> Media finished'
    def process_started(self, evt):
        print '----------> Process started'
        self.mpc.Loadfile(u'testmovie.mpg')
    def process_stopped(self, evt):
        print '----------> Process stopped'

    def key_down(self, evt):
        k = evt.GetKeyCode()
        if k in (43, 45) and self.mpc.playing:
            volume = self.mpc.volume
            if k == 43:
                if not volume > 95:
                    self.mpc.volume += 5
            elif k == 45:
                if not volume <= 5:
                    self.mpc.volume -= 5
        evt.Skip()


if __name__ == '__main__':
    app = wx.App()
    f = Frame(None, -1)
    app.MainLoop()