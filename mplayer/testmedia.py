import wx
import MplayerCtrl as mpc

class Frame(wx.Frame):
    def __init__(self, parent, id, title, mplayer, media_file):
        wx.Frame.__init__(self, parent, id, title)

        self.mpc = mpc.MplayerCtrl(self, -1, mplayer, media_file)
        self.mpc.Bind(wx.EVT_KEY_DOWN, self.key_down)
        self.Show()

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
    app = wx.App(redirect=False)
    #result='https://www.youtube.com/embed/qIF8xvSA0Gw'
    #frame = Frame(None, -1, 'Hello MplayerCtrl', 'C:\Users\jacky\Desktop\MPlayer-rtm-svn-31170\mplayer.exe','test2.mkv')
    frame = Frame(None, -1, 'Hello MplayerCtrl', 'C:\Users\jacky\Desktop\MPlayer-rtm-svn-31170\mplayer.exe','love.mkv')
    app.MainLoop()