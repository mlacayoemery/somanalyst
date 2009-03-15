import wx

def OnTaskBarRight(event):
    app.ExitMainLoop()

class MyApp(wx.App):
    
    def OnInit(self):
       frame = MyFrame("Abstract Map - Manager", (0, 0), (800,600))
       frame.Show()
       self.SetTopWindow(frame)
       #frame.Maximize(True)
       #frame.SetIcon(wx.Icon("icon.bmp", wx.BITMAP_TYPE_ICO))
       return True
    
class MyFrame(wx.Frame):
    
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        panel = wx.Panel(self, -1)

        wx.StaticText(panel, -1, "Collections",(0, 0))

        sampleList = ['collection1','collection2','collection3']

        listBox = wx.ListBox(panel, -1, (0, 15), (150, 100), sampleList, 
                wx.LB_SINGLE)
        listBox.SetSelection(0)

        self.button = wx.Button(panel, -1, "Export", pos=(152, 41))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

        self.button = wx.Button(panel, -1, "Rename", pos=(152, 64))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

        self.button = wx.Button(panel, -1, "Delete", pos=(152, 87))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

        self.button = wx.Button(panel, -1, "Import", pos=(152, 17))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

        wx.StaticText(panel, -1, "Completed Projects",(233, 0))        

        sampleList2 = ['project1','project2','project3']
        listBox = wx.ListBox(panel, -1, (233, 15), (200, 100), sampleList2, 
                wx.LB_SINGLE)
        listBox.SetSelection(0)

        self.button = wx.Button(panel, -1, "Copy", pos=(435, 17))

        self.button = wx.Button(panel, -1, "Rename", pos=(435, 41))

        self.button = wx.Button(panel, -1, "Delete", pos=(435, 64))

        wx.StaticText(panel, -1, "Projects Index (",(0, 270))        

        sampleList2 = ['<select a project>','project1','project2','project3']
        listBox = wx.ListBox(panel, -1, (0, 285), (200, 100), sampleList2, 
                wx.LB_SINGLE)
        listBox.SetSelection(0)

        self.button = wx.Button(panel, -1, "New", pos=(202, 287))

        self.button = wx.Button(panel, -1, "Rename", pos=(202, 311))

        self.button = wx.Button(panel, -1, "Delete", pos=(202, 334))
        wx.CheckBox(panel, -1, "include completed)", (78, 269), (150, 16))

        wx.StaticText(panel, -1, "Base Collection",(0, 387))    
               
        wx.CheckBox(panel, -1, "Title", (0, 422), (70, 16))
        wx.CheckBox(panel, -1, "Abstract", (0, 437), (70, 16))
        wx.CheckBox(panel, -1, "Full text", (0, 452), (70, 16))
        wx.CheckBox(panel, -1, "Keywords", (0, 467), (70, 16))

        wx.Choice(panel, -1, (0, 400), choices=sampleList)
        self.button = wx.Button(panel, -1, "Insert", pos=(202, 400))
        self.button = wx.Button(panel, -1, "Export", pos=(202, 423))

        wx.StaticText(panel, -1, "Collection to Index",(90, 387))    
        wx.Choice(panel, -1, (90, 400), choices=sampleList)       
        wx.CheckBox(panel, -1, "Title", (90, 422), (70, 16))
        wx.CheckBox(panel, -1, "Abstract", (90, 437), (70, 16))
        wx.CheckBox(panel, -1, "Full text", (90, 452), (70, 16))
        wx.CheckBox(panel, -1, "Keywords", (90, 467), (70, 16))

    def OnClick(self, event):
        self.button.SetLabel("Clicked")        
        
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

