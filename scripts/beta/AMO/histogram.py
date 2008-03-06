import wx
class DrawPanel(wx.Panel):

    """Draw a line to a panel."""

    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.slider = wx.Slider(self, 100, 25, 1, 100, pos=(10, 10),
        size=(250, -1),
        style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS )
        self.slider.SetTickFreq(10, 1)
        self.slider.SetValue(0)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SLIDER, self.OnSlide)

    def OnPaint(self, event=None):
        self.dc = wx.PaintDC(self)        
        self.dc.SetBackground(wx.Brush("White"))
        self.dc.Clear()
        #fill
        self.dc.SetBrush(wx.Brush("BLACK"))
        #line
        self.dc.SetPen(wx.Pen("BLACK", 4))
        self.dc.DrawRectangle(0, 0, 50, 50)

    def OnSlide(self, event=None):
        self.dc.Clear()
        self.dc.DrawRectangle(0, 0, 50, 10)
        

app = wx.PySimpleApp(False)
frame = wx.Frame(None, title="Draw on Panel")
DrawPanel(frame)
frame.Show(True)
app.MainLoop()


##import pylab
##
##fName="D:/users/ryan/dat.txt"
##iFile=open(fName)
##lines=iFile.readlines()
##iFile.close()
##
##termDocumentMatrix=[map(int,l.strip().split(" ")) for l in lines[1:]]
###demonstrates the breadth of vocabulary in a document
##sumDocument=map(sum,termDocumentMatrix)
##
##documentTermMatrix=[[i] for i in termDocumentMatrix[0]]
##for i in termDocumentMatrix[1:]:
##    for id,j in enumerate(i):
##        documentTermMatrix[id].append(j)
###demontrates word usage/frequency
##sumTerm=map(sum,documentTermMatrix)
##
###determin bins
##b=list(set(sumTerm))
##b.sort()
##b=map(b.__getitem__,range(0,len(b),len(b)/20))
##
##
### Make a histogram out of the data in x and prepare a bar plot.
##vals, bins, patchs = pylab.hist(sumTerm, b)
##
### Show the plot.
##pylab.show()


##def bin(
##delta=(max(sumTerm)-min(sumTerm)-.1)/10.0
##hist=[0]*10
##for n in sumTerm:
##    i=int(math.floor(n/delta))
##    hist[i]+=1

##def squared(i):
##    return i**2
##
##N=float(len(sumTerm))
##mean=sum(sumTerm)/float(N)

###std dev, sqrt of difference squared
##stdDev=0
##for i in sumTerm:
##    stdDev+=((i-mean)**2)/N
##stdDev=stdDev**0.5
##
##min=mean-stdDev
##max=mean+stdDev
###%68 of data with 1 std dev
