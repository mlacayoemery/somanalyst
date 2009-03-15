class FileHeader:
    def __init__ (FileCode=9994,NA1=0,NA2=0,NA3=0,NA4=0,NA5=0,
                  FileLength=50,version=1000,shptype=0,
                  Xmin=0.0,Ymin=0.0,Xmax=0.0,Ymax=0.0,
                  Zmin=0.0,Zmax=0.0,Mmin=0.0,Mmax=0.0):
        self.FileCode=FileCode
        self.NA1=NA1
        self.NA2=NA2
        self.NA3=NA3
        self.NA4=NA4
        self.NA5=NA5
        self.FileLength=FileLength
        self.version=version
        self.shptype=shptype
        self.Xmin=Xmin
        self.Ymin=Ymin
        self.Xmax=Xmax
        self.Ymax=Ymax
        self.Zmin=Zmin
        self.Zmax=Zmax
        self.Mmin=Mmin
        self.Mmax=Mmax
        self.FileLength=FileLength
        self.bytes=""

    def __str__(self):
        return self.bytes

    def __eq__ (self,i):
        if self.ShapeType==1:
            self.FileLength=50+(10*i)
        elif shapeType==5:
            if topology=='rect':
                self.FileLength=50+(56*i)
            elif topology=='hexa':
                self.FileLength=50+(72*i)
      
    def __addeq__ (self,i):
        if self.ShapeType==1:
            self.FileLength+=10*i
        elif shapeType==5:
            if topology=='rect':
                self.FileLength+=56*i
            elif topology=='hexa':
                self.FileLength+=72*i

    def pack (self):
        self.bytes=struct.pack('>i', self.FileCode)
        self.bytes+=struct.pack('>i', self.NA1)
        self.bytes+=struct.pack('>i', self.NA2)
        self.bytes+=struct.pack('>i', self.NA3)
        self.bytes+=struct.pack('>i', self.NA4)
        self.bytes+=struct.pack('>i', self.NA5)
        self.bytes+=struct.pack('>i', self.FileLength)
        self.bytes+=struct.pack('<i', self.version)
        self.bytes+=struct.pack('<i',self.ShapeType)
        self.bytes+=struct.pack('<d',self.Xmin)
        self.bytes+=struct.pack('<d',self.Ymin)
        self.bytes+=struct.pack('<d',self.Xmax)
        self.bytes+=struct.pack('<d',self.Ymax)
        self.bytes+=struct.pack('<d',self.Zmin)
        self.bytes+=struct.pack('<d',self.Zmax)
        self.bytes+=struct.pack('<d',self.Mmin)
        self.bytes+=struct.pack('<d',self.Mmax)                
