import struct, dbftool

class Shapefile:
    def __init__(self,type,fieldnames,fieldspecs,fieldrecords):
        self.spatial=SHP(type)
        self.table=DBF(fieldnames,fieldspecs,fieldrecords)

    def addRecord(self,shape,record):
        self.spatial.addRecord(shape)
        self.table.addRecord(record)

    def write(self,stem):
        ofile=open(stem+".shp",'wb')
        ofile.write(str(self.spatial))
        ofile.close()
        ofile=open(stem+".shx",'wb')
        ofile.write(self.spatial.index())
        ofile.close()
        ofile=open(stem+".dbf",'wb')
        ofile.write(str(self.table))
        ofile.close()

class SHP:
    def __init__(self,Type):
        self.iterator=0
        self.FileCode=9994
        self.Unused=[0,0,0,0,0]
        self.Length=50
        self.Version=1000
        self.Type=Type
        self.BoxXY=BoxRecord([0,0,0,0])
        self.BoxZM=BoxRecord([0,0,0,0])
        self.Records=[]

    def addRecord(self,record):
        if self.Records == []:
            self.BoxXY.minX=record['minX']
            self.BoxXY.minY=record['minY']
            self.BoxXY.maxX=record['maxX']
            self.BoxXY.maxY=record['maxY'] 
            
        if record.Type==self.Type:
            self.Records.append(record)
            self.Length+=len(record)
            if record['minX']<self.BoxXY.minX:
                self.BoxXY.minX=record['minX']
            if record['minY']<self.BoxXY.minY:
                self.BoxXY.minY=record['minY']
            if record['maxX']>self.BoxXY.maxX:
                self.BoxXY.maxX=record['maxX']
            if record['maxY']>self.BoxXY.maxY:
                self.BoxXY.maxY=record['maxY']
        else:
            raise TypeError
                            
    def __str__(self):
        record=struct.pack('>i', self.FileCode)
        for i in self.Unused:
            record+=struct.pack('>i', i)
        record+=struct.pack('>i', self.Length)
        
        record+=struct.pack('<i', self.Version)
        record+=struct.pack('<i', self.Type)

        record+=str(self.BoxXY)
        record+=str(self.BoxZM)
        

        
        for id,r in enumerate(self.Records):
            record+=struct.pack('>i', id)
            record+=struct.pack('>i', len(r))
            #record+="\xFF\xFF"
            record+=str(r)
            
        return record

    #define the iterator function    
    def __iter__(self):
        return self
    
    def next(self):
        if self.iterator > (len(records)-1):
            self.iterator=0
            raise StopIteration
        else:
            self.iterator+=1
            return self.Records[self.iterator]

    def index(self):
        record=struct.pack('>i', self.FileCode)
        for i in self.Unused:
            record+=struct.pack('>i', i)
        record+=struct.pack('>i', 50+(4*len(self.Records)))
        record+=struct.pack('<i', self.Version)
        record+=struct.pack('<i', self.Type)
        record+=str(self.BoxXY)
        record+=str(self.BoxZM)
        #first offset
        offset=50
        for r in self.Records:
            record+=struct.pack('>i', offset)
            record+=struct.pack('>i', len(r))
            #record+="\xFF"
            offset+=len(r)+4
        return record

    def __getitem__(self,i):
        return self.Records[i]

#returns the mins and maxes in a point set
#returns a list in minX,minY,maxX,maxY order
def minmaxXY(points):
    minX=points[0][0]
    minY=points[0][1]
    maxX=points[0][0]
    maxY=points[0][1]
    for x,y in points:
        if x<minX:
            minX=x
        if y<minY:
            minY=y
        if x>maxX:
            maxX=x
        if y>maxY:
            maxY=y
    return [minX, minY, maxX, maxY]
        

#bounding box class
#extracts extrema from a list
#the list must be in minX,minY,maxX,maxY order
class BoxRecord:            
    def __init__(self,extrema):
        for minX,minY,maxX,maxY in [extrema]:
            self.minX=float(minX)
            self.minY=float(minY)
            self.maxX=float(maxX)
            self.maxY=float(maxY)

    def __str__(self):
        record=struct.pack('<d',self.minX)
        record+=struct.pack('<d',self.minY)
        record+=struct.pack('<d',self.maxX)
        record+=struct.pack('<d',self.maxY)
        return record
        
