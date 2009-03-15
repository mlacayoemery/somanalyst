import xml.dom.minidom, string
import wx

TEXT_NODE = xml.dom.minidom.DocumentType.TEXT_NODE



#gets value from a leaf node list
#skips text node leafs
def getXMLValue(nodes):
    #ignore preceeding whitespace and get value
    if nodes[0].nodeType==TEXT_NODE:
        nodes.pop(0)
    node=nodes.pop(0).childNodes
    if len(node)==0:
        return None
    else:
        return node[0].nodeValue

class Dispatcher:
    "Dispatches functions calls allowing events to be bound to "
    def __init__(self):
        self.dispatch={}
        self.dispatch["MessageDialog"]=MessageDialog

    def wrap(self,id,function,*parameters):
        "Returns a constructor sequence for a function"
        return (id, function, parameters)

    def unwrap(self,function,parameters):
        "Constructs a function from a constructor sequence"
        return self.dispatch[function](parameters)
        

class MessageDialog:
    def __init__(self, (otherself, title="Title", message="Message Dialog Text", style=wx.OK | wx.ICON_INFORMATION)):
        self.otherself=otherself
        self.message=message
        self.title=title
        self.style=style

    def __call__(self,event):
        dlg = wx.MessageDialog(self.otherself,
                               self.message,
                               self.title,
                               self.style)
        dlg.ShowModal()
        dlg.Destroy()


class MyFrame(wx.Frame):
    def __init__(self,title="My Frame", dimensions=(300,300), menuBar=None, events=None):
        wx.Frame.__init__(self, None, -1, title, size=dimensions)
        panel = wx.Panel(self,-1)
        self.SetMenuBar(menuBar)
        
        for id,function,parameters in events:
            wx.EVT_MENU(self, id, dispatch.unwrap(function,[self]+parameters))
##        panel.Bind(wx.EVT_MOTION, self.OnMove)
##        wx.StaticText(panel,-1, "Pos:", pos=(10,12))
##        self.posCtrl = wx.TextCtrl (panel, -1, "", pos=(40,10))

    def Dispatcher(self,function):
        try:
            return self.dispatch[function]
        except KeyError:
            return None

    def TimeToQuit(self, event):
        self.Close(True)

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))
        
if __name__ == "__main__":
    dispatch=Dispatcher()
    #parse document, get root node
    doc = xml.dom.minidom.parse("D:/users/martin/somanalyst/scripts/beta/SOMgui.xml")
    rootNode = doc.childNodes
    if rootNode[0].nodeType==TEXT_NODE:
        rootNode.pop(0)
    rootNode=rootNode.pop(0)

    #skip to window
    windowNodes=rootNode.childNodes
    if windowNodes[0].nodeType==TEXT_NODE:
        windowNodes.pop(0)
    windowNodes=windowNodes.pop(0).childNodes

    #get title    
    app = wx.PySimpleApp()
    XMLtitle=getXMLValue(windowNodes)

    #get size
    if windowNodes[0].nodeType==TEXT_NODE:
        windowNodes.pop(0)
    dimNode=windowNodes.pop(0).childNodes
    XMLdimensions=(int(getXMLValue(dimNode)),int(getXMLValue(dimNode)))

    #get menu bar
    id=0
    if windowNodes[0].nodeType==TEXT_NODE:
        windowNodes.pop(0)
    menuBarNode=windowNodes.pop(0).childNodes
    menuBar = wx.MenuBar()
    events=[]
    for i in range(len(menuBarNode)):
        node=menuBarNode.pop(0)
        if node.nodeType!=TEXT_NODE:
            menuNode=node.childNodes
            menu=wx.Menu()
            name=getXMLValue(menuNode)
            for j in range(len(menuNode)):
                itemNode=menuNode.pop(0)
                if itemNode.localName=="ITEM":
                    menu.Append(id, getXMLValue(itemNode.childNodes))
                    if itemNode.childNodes[0].nodeType=TEXT_NODE:
                        itemNode.childNodes.pop(0)
                    eventNode=itemNode.childNodes.pop(0).childNodes
                    if eventNode[0].localName=="MESSAGEDIALOG":
                        title=getXMLValue(eventNode[0].childNodes)
                        text=getXMLValue(eventNode[0].childNodes)
                        events.append(dispatch.wrap(id, "MessageDialog",[title,text]))
                    id+=1
                elif itemNode.localName=="SEPARATOR":
                    menu.AppendSeparator()
            menuBar.Append(menu, name)

    ##set parameters and activate GUI
    frame = MyFrame(title=XMLtitle,dimensions=XMLdimensions,menuBar=menuBar,events=events)
    frame.Show(True)
    app.MainLoop()

##ID_ABOUT = 101
##ID_EXIT  = 102
##ID_HELP = 103
##ID_OPEN = 104
##ID_SAVE = 105
##ID_CLOSE = 106
##
##class MyFrame(wx.Frame):
##    def __init__(self, parent, ID, title):
##        wx.Frame.__init__(self, parent, ID, title,
##                         wx.DefaultPosition, wx.Size(800, 600))
##        self.CreateStatusBar()
##        #self.SetStatusText("This is the statusbar")
##
##        menu = wx.Menu()
##
##        menu.Append(ID_OPEN, "&Open", "Open a project")
##        menu.Append(ID_SAVE, "&Save", "Save a project")
##        menu.Append(ID_CLOSE, "&Close", "Close a project")
##
##        menu.AppendSeparator()
##        menu.Append(ID_EXIT, "E&xit", "Terminate the program")
##
##        menuBar = wx.MenuBar()
##        menuBar.Append(menu, "&File");
##
##        menu = wx.Menu()
##
##        menu.Append(ID_HELP, "&Help Contents", "Help with SOM Analyst")        
##        menu.AppendSeparator()
##        menu.Append(ID_ABOUT, "&About",
##                    "More information about this program")
##        menuBar.Append(menu, "&Help");
##      
##
##        self.SetMenuBar(menuBar)
##
##        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)
##        wx.EVT_MENU(self, ID_EXIT,  self.TimeToQuit)
##        wx.EVT_MENU(self, ID_HELP, self.OnHelp)
##
##    def OnAbout(self, event):
##        dlg = wx.MessageDialog(self, "created by:\n"
##                               "\tMartin Lacayo-Emery\n"
##                               "\tGeography Department\n"
##                               "\tSan Diego State University\n"
##                               "\tlacayo@rohan.sdsu.edu",
##                              "About SOM Analyst", wx.OK | wx.ICON_INFORMATION)
##        dlg.ShowModal()
##        dlg.Destroy()
##
##    def OnHelp(self, event):
##        dlg = wx.MessageDialog(self, "This feature is in development.",
##                              "Help Contenets", wx.OK | wx.ICON_INFORMATION)
##        dlg.ShowModal()
##        dlg.Destroy()
##
##    def TimeToQuit(self, event):
##        self.Close(True)
##
##class MyApp(wx.App):
##    def OnInit(self):
##        frame = MyFrame(None, -1, "SOM Analyst")
##        frame.Show(True)
##        self.SetTopWindow(frame)
##        return True
##
##app = MyApp(0)
##app.MainLoop()
    
