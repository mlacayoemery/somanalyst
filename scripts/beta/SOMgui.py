import wx

def OnTaskBarRight(event):
    app.ExitMainLoop()

class MyApp(wx.App):
    
    def OnInit(self):
       frame = MyFrame("SOM Analyst", (0, 0), (0,0))
       frame.Show()
       self.SetTopWindow(frame)
       frame.Maximize(True)
       frame.SetIcon(wx.Icon("icon.bmp", wx.BITMAP_TYPE_ICO))
       return True
    
class MyFrame(wx.Frame):
    
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        menuFile = wx.Menu()
        menuFile.Append(1, "&About...")
        menuFile.AppendSeparator()
        menuFile.Append(2, "E&xit")
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")

        menu=wx.Menu()
        menu.Append(3,"Normalize")
        menuBar.Append(menu, "&Data")
        menu=wx.Menu()
        menu.Append(4,"Initialize SOM")
        menuBar.Append(menu, "&Computation")
        menu=wx.Menu()
        menu.Append(5,"SOM to Shapefile")
        menuBar.Append(menu, "&Visualization")
        menu=wx.Menu()
        menu.Append(6,"SOM Creation")
        menuBar.Append(menu, "&Wizards")
        menu=wx.Menu()
        menu.Append(7,"SOM")
        menuBar.Append(menu, "&Help")

        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")
        self.Bind(wx.EVT_MENU, self.OnAbout, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=2)
        
    def OnQuit(self, event):
        self.Close()
         
    def OnAbout(self, event):
        wx.MessageBox("Copyright 2008 Martin Lacayo\n\nThanks to my thesis committee:\nAndr\xe9 Skupin, Serge Rey, Carl Eckberg\n\n"+
                      "For futher information visit:\nhttp://somanalyst.hopto.org","About SOM Analyst",
                      wx.OK | wx.ICON_INFORMATION, self)
                
if __name__ == '__main__':
    app = MyApp(False)

##    #setup icon object
##    
##
##    #setup taskbar icon
##    tbicon = wx.TaskBarIcon()
##    tbicon.SetIcon(icon, "I am an Icon")
##    #add taskbar icon event
##    wx.EVT_TASKBAR_RIGHT_UP(tbicon, OnTaskBarRight)

    app.MainLoop()