###point stored as individual coordinates
##class Point:
##    def __init__(self,X,Y):
##        #index for interator
##        self.index=0
##        self.X=float(X)
##        self.Y=float(Y)
##

    
#point stored as individual coordinates with shape type
class PointRecord:
    def __init__(self,X,Y):
        self.index=0
        self.Type=int(1)
        self.X=float(X)
        self.Y=float(Y)

    def __str__(self):
        record=struct.pack('<i',self.Type)
        record+=struct.pack('<d',self.X)
        record+=struct.pack('<d',self.Y)
        return record

    def __getitem__(self,i):
        if i=="minX":
            return self.X
        if i=="minY":
            return self.Y
        if i=="maxX":
            return self.X
        if i=="maxY":
            return self.Y  

    #length of the record in 16-bit words
    def __len__(self):
        return 10
        
#parts contains a list of indicie
#parts begins at 0
class PolyLineRecord:
    def __init__(self,points,parts):
        self.Type=int(3)
        self.Box=BoxRecord(minmaxXY(points))
        self.NumParts=len(parts)
        self.NumPoints=len(points)
        self.Parts=parts
        self.Points=points

    def __str__(self):
        record=struct.pack('<i',self.Type)
        record+=str(self.Box)
        record+=struct.pack('<i',self.NumParts)
        record+=struct.pack('<i',self.NumPoints)
        for i in self.Parts:
            record+=struct.pack('<i',i)
        for x,y in self.Points:
            record+=struct.pack('<d',x)
            record+=struct.pack('<d',y)
        return record

    #length of the record in 16-bit words
    def __len__(self):
        return 22 + (2*self.NumParts) + (4*2*self.NumPoints)

    def __getitem__(self,i):
        if i=="minX":
            return self.Box.minX
        if i=="minY":
            return self.Box.minY
        if i=="maxX":
            return self.Box.maxX
        if i=="maxY":
            return self.Box.maxY  

#parts contains a list of indicie
class PolygonRecord(PolyLineRecord):
    def __init__(self,points,parts):
        self.Type=int(5)
        self.Box=BoxRecord(minmaxXY(points))
        self.NumParts=len(parts)
        self.NumPoints=len(points)
        self.Parts=parts
        self.Points=points
      

############
class DBF:
    def __init__(self,fieldnames,fieldspecs,records):
        self.fieldnames=fieldnames
        self.fieldspecs=fieldspecs
        self.records=records

    def addRecord(self, record):
        self.records.append(record)

    def __str__(self):
        ver=3
        yr=34
        mon=7
        day=11
        numrec = len(self.records)
        numfields = len(self.fieldspecs)
        lenheader = numfields * 32 + 33
        lenrecord = sum(field[1] for field in self.fieldspecs) + 1

        record = struct.pack('<BBBBLHH20x', ver, yr, mon, day, numrec, lenheader, lenrecord)

        # field specs
        for i in range(len(self.fieldnames)):
            name=self.fieldnames[i-1].ljust(11, '\x00')
            typ=self.fieldspecs[i-1][0]
            size=self.fieldspecs[i-1][1]
            deci=self.fieldspecs[i-1][2]

            record+=struct.pack('<11sc4xBB14x', name, typ, size, deci)
        record+='\r'

        for r in self.records:
            #deletion flag
            record+=' '
            for i,value in enumerate(r):
                typ=self.fieldspecs[i][0]
                size=self.fieldspecs[i][1]
                deci=self.fieldspecs[i][2]
                if typ == 'N':
                    value = str(value).rjust(size, ' ')
                elif typ == 'D':
                    value = value.strftime('%Y%m%d')
                elif typ == 'L':
                    value = str(value)[0].upper()
                else:
                    value = str(value)[:size].ljust(size, ' ')
                record+=value
        # End of file
        record+='\x1A'
        return record

#######      
if __name__ == "__main__":
    temp=Shapefile(5,["temp"],[('C',10,0)],[])
    for i in range(10):
        for j in range(10):
            temp.addRecord(PolygonRecord([[j,i],[j,i+1],[j+1,i+1],[j+1,i],[j,i]],[0]),["Hello"])
    temp.write("E:/mlacayo/SOManalyst/final")
    ##    for i in range(10):
##        for j in range(10):
##            temp.addRecord(PointRecord(i,j))
    

    
    
    
    
