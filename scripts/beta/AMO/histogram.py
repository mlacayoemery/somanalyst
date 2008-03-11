import wx
import math

def histogram(data,classes):
    minimum=float(min(data))
    maximum=float(max(data))
    delta=(maximum-minimum)/(classes-1)
    counts=[0]*classes
    for d in data:
        counts[int(math.floor((d-minimum)/delta))]+=1
    for i in range(len(counts)):
        counts[i]=int(long(counts[i])*10/len(data))
    return counts
    

class DrawPanel(wx.Panel):

    """Draw a line to a panel."""

    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        self.data=[1,2,2,3,3,3,4,4,5]
        self.classes=5
        self.histogram=histogram(self.data,self.classes)
        self.width=100
        self.classwidth=int(float(self.width)/self.classes)
        
        self.minslider = wx.Slider(self, 100, 25, 0, self.classes, pos=(0, 100),
        size=(self.width+20, 20),
        style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_TOP)
        self.minslider.SetTickFreq(1, self.classes)
        self.minslider.SetValue(0)
        self.minOldValue=0
        
        self.maxslider = wx.Slider(self, 100, 25, 0, self.classes, pos=(0, 120),
        size=(self.width+20, 20),
        style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_TOP)
        self.maxslider.SetTickFreq(1, self.classes)
        self.maxslider.SetValue(5)
        self.maxOldValue=5

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SLIDER, self.OnSlide)

    def OnPaint(self, event=None):
        self.dc = wx.PaintDC(self)        
        self.dc.SetBackground(wx.Brush("Grey"))
        self.dc.Clear()
        #fill
        self.dc.SetBrush(wx.Brush("Black"))
        #line
        self.dc.SetPen(wx.TRANSPARENT_PEN)
        for col,value in enumerate(self.histogram):
            self.dc.DrawRectangle(10+(self.classwidth*col), 100, self.classwidth, value*-10)
        

    def OnSlide(self, event=None):
        if self.minOldValue>self.minslider.GetValue():
            #uncolor
            self.dc.SetBrush(wx.Brush("Black"))
            for col in range(self.minslider.GetValue(),self.minOldValue):
                self.dc.DrawRectangle(10+(self.classwidth*col), 100,
                                      self.classwidth/2, self.histogram[col]*-10)                
        elif self.minOldValue<self.minslider.GetValue():
            #color
            self.dc.SetBrush(wx.Brush("Blue"))
            for col in range(self.minOldValue,self.minslider.GetValue()):
                self.dc.DrawRectangle(10+(self.classwidth*col), 100,
                                      self.classwidth/2, self.histogram[col]*-10)

        if self.maxOldValue>self.maxslider.GetValue():
            #color
            self.dc.SetBrush(wx.Brush("Blue"))
            for col in range(self.maxslider.GetValue(),self.maxOldValue):
                self.dc.DrawRectangle(20+(self.classwidth*col), 100,
                                      self.classwidth/2, self.histogram[col]*-10)                
        elif self.maxOldValue<self.maxslider.GetValue():
            #uncolor
            self.dc.SetBrush(wx.Brush("Black"))
            for col in range(self.maxOldValue,self.maxslider.GetValue()):
                self.dc.DrawRectangle(20+(self.classwidth*col), 100,
                                      self.classwidth/2, self.histogram[col]*-10)      
        self.maxOldValue=self.maxslider.GetValue()        
        self.minOldValue=self.minslider.GetValue()
        
if __name__=="__main__":
    app = wx.PySimpleApp(False)
    frame = wx.Frame(None, title="Draw on Panel")
    DrawPanel(frame)
    frame.Show(True)
    app.MainLoop()