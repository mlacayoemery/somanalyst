import wx, os, shutil, pickle
from lib.som import mapinit, visual, vsom
from lib.som import ATRtoSHP, CODtoSHP


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        #raw data elements
        ##variables        
        self.rawListPaths = {}
        
        ##labels
        self.rawTitle = wx.StaticText(self, -1, "Raw Data")

        ##buttons
        self.rawAdd = wx.Button(self, wx.NewId(), "Add")
        self.rawRen = wx.Button(self, wx.NewId(), "Rename")
        self.rawDel = wx.Button(self, wx.NewId(), "Delete")
        self.toPre = wx.Button(self, wx.NewId(), "->")
        self.fromPre = wx.Button(self, wx.NewId(), "<-")
        self.rawExport = wx.Button(self, wx.NewId(), "Export")
        self.rawMerge = wx.Button(self, wx.NewId(), "Merge")
        self.subStartLabel = wx.StaticText(self, -1, "Start")
        self.subStopLabel = wx.StaticText(self, -1, "Stop")
        self.subStepLabel = wx.StaticText(self, -1, "Step")
        self.rawSubset = wx.Button(self, wx.NewId(), "Subset")        
        
        ##boxes        
        self.mergeType = wx.RadioBox(self, -1, "", choices=["Vertical", "Horizontal"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.rawList = wx.ListBox(self, -1, choices=[], style=wx.LB_EXTENDED)
        self.subStart = wx.TextCtrl(self, -1, "1")
        self.subStop = wx.TextCtrl(self, -1, "")
        self.subStep = wx.TextCtrl(self, -1, "1")
        
        #preprocessed data elements     
        ##varaibles
        self.preListPaths = {}
        
        ##labels
        self.preTitle = wx.StaticText(self, -1, "Preprocessed Data")
        self.initTypeLabel = wx.StaticText(self, -1, "type")
        self.xDimLabel = wx.StaticText(self, -1, "x dim")
        self.yDimLabel = wx.StaticText(self, -1, "y dim")
       
        ##buttons
        self.preAdd = wx.Button(self, wx.NewId(), "Add")
        self.preRen = wx.Button(self, wx.NewId(), "Rename")
        self.preDel = wx.Button(self, wx.NewId(), "Delete")
        self.preExport = wx.Button(self, wx.NewId(), "Export")
        self.initSOM = wx.Button(self, wx.NewId(), "Initial SOM")
        self.project = wx.Button(self, wx.NewId(), "Project")
        
        ##boxes
        self.preList = wx.ListBox(self, -1, choices=[],style=wx.LB_EXTENDED)
        self.projMeasure = wx.RadioBox(self, -1, "", choices=["Cosine", "Euclidean"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)        
        self.initType = wx.ComboBox(self, -1, choices=["lin", "rand"], style=wx.CB_DROPDOWN)
        self.xDim = wx.TextCtrl(self, -1, "")
        self.yDim = wx.TextCtrl(self, -1, "")
        
        #projected data elements
        ##varaibles
        self.proListPaths = {}
        
        ##labels
        self.proTitle = wx.StaticText(self, -1, "Projected Data")
        self.trajStartLabel = wx.StaticText(self, -1, "Start")
        self.trajStopLabel = wx.StaticText(self, -1, "Stop")
        self.trajStepLabel = wx.StaticText(self, -1, "Step")
        self.trajOffsetLabel = wx.StaticText(self, -1, "Offset")
        self.trajRepeatLabel = wx.StaticText(self, -1, "Repeat")
        
        ##buttons
        self.proAdd = wx.Button(self, wx.NewId(), "Add")
        self.proRen = wx.Button(self, wx.NewId(), "Rename")
        self.proDel = wx.Button(self, wx.NewId(), "Delete")
        self.proShape = wx.Button(self, wx.NewId(), "Shapefile")
        self.proExport = wx.Button(self, wx.NewId(), "Export")
        self.trajectory = wx.Button(self, wx.NewId(), "Trajectory")
        
        ##boxes
        self.proList = wx.ListBox(self, -1, choices=[], style=wx.LB_EXTENDED)
        self.trajStart = wx.TextCtrl(self, -1, "0")
        self.trajStop = wx.TextCtrl(self, -1, "")
        self.trajStep = wx.TextCtrl(self, -1, "1")
        self.trajOffset = wx.TextCtrl(self, -1, "0")
        self.trajRepeat = wx.TextCtrl(self, -1, "1")
        
        #intial som elements
        ##varaibles
        self.initListPaths={}
        
        ##labels
        self.initTitle = wx.StaticText(self, -1, "Initial SOM")
        self.trainLenLabel = wx.StaticText(self, -1, "rlen")
        self.trainAlphaLabel = wx.StaticText(self, -1, "alpha")
        self.trainRadiusLabel = wx.StaticText(self, -1, "radius")
        
        ##buttons
        self.initAdd = wx.Button(self, wx.NewId(), "Add")
        self.initRen = wx.Button(self, wx.NewId(), "Rename")
        self.initDel = wx.Button(self, wx.NewId(), "Delete")
        self.toTrain = wx.Button(self, wx.NewId(), "->")
        self.fromTrain = wx.Button(self, wx.NewId(), "<-")
        self.initExport = wx.Button(self, wx.NewId(), "Export")
        self.train = wx.Button(self, wx.NewId(), "Train")
        
        ##boxes
        self.initList = wx.ListBox(self, -1, choices=[], style=wx.LB_EXTENDED)
        self.trainLen = wx.TextCtrl(self, -1, "")
        self.trainAlpha = wx.TextCtrl(self, -1, "0.04")
        self.trainRadius = wx.TextCtrl(self, -1, "")
        self.trainMeasure = wx.RadioBox(self, -1, "", choices=["Cosine", "Euclidean"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
          
        #trained som elements
        ##varaibles
        self.trainListPaths={}
        
        ##labels
        self.trainTitle = wx.StaticText(self, -1, "Trained SOM")
        self.clusteringLabel = wx.StaticText(self, -1, "Clustering")
        self.kClustersLabel = wx.StaticText(self, -1, "clusters")
        
        ##buttons
        self.trainAdd = wx.Button(self, wx.NewId(), "Add")
        self.trainRen = wx.Button(self, wx.NewId(), "Rename")
        self.trainDel = wx.Button(self, wx.NewId(), "Delete")
        self.trainShape = wx.Button(self, wx.NewId(), "Shapefile")
        self.trainExport = wx.Button(self, wx.NewId(), "Export")
        self.dominance = wx.Button(self, wx.NewId(), "Dominance")
        self.Kmeans = wx.Button(self, wx.NewId(), "K-means")
        
        ##boxes
        self.trainList = wx.ListBox(self, -1, choices=[], style=wx.LB_EXTENDED)
        self.kClusters = wx.TextCtrl(self, -1, "")
        self.kLenLabel = wx.StaticText(self, -1, "rlen")
        self.kLength = wx.TextCtrl(self, -1, "")
        
        #shapefile elements
        ##variables
        self.shapeListPaths={}
        ##labels
        self.shapeTitle = wx.StaticText(self, -1, "Shapefiles")

        ##buttons
        self.shapeRen = wx.Button(self, wx.NewId(), "Rename")
        self.shapeDel = wx.Button(self, wx.NewId(), "Delete")
        self.shapeExport = wx.Button(self, wx.NewId(), "Export")

        ##boxes
        self.shapeList = wx.ListBox(self, -1, choices=[])

        #system elements
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
        wx.EVT_BUTTON(self,self.toPre.GetId(),self.OnToPre)
        wx.EVT_BUTTON(self,self.fromPre.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.rawExport.GetId(),self.OnRawExport)
        wx.EVT_BUTTON(self,self.rawMerge.GetId(),self.OnMerge)
        wx.EVT_BUTTON(self,self.rawSubset.GetId(),self.OnSubset)

        #preprocessed data events
        wx.EVT_BUTTON(self,self.preAdd.GetId(),self.OnPreAdd)
        wx.EVT_BUTTON(self,self.preRen.GetId(),self.OnPreRen)
        wx.EVT_BUTTON(self,self.preDel.GetId(),self.OnPreDel)
        wx.EVT_BUTTON(self,self.fromPre.GetId(),self.OnToRaw)        
        wx.EVT_BUTTON(self,self.project.GetId(),self.OnProject)
        wx.EVT_BUTTON(self,self.initSOM.GetId(),self.OnInitSOM)

        #projected data events
        wx.EVT_BUTTON(self,self.proAdd.GetId(),self.OnProAdd)
        wx.EVT_BUTTON(self,self.proRen.GetId(),self.OnProRen)
        wx.EVT_BUTTON(self,self.proDel.GetId(),self.OnProDel)
        wx.EVT_BUTTON(self,self.proShape.GetId(),self.OnProShape)
        wx.EVT_BUTTON(self,self.proExport.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.trajectory.GetId(),self.OnDevelopment)
        
        #initial SOM events
        wx.EVT_BUTTON(self,self.initAdd.GetId(),self.OnInitAdd)
        wx.EVT_BUTTON(self,self.initRen.GetId(),self.OnInitRen)
        wx.EVT_BUTTON(self,self.initDel.GetId(),self.OnInitDel)
        wx.EVT_BUTTON(self,self.toTrain.GetId(),self.OnToTrain)
        wx.EVT_BUTTON(self,self.fromTrain.GetId(),self.OnToInit)
        wx.EVT_BUTTON(self,self.initExport.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.train.GetId(),self.OnTrain)

        #trained SOM events
        wx.EVT_BUTTON(self,self.trainAdd.GetId(),self.OnTrainAdd)
        wx.EVT_BUTTON(self,self.trainRen.GetId(),self.OnTrainRen)
        wx.EVT_BUTTON(self,self.trainDel.GetId(),self.OnTrainDel)
        wx.EVT_BUTTON(self,self.trainShape.GetId(),self.OnTrainShape)
        wx.EVT_BUTTON(self,self.trainExport.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.dominance.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.Kmeans.GetId(),self.OnDevelopment)

        #shapefile events
        wx.EVT_BUTTON(self,self.shapeRen.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.shapeDel.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.shapeExport.GetId(),self.OnDevelopment)
        wx.EVT_BUTTON(self,self.load.GetId(),self.OnLoad)
        wx.EVT_BUTTON(self,self.save.GetId(),self.OnSave)
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

    #events
    def OnAbout(self, event):
        wx.MessageBox("Copyright 2008 Martin Lacayo\n\nThanks to my thesis committee:\nAndr\xe9 Skupin, Serge Rey, Carl Eckberg\n\n"+
                      "For futher information visit:\nhttp://somanalyst.hopto.org","About SOM Analyst",
                      wx.OK | wx.ICON_INFORMATION, self)

    def OnHelp(self, event):
        wx.MessageBox("visit http://somanalyst.hopto.org for help using SOM Analyst","SOM Analyst Help",
                      wx.OK | wx.ICON_INFORMATION, self)
    
    def OnDevelopment(self, event):
        wx.MessageBox("This function is under development.","Under development",
                      wx.OK | wx.ICON_INFORMATION, self)    
        
    #event helper functions
    #multiple add file dialog
    def OnAdd(self,listbox,paths,wcd):
        dialog = wx.FileDialog(self, message='Select files', wildcard=wcd, style=wx.MULTIPLE)
        temp=[]
        if dialog.ShowModal() == wx.ID_OK:
            temp= dialog.GetPaths()
        dialog.Destroy()
        for p in temp:
            name=p[p.rfind("\\")+1:]
            if not paths.has_key(name):
                paths[name]=p
                listbox.Insert(name,0)

    #multiple delete function
    def OnDel(self,listbox,paths):
        loc=list(listbox.GetSelections())
        loc.reverse()
        for l in loc:
            paths.pop(listbox.GetString(l))
            listbox.Delete(l)

    #multiple rename function
    def OnRen(self,listbox,paths):
        dialog=wx.TextEntryDialog(None, "Name","Rename Dialog","")
        loc=listbox.GetSelections()
        for l in loc:
            dialog.SetValue(listbox.GetString(l))
            if dialog.ShowModal() == wx.ID_OK:
                name=dialog.GetValue()
                if not paths.has_key(name):
                    paths[name]=paths.pop(listbox.GetString(l))
                    listbox.Delete(l)
                    listbox.Insert(name,l)
        dialog.Destroy()

    #transfers files between lists
    def OnTo(self,listboxorigin,pathsorigin,listboxdestination,pathsdestination):
        loc=list(listboxorigin.GetSelections())
        loc.reverse()
        for l in loc:
            name=listboxorigin.GetString(l)
            if not pathsdestination.has_key(name):
                pathsdestination[name]=pathsorigin[name]
                listboxdestination.Insert(name,0)   
            
    def OnExport(self,listbox,paths,wcd="Text File (*.txt)|*.txt|All files (*.*)|*.*"):      
        dir = os.getcwd()
        dialog = wx.FileDialog(self, message='Save file as...', defaultDir=dir, defaultFile='',wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
        loc=listbox.GetSelections()
        for l in loc:
            dialog.SetFilename(listbox.GetString(l))
            if dialog.ShowModal() == wx.ID_OK:
                shutil.copy(paths[listbox.GetString(l)],dialog.GetDirectory()+"\\"+dialog.GetFilename())
        dialog.Destroy()

      
    #RAW DATA EVENTS
    def OnRawAdd(self,event):
        self.OnAdd(self.rawList,self.rawListPaths,"Data File (*.dat)|*.dat|All files (*.*)|*.*")

    def OnRawDel(self,event):
        self.OnDel(self.rawList,self.rawListPaths)

    def OnRawRen(self,event):
        self.OnRen(self.rawList,self.rawListPaths)

    def OnToPre(self,event):
        self.OnTo(self.rawList,self.rawListPaths,self.preList,self.preListPaths)

    def OnRawExport(self,event):
        self.OnExport(self.rawList,self.rawListPaths)

    def OnMerge(self,event):
        wcd="Data File (*.dat)|*.dat|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, message='Save file as...', wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
        loc=self.rawList.GetSelections()
        paths=[]
        name=[]
        for l in loc:
            name.append(self.rawList.GetString(l).replace(".","_"))
            paths.append(self.rawListPaths[self.rawList.GetString(l)])
        print name
        dialog.SetFilename("-".join(name)+".dat")
        if dialog.ShowModal() == wx.ID_OK:
            path=dialog.GetDirectory()+"\\"+dialog.GetFilename()
            name=dialog.GetFilename()
            oFile=open(path,'w')
            if self.mergeType.GetSelection()==0:
                iFile=open(paths[0],'r')
                oFile.write(iFile.readline())
                iFile.close()
                for p in paths:
                    iFile=open(p,'r')
                    iFile.readline()
                    lines=iFile.readlines()
                    for l in lines:
                        oFile.write(l)
                    oFile.write("\n")
                oFile.close()                       
            else:
                iFile=open(paths[0],'r')
                iFile.close()
                dims=0
                iLines=[]
                for p in paths:
                    temp=open(p,'r')
                    dims+=int(temp.readline())
                    iLines.append(temp.readlines())
                    temp.close()
                oFile.write(str(dims))
                for i in range(len(iLines[0])):
                    line=[]
                    for l in iLines:
                        line.append(l[i].strip())
                    oFile.write("\n"+" ".join(line))
                oFile.close()    
            if not self.rawListPaths.has_key(name):
                self.rawListPaths[name]=path
                self.rawList.Insert(name,0)
        dialog.Destroy()


    def OnSubset(self,event):
        wcd="Data File (*.dat)|*.dat|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, message='Save file as...', wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
        loc=self.rawList.GetSelections()
        for l in loc:
            dialog.SetFilename(self.rawList.GetString(l).replace(".","_")+"_sub.dat")
            if dialog.ShowModal() == wx.ID_OK:
                iFile=open(self.rawListPaths[self.rawList.GetString(l)],'r')
                oFile=open(dialog.GetDirectory()+"\\"+dialog.GetFilename(),'w')
                lines=iFile.readlines()
                iFile.close()
                oFile.write(lines[0])
                start=int(self.subStart.GetValue())
                step=int(self.subStep.GetValue())
                stop=self.subStop.GetValue()
                if stop=="":
                    lines=lines[start::step]
                else:
                    lines=lines[start:int(stop):step]
                for l in lines:
                    oFile.write(l)
                oFile.close()
        dialog.Destroy()        

    #PREPROCESSED DATA EVENTS
    def OnPreAdd(self,event):
        self.OnAdd(self.preList,self.preListPaths,"Data File (*.dat)|*.dat|All files (*.*)|*.*")

    def OnPreDel(self,event):
        self.OnDel(self.preList,self.preListPaths)

    def OnPreRen(self,event):
        self.OnRen(self.preList,self.preListPaths)

    def OnToRaw(self,event):
        self.OnTo(self.preList,self.preListPaths,self.rawList,self.rawListPaths)

    def OnInitSOM(self,event):
        wcd="Codebook File (*.cod)|*.cod|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, message='Save file as...', wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
        loc=self.preList.GetSelections()
        for l in loc:
            dialog.SetFilename(self.preList.GetString(l).replace(".","_")+".cod")
            if dialog.ShowModal() == wx.ID_OK:
                path=dialog.GetDirectory()+"\\"+dialog.GetFilename()
                name=path[path.rfind("\\")+1:]
                mapinit.mapinit(self.preListPaths[self.preList.GetString(l)],path,
                                "hexa","gaussian",self.xDim.GetValue(),self.yDim.GetValue(),
                                self.initType.GetValue())
                if not self.initListPaths.has_key(name):
                    self.initListPaths[name]=path
                    self.initList.Insert(name,0)
        dialog.Destroy()

    def OnProject(self,event):
        wcd="Projection File (*.bmu)|*.bmu|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, message='Save file as...', wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
        soms=self.trainList.GetSelections()
        data=self.preList.GetSelections()
        for s in soms:
            for d in data:
                dialog.SetFilename(self.preList.GetString(d).replace(".","_")+"-"+
                                   self.trainList.GetString(s).replace(".","_")+".bmu")
                if dialog.ShowModal() == wx.ID_OK:
                    path=dialog.GetDirectory()+"\\"+dialog.GetFilename()
                    name=path[path.rfind("\\")+1:]
                    visual.visual(self.trainListPaths[self.trainList.GetString(s)],
                                  self.preListPaths[self.preList.GetString(d)],
                                  path)
                    if not self.proListPaths.has_key(name):
                        self.proListPaths[name]=path
                        self.proList.Insert(name,0)                    
        dialog.Destroy()


    #PROJECTED DATA EVENTS
    def OnProAdd(self,event):
        self.OnAdd(self.proList,self.proListPaths,"Projection File (*.bmu)|*.bmu|All files (*.*)|*.*")

    def OnProDel(self,event):
        self.OnDel(self.proList,self.proListPaths)

    def OnProRen(self,event):
        self.OnRen(self.proList,self.proListPaths)

    def OnProShape(self,event):
        wcd="Shapefile (*.shp)|*.shp|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, message='Save file as...', wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
        loc=self.proList.GetSelections()
        for l in loc:
            dialog.SetFilename(self.proList.GetString(l).replace(".","_")+".shp")
            if dialog.ShowModal() == wx.ID_OK:
                path=dialog.GetDirectory()+"\\"+dialog.GetFilename()
                name=path[path.rfind("\\")+1:]
                ATRtoSHP.ATRtoP(self.proListPaths[self.proList.GetString(l)],
                                path,"point")
                if not self.shapeListPaths.has_key(name):
                    self.shapeListPaths[name]=path
                    self.shapeList.Insert(name,0)
        dialog.Destroy()        

    #INTIAL SOM EVENTS
    def OnInitAdd(self,event):
        self.OnAdd(self.initList,self.initListPaths,"Codebook File (*.cod)|*.cod|All files (*.*)|*.*")

    def OnInitDel(self,event):
        self.OnDel(self.initList,self.initListPaths)

    def OnInitRen(self,event):
        self.OnRen(self.initList,self.initListPaths)

    def OnToTrain(self,event):
        self.OnTo(self.initList,self.initListPaths,self.trainList,self.trainListPaths)

    def OnTrain(self,event):
        wcd="Codebook File (*.cod)|*.cod|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, message='Save file as...', wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
        soms=self.initList.GetSelections()
        data=self.preList.GetSelections()
        for s in soms:
            for d in data:
                dialog.SetFilename(self.initList.GetString(s).replace(".","_")+"-"+
                                   self.preList.GetString(d).replace(".","_")+".cod")
                if dialog.ShowModal() == wx.ID_OK:
                    path=dialog.GetDirectory()+"\\"+dialog.GetFilename()
                    name=path[path.rfind("\\")+1:]
                    vsom.vsom(self.initListPaths[self.initList.GetString(s)],
                              self.preListPaths[self.preList.GetString(d)],
                              path,
                              self.trainLen.GetValue(),
                              self.trainAlpha.GetValue(),
                              self.trainRadius.GetValue())
                    if not self.trainListPaths.has_key(name):
                        self.trainListPaths[name]=path
                        self.trainList.Insert(name,0)                    
        dialog.Destroy()
        

    #TRAINED SOM EVENTS
    def OnTrainAdd(self,event):
        self.OnAdd(self.trainList,self.trainListPaths,"Codebook File (*.cod)|*.cod|All files (*.*)|*.*")

    def OnTrainDel(self,event):
        self.OnDel(self.trainList,self.trainListPaths)

    def OnTrainRen(self,event):
        self.OnRen(self.trainList,self.trainListPaths)

    def OnToInit(self,event):
        self.OnTo(self.trainList,self.trainListPaths,self.initList,self.initListPaths)

    def OnTrainShape(self,event):
        wcd="Shapefile (*.shp)|*.shp|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, message='Save file as...', wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
        loc=self.trainList.GetSelections()
        for l in loc:
            dialog.SetFilename(self.trainList.GetString(l).replace(".","_")+".shp")
            if dialog.ShowModal() == wx.ID_OK:
                path=dialog.GetDirectory()+"\\"+dialog.GetFilename()
                name=path[path.rfind("\\")+1:]
                CODtoSHP.CODtoSHP(self.trainListPaths[self.trainList.GetString(l)],
                                path,"polygon")
                if not self.shapeListPaths.has_key(name):
                    self.shapeListPaths[name]=path
                    self.shapeList.Insert(name,0)
        dialog.Destroy()        


    #SHAPEFILE EVENTS

    #SOM ANALYST SYSTEM EVENTS
    def OnSave(self,event):
        wcd="Pickle File (*.p)|*.p|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, message='Save file as...', wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
        if dialog.ShowModal() == wx.ID_OK:
            path=open(dialog.GetDirectory()+"\\"+dialog.GetFilename(),'w')
            
            pickle.dump(list(self.rawList.GetStrings()), path)
            pickle.dump(list(self.preList.GetStrings()), path)
            pickle.dump(list(self.proList.GetStrings()), path)
            pickle.dump(list(self.initList.GetStrings()), path)
            pickle.dump(list(self.trainList.GetStrings()), path)
            pickle.dump(list(self.shapeList.GetStrings()), path)
            pickle.dump(self.rawListPaths, path)
            pickle.dump(self.preListPaths, path)
            pickle.dump(self.proListPaths, path)
            pickle.dump(self.initListPaths, path)
            pickle.dump(self.trainListPaths, path)
            pickle.dump(self.shapeListPaths, path)

            path.close()            

        dialog.Destroy()             

    def EmptyLoad(self,listbox,strings):
        for i in range(listbox.GetCount()):
            listbox.Delete(0)
        for id,s in enumerate(strings):
            listbox.Insert(s,id)       

    def OnLoad(self,event):
        wcd="Pickle File (*.p)|*.p|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, message='Select files', wildcard=wcd)
        temp=[]
        if dialog.ShowModal() == wx.ID_OK:
            path=open(dialog.GetPath(),'r')


            self.EmptyLoad(self.rawList,pickle.load(path))
            self.EmptyLoad(self.preList,pickle.load(path))
            self.EmptyLoad(self.proList,pickle.load(path))
            self.EmptyLoad(self.initList,pickle.load(path))
            self.EmptyLoad(self.trainList,pickle.load(path))
            self.EmptyLoad(self.shapeList,pickle.load(path))
            self.rawListPaths = pickle.load(path)
            self.preListPaths = pickle.load(path)
            self.proListPaths = pickle.load(path)
            self.initListPaths = pickle.load(path)
            self.trainListPaths = pickle.load(path)
            self.shapeListPaths = pickle.load(path)

            path.close()            
        dialog.Destroy()

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
