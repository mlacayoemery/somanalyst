import fHeader, rHeader

class SHP:
    def __init__ (FileCode=9994,NA1=0,NA2=0,NA3=0,NA4=0,NA5=0,
                  length=0,version=1000,shptype=0,
                  Xmin=0.0,Ymin=0.0,Xmax=0.0,Ymax=0.0,
                  Zmin=0.0,Zmax=0.0,Mmin=0.0,Mmax=0.0,
                  FileLength=0):
        self.header=fHeader(FileCode,NA1,NA2,NA3,NA4,NA5,
                            length,version,shptype,
                            Xmin,Ymin,Xmax,Ymax,
                            Zmin,Zmax,Mmin,Mmax)
        self.rheader=[]
        self.bytes=""

    def __str__ (self):
        self.pack()
        return self.bytes
    
    def addRecord (self,location,length):
        self.header+=1
        self.rheader.append(rheader(location,length))
 
    def pack(self):
        self.header.pack()
        self.bytes=str(self.header)
        for i in self.rheader:
            self.bytes+=i

        