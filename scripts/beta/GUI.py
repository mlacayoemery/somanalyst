import wx, os


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.rawTitle = wx.StaticText(self, -1, "Raw Data")
        self.preTitle = wx.StaticText(self, -1, "Preprocessed Data")
        self.proTitle = wx.StaticText(self, -1, "Projected Data")
        self.rawList = wx.ListBox(self, -1, choices=[], style=wx.LB_EXTENDED)
        self.rawListPaths = {}
        self.rawAdd = wx.Button(self, wx.NewId(), "Add")
        self.rawRen = wx.Button(self, wx.NewId(), "Rename")
        self.rawDel = wx.Button(self, wx.NewId(), "Delete")
        self.toPre = wx.Button(self, wx.NewId(), "->")
        self.fromPre = wx.Button(self, wx.NewId(), "<-")
        self.rawExport = wx.Button(self, wx.NewId(), "Export")
        self.mergeType = wx.RadioBox(self, -1, "", choices=["Vertical", "Horizontal"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.rawMerge = wx.Button(self, wx.NewId(), "Merge")
        self.subStartLabel = wx.StaticText(self, -1, "Start")
        self.subStart = wx.TextCtrl(self, -1, "0")
        self.subStopLabel = wx.StaticText(self, -1, "Stop")
        self.subStop = wx.TextCtrl(self, -1, "")
        self.subStepLabel = wx.StaticText(self, -1, "Step")
        self.subStep = wx.TextCtrl(self, -1, "1")
        self.rawSubset = wx.Button(self, wx.NewId(), "Subset")
        self.preList = wx.ListBox(self, -1, choices=[])
        self.preAdd = wx.Button(self, wx.NewId(), "Add")
        self.preRen = wx.Button(self, wx.NewId(), "Rename")
        self.preDel = wx.Button(self, wx.NewId(), "Delete")
        self.preExport = wx.Button(self, wx.NewId(), "Export")
        self.projMeasure = wx.RadioBox(self, -1, "", choices=["Cosine", "Euclidean"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.project = wx.Button(self, wx.NewId(), "Project")
        self.initTypeLabel = wx.StaticText(self, -1, "type")
        self.initType = wx.ComboBox(self, -1, choices=["Linear", "Random"], style=wx.CB_DROPDOWN)
        self.xDimLabel = wx.StaticText(self, -1, "x dim")
        self.xDim = wx.TextCtrl(self, -1, "")
        self.yDimLabel = wx.StaticText(self, -1, "y dim")
        self.yDim = wx.TextCtrl(self, -1, "")
        self.initSOM = wx.Button(self, wx.NewId(), "Initial SOM")
        self.proList = wx.ListBox(self, -1, choices=[])
        self.proAdd = wx.Button(self, wx.NewId(), "Add")
        self.proRen = wx.Button(self, wx.NewId(), "Rename")
        self.proDel = wx.Button(self, wx.NewId(), "Delete")
        self.proShape = wx.Button(self, wx.NewId(), "Shapefile")
        self.proExport = wx.Button(self, wx.NewId(), "Export")
        self.trajStartLabel = wx.StaticText(self, -1, "Start")
        self.trajStart = wx.TextCtrl(self, -1, "0")
        self.trajStopLabel = wx.StaticText(self, -1, "Stop")
        self.trajStop = wx.TextCtrl(self, -1, "")
        self.trajStepLabel = wx.StaticText(self, -1, "Step")
        self.trajStep = wx.TextCtrl(self, -1, "1")
        self.trajOffsetLabel = wx.StaticText(self, -1, "Offset")
        self.trajOffset = wx.TextCtrl(self, -1, "0")
        self.trajRepeatLabel = wx.StaticText(self, -1, "Repeat")
        self.trajRepeat = wx.TextCtrl(self, -1, "1")
        self.trajectory = wx.Button(self, wx.NewId(), "Trajectory")
        self.initTitle = wx.StaticText(self, -1, "Initial SOM")
        self.trainTitle = wx.StaticText(self, -1, "Trained SOM")
        self.shapeTitle = wx.StaticText(self, -1, "Shapefiles")
        self.initList = wx.ListBox(self, -1, choices=[])
        self.initAdd = wx.Button(self, wx.NewId(), "Add")
        self.initRen = wx.Button(self, wx.NewId(), "Rename")
        self.initDel = wx.Button(self, wx.NewId(), "Delete")
        self.toTrain = wx.Button(self, wx.NewId(), "->")
        self.fromTrain = wx.Button(self, wx.NewId(), "<-")
        self.initExport = wx.Button(self, wx.NewId(), "Export")
        self.trainLenLabel = wx.StaticText(self, -1, "rlen")
        self.trainLen = wx.TextCtrl(self, -1, "")
        self.trainAlphaLabel = wx.StaticText(self, -1, "alpha")
        self.trainAlpha = wx.TextCtrl(self, -1, "0.04")
        self.trainRadiusLabel = wx.StaticText(self, -1, "radius")
        self.trainRadius = wx.TextCtrl(self, -1, "")
        self.trainMeasure = wx.RadioBox(self, -1, "", choices=["Cosine", "Euclidean"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.train = wx.Button(self, wx.NewId(), "Train")
        self.trainList = wx.ListBox(self, -1, choices=[])
        self.trainAdd = wx.Button(self, wx.NewId(), "Add")
        self.trainRen = wx.Button(self, wx.NewId(), "Rename")
        self.trainDel = wx.Button(self, wx.NewId(), "Delete")
        self.trainShape = wx.Button(self, wx.NewId(), "Shapefile")
        self.trainExport = wx.Button(self, wx.NewId(), "Export")
        self.clusteringLabel = wx.StaticText(self, -1, "Clustering")
        self.dominance = wx.Button(self, wx.NewId(), "Dominance")
        self.kClustersLabel = wx.StaticText(self, -1, "clusters")
        self.kClusters = wx.TextCtrl(self, -1, "")
        self.kLenLabel = wx.StaticText(self, -1, "rlen")
        self.kLength = wx.TextCtrl(self, -1, "")
        self.Kmeans = wx.Button(self, wx.NewId(), "K-means")
        self.shapeList = wx.ListBox(self, -1, choices=[])
        self.shapeRen = wx.Button(self, wx.NewId(), "Rename")
        self.shapeDel = wx.Button(self, wx.NewId(), "Delete")
        self.shapeExport = wx.Button(self, wx.NewId(), "Export")
        self.systemLabel = wx.StaticText(self, -1, "SOM Analyst System")
        self.load = wx.Button(self, wx.NewId(), "Load")
        self.save = wx.Button(self, wx.NewId(), "Save")
        self.help = wx.Button(self, wx.NewId(), "Help")
        self.about = wx.Button(self, wx.NewId(), "About")
        self.copyright = wx.StaticText(self, -1, "\n (c) 2008\n Martin Lacayo\n Geography\n SDSU")

        #raw data events
        wx.EVT_BUTTON(self,self.rawAdd.GetId(),self.OnRawAdd)
        wx.EVT_BUTTON(self,self.rawRen.GetId(),self.OnRawRen)
        wx.EVT_BUTTON(self,self.rawDel.GetId(),self.OnRawDel)
        wx.EVT_BUTTON(self,self.toPre.GetId(),self.ToPre)
        wx.EVT_BUTTON(self,self.fromPre.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.rawExport.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.rawMerge.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.rawSubset.GetId(),self.OnDevelopment)

        #preprocessed data events
        wx.EVT_BUTTON(self,self.preAdd.GetId(),self.OnPreAdd)
        wx.EVT_BUTTON(self,self.preRen.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.preDel.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.project.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.initSOM.GetId(),self.OnDevelopment)

        #projected data events
        wx.EVT_BUTTON(self,self.proAdd.GetId(),self.OnProAdd)
        wx.EVT_BUTTON(self,self.proRen.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.proDel.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.proShape.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.proExport.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.trajectory.GetId(),self.OnDevelopment)
        
        #initial SOM events
        wx.EVT_BUTTON(self,self.initAdd.GetId(),self.OnInitAdd)
        wx.EVT_BUTTON(self,self.initRen.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.initDel.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.toTrain.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.fromTrain.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.initExport.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.train.GetId(),self.OnDevelopment)

        #trained SOM events
        wx.EVT_BUTTON(self,self.trainAdd.GetId(),self.OnTrainAdd)
        wx.EVT_BUTTON(self,self.trainRen.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.trainDel.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.trainShape.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.trainExport.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.dominance.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.Kmeans.GetId(),self.OnDevelopment)

        #shapefile events
        wx.EVT_BUTTON(self,self.shapeRen.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.shapeDel.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.shapeExport.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.load.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.save.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.help.GetId(),self.OnHelp)
        wx.EVT_BUTTON(self,self.about.GetId(),self.OnAbout)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("SOM Analyst")
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_BTNFACE))
        self.mergeType.SetSelection(0)
        self.projMeasure.SetSelection(0)
        self.initType.SetSelection(0)
        self.trainMeasure.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        mainBox = wx.BoxSizer(wx.VERTICAL)
        mainGrid = wx.FlexGridSizer(4, 3, 2, 2)
        shapeGrid = wx.FlexGridSizer(4, 2, 2, 0)
        grid_sizer_7 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_4_copy_4 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_3_copy_4 = wx.FlexGridSizer(6, 1, 0, 0)
        trainGrid = wx.FlexGridSizer(4, 2, 2, 0)
        grid_sizer_4_copy_3 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_3_copy_3 = wx.FlexGridSizer(6, 1, 0, 0)
        initGrid = wx.FlexGridSizer(4, 2, 2, 0)
        grid_sizer_6 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_4_copy_2 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_3_copy_2 = wx.FlexGridSizer(6, 1, 0, 0)
        proGrid = wx.FlexGridSizer(4, 2, 2, 0)
        grid_sizer_5 = wx.FlexGridSizer(5, 2, 0, 0)
        grid_sizer_3_copy_1 = wx.FlexGridSizer(6, 1, 0, 0)
        preGrid = wx.FlexGridSizer(4, 2, 2, 0)
        grid_sizer_4_copy = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_3_copy = wx.FlexGridSizer(6, 1, 0, 0)
        rawGrid = wx.FlexGridSizer(4, 2, 2, 0)
        grid_sizer_4 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(6, 1, 0, 0)
        mainGrid.Add(self.rawTitle, 0, 0, 0)
        mainGrid.Add(self.preTitle, 0, 0, 0)
        mainGrid.Add(self.proTitle, 0, 0, 0)
        rawGrid.Add(self.rawList, 0, wx.EXPAND, 0)
        grid_sizer_3.Add(self.rawAdd, 0, 0, 0)
        grid_sizer_3.Add(self.rawRen, 0, 0, 0)
        grid_sizer_3.Add(self.rawDel, 0, 0, 0)
        grid_sizer_3.Add(self.toPre, 0, 0, 0)
        grid_sizer_3.Add(self.fromPre, 0, 0, 0)
        grid_sizer_3.Add(self.rawExport, 0, 0, 0)
        rawGrid.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        rawGrid.Add(self.mergeType, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        rawGrid.Add(self.rawMerge, 0, wx.ALIGN_BOTTOM, 0)
        grid_sizer_4.Add(self.subStartLabel, 0, 0, 0)
        grid_sizer_4.Add(self.subStart, 0, 0, 0)
        grid_sizer_4.Add(self.subStopLabel, 0, 0, 0)
        grid_sizer_4.Add(self.subStop, 0, 0, 0)
        grid_sizer_4.Add(self.subStepLabel, 0, 0, 0)
        grid_sizer_4.Add(self.subStep, 0, 0, 0)
        rawGrid.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        rawGrid.Add(self.rawSubset, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        mainGrid.Add(rawGrid, 1, wx.EXPAND, 0)
        preGrid.Add(self.preList, 0, wx.EXPAND, 0)
        grid_sizer_3_copy.Add(self.preAdd, 0, 0, 0)
        grid_sizer_3_copy.Add(self.preRen, 0, 0, 0)
        grid_sizer_3_copy.Add(self.preDel, 0, 0, 0)
        grid_sizer_3_copy.Add((20, 22), 0, 0, 0)
        grid_sizer_3_copy.Add((20, 22), 0, 0, 0)
        grid_sizer_3_copy.Add(self.preExport, 0, 0, 0)
        preGrid.Add(grid_sizer_3_copy, 1, wx.EXPAND, 0)
        preGrid.Add(self.projMeasure, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        preGrid.Add(self.project, 0, wx.ALIGN_BOTTOM, 0)
        grid_sizer_4_copy.Add(self.initTypeLabel, 0, 0, 0)
        grid_sizer_4_copy.Add(self.initType, 0, wx.EXPAND, 0)
        grid_sizer_4_copy.Add(self.xDimLabel, 0, 0, 0)
        grid_sizer_4_copy.Add(self.xDim, 0, 0, 0)
        grid_sizer_4_copy.Add(self.yDimLabel, 0, 0, 0)
        grid_sizer_4_copy.Add(self.yDim, 0, 0, 0)
        preGrid.Add(grid_sizer_4_copy, 1, wx.EXPAND, 0)
        preGrid.Add(self.initSOM, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        mainGrid.Add(preGrid, 1, wx.EXPAND, 0)
        proGrid.Add(self.proList, 0, wx.EXPAND, 0)
        grid_sizer_3_copy_1.Add(self.proAdd, 0, 0, 0)
        grid_sizer_3_copy_1.Add(self.proRen, 0, 0, 0)
        grid_sizer_3_copy_1.Add(self.proDel, 0, 0, 0)
        grid_sizer_3_copy_1.Add(self.proShape, 0, 0, 0)
        grid_sizer_3_copy_1.Add((20, 22), 0, 0, 0)
        grid_sizer_3_copy_1.Add(self.proExport, 0, 0, 0)
        proGrid.Add(grid_sizer_3_copy_1, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(self.trajStartLabel, 0, 0, 0)
        grid_sizer_5.Add(self.trajStart, 0, 0, 0)
        grid_sizer_5.Add(self.trajStopLabel, 0, 0, 0)
        grid_sizer_5.Add(self.trajStop, 0, 0, 0)
        grid_sizer_5.Add(self.trajStepLabel, 0, 0, 0)
        grid_sizer_5.Add(self.trajStep, 0, 0, 0)
        grid_sizer_5.Add(self.trajOffsetLabel, 0, 0, 0)
        grid_sizer_5.Add(self.trajOffset, 0, 0, 0)
        grid_sizer_5.Add(self.trajRepeatLabel, 0, 0, 0)
        grid_sizer_5.Add(self.trajRepeat, 0, 0, 0)
        proGrid.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        proGrid.Add(self.trajectory, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        mainGrid.Add(proGrid, 1, wx.EXPAND, 0)
        mainGrid.Add(self.initTitle, 0, 0, 0)
        mainGrid.Add(self.trainTitle, 0, 0, 0)
        mainGrid.Add(self.shapeTitle, 0, 0, 0)
        initGrid.Add(self.initList, 0, wx.EXPAND, 0)
        grid_sizer_3_copy_2.Add(self.initAdd, 0, 0, 0)
        grid_sizer_3_copy_2.Add(self.initRen, 0, 0, 0)
        grid_sizer_3_copy_2.Add(self.initDel, 0, 0, 0)
        grid_sizer_3_copy_2.Add(self.toTrain, 0, 0, 0)
        grid_sizer_3_copy_2.Add(self.fromTrain, 0, 0, 0)
        grid_sizer_3_copy_2.Add(self.initExport, 0, 0, 0)
        initGrid.Add(grid_sizer_3_copy_2, 1, wx.EXPAND, 0)
        grid_sizer_4_copy_2.Add(self.trainLenLabel, 0, 0, 0)
        grid_sizer_4_copy_2.Add(self.trainLen, 0, 0, 0)
        grid_sizer_4_copy_2.Add(self.trainAlphaLabel, 0, 0, 0)
        grid_sizer_4_copy_2.Add(self.trainAlpha, 0, 0, 0)
        grid_sizer_4_copy_2.Add(self.trainRadiusLabel, 0, 0, 0)
        grid_sizer_4_copy_2.Add(self.trainRadius, 0, 0, 0)
        initGrid.Add(grid_sizer_4_copy_2, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_6.Add(self.trainMeasure, 0, 0, 0)
        grid_sizer_6.Add(self.train, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        initGrid.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        mainGrid.Add(initGrid, 1, wx.EXPAND, 0)
        trainGrid.Add(self.trainList, 0, wx.EXPAND, 0)
        grid_sizer_3_copy_3.Add(self.trainAdd, 0, 0, 0)
        grid_sizer_3_copy_3.Add(self.trainRen, 0, 0, 0)
        grid_sizer_3_copy_3.Add(self.trainDel, 0, 0, 0)
        grid_sizer_3_copy_3.Add(self.trainShape, 0, 0, 0)
        grid_sizer_3_copy_3.Add((20, 22), 0, 0, 0)
        grid_sizer_3_copy_3.Add(self.trainExport, 0, 0, 0)
        trainGrid.Add(grid_sizer_3_copy_3, 1, wx.EXPAND, 0)
        trainGrid.Add(self.clusteringLabel, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        trainGrid.Add(self.dominance, 0, wx.ALIGN_BOTTOM, 0)
        grid_sizer_4_copy_3.Add(self.kClustersLabel, 0, 0, 0)
        grid_sizer_4_copy_3.Add(self.kClusters, 0, 0, 0)
        grid_sizer_4_copy_3.Add(self.kLenLabel, 0, 0, 0)
        grid_sizer_4_copy_3.Add(self.kLength, 0, 0, 0)
        trainGrid.Add(grid_sizer_4_copy_3, 1, wx.EXPAND, 0)
        trainGrid.Add(self.Kmeans, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        mainGrid.Add(trainGrid, 1, wx.EXPAND, 0)
        shapeGrid.Add(self.shapeList, 0, wx.EXPAND, 0)
        grid_sizer_3_copy_4.Add((20, 22), 0, 0, 0)
        grid_sizer_3_copy_4.Add(self.shapeRen, 0, 0, 0)
        grid_sizer_3_copy_4.Add(self.shapeDel, 0, 0, 0)
        grid_sizer_3_copy_4.Add((20, 22), 0, 0, 0)
        grid_sizer_3_copy_4.Add((20, 22), 0, 0, 0)
        grid_sizer_3_copy_4.Add(self.shapeExport, 0, 0, 0)
        shapeGrid.Add(grid_sizer_3_copy_4, 1, wx.EXPAND, 0)
        grid_sizer_7.Add(self.systemLabel, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_4_copy_4.Add(self.load, 0, 0, 0)
        grid_sizer_4_copy_4.Add(self.save, 0, 0, 0)
        grid_sizer_4_copy_4.Add(self.help, 0, 0, 0)
        grid_sizer_4_copy_4.Add(self.about, 0, 0, 0)
        grid_sizer_7.Add(grid_sizer_4_copy_4, 1, wx.EXPAND, 0)
        shapeGrid.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        shapeGrid.Add(self.copyright, 0, 0, 0)
        mainGrid.Add(shapeGrid, 1, wx.EXPAND, 0)
        mainBox.Add(mainGrid, 1, wx.EXPAND, 0)
        self.SetSizer(mainBox)
        mainBox.Fit(self)
        self.Layout()
        # end wxGlade

    def OnAbout(self, event):
        wx.MessageBox("Copyright 2008 Martin Lacayo\n\nThanks to my thesis committee:\nAndr\xe9 Skupin, Serge Rey, Carl Eckberg\n\n"+
                      "For futher information visit:\nhttp://somanalyst.hopto.org","About SOM Analyst",
                      wx.OK | wx.ICON_INFORMATION, self)

    def OnHelp(self, event):
        wx.MessageBox("visit http://somanalyst.hopto.org for help using SOM Analyst","SOM Analyst Help",
                      wx.OK | wx.ICON_INFORMATION, self)

    #events
    def OnDevelopment(self, event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)    
        

    #event helper functions
    def OnAdd(self,wildcard):
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(),"", wildcard, wx.MULTIPLE)
        if dialog.ShowModal() == wx.ID_OK:
            temp= dialog.GetPaths()
        dialog.Destroy()
        return temp

    #raw data events
    #add to Raw list box entries and update paths list
    def OnRawAdd(self,event):
        paths=self.OnAdd("Text File (*.txt)|*.txt|All files (*.*)|*.*")
        for p in paths:
            name=p[p.rfind("\\")+1:]
            self.rawListPaths[name]=p
            self.rawList.Insert(name,0)

    #delete Raw list box entries and update paths list
    def OnRawDel(self,event):
        loc=list(self.rawList.GetSelections())
        loc.reverse()
        for l in loc:
            self.rawListPaths.pop(self.rawList.GetString(l))
            self.rawList.Delete(l)

    #rename Raw list box entries and update paths list
    def OnRawRen(self,event):
        dialog=wx.TextEntryDialog(None, "Name","Rename Dialog","")
        loc=self.rawList.GetSelections()
        for l in loc:
            dialog.SetValue(self.rawList.GetString(l))
            if dialog.ShowModal() == wx.ID_OK:
                name=dialog.GetValue()
                self.rawListPaths[name]=self.rawListPaths.pop(self.rawList.GetString(l))
                self.rawList.Delete(l)
                self.rawList.Insert(name,l)
        dialog.Destroy()
        print self.rawListPaths

    def ToPre(self,event):
        self.preList.I

    def OnPreAdd(self,event):
        self.preList.Insert(str(self.OnAdd("Text File (*.txt)|*.txt|All files (*.*)|*.*")),0)

    def OnProAdd(self,event):
        self.proList.Insert(str(self.OnAdd("Bmu File (*.bmu)|*.txt|All files (*.*)|*.*")),0)

    def OnInitAdd(self,event):
        self.initList.Insert(str(self.OnAdd("Codebook (*.cod)|*.cod|All files (*.*)|*.*")),0)

    def OnTrainAdd(self,event):
        self.trainList.Insert(str(self.OnAdd("Codebook (*.cod)|*.cod|All files (*.*)|*.*")),0)



# end of class MyFrame


class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = MyFrame(None, -1, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
