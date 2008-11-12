#Martin Lacayo-Emery
#12/11/2008

import sys, struct
import dbftool



def rectangle(x,y,r):
    """
    returns the coordinates for a closed set of points forming a rectangle.
    The rectangle is centered at (x,y) and has a width of r
    """
    return [(x,y),(x,y+r),(x+r,y+r),(x+r,y),(x,y)]

def hexagonCentroids(startX,endX,startY,endY,r):
    """
    returns a list of the centorids for a hexagonal grid with spacing r
    """
    deltaY=r*(0.75**0.5)
    deltaX=float(r)

    #set the orgin
    hexX=startX
    hexY=startY

    points=[]
    for y in range(startY,endY):
        if (y-startY+2)%2:
            hexX=startX+(0.5*deltaX)
        else:
            hexX=startX
        for x in range(startX,endX):
            points.append((hexX,hexY))
            hexX+=deltaX
        hexY+=deltaY

    return points        

def hexagon(x,y,r):
    """
    returns the coordinates for a closed set of points froming a hexagon.
    The hexagon is centered at (x,y) and has a width of r
    """
    offset1=r/(3**0.5)
    offset2=r
    offset3=2*offset1
    return [(x,y+offset3),(x+offset2,y+offset1),
            (x+offset2,y-+offset1),(x,y-offset3),
            (x-offset2,y-offset1),(x-offset2,y+offset1),
            (x,y+offset3)]

class Shapefile:
    """
    Shapefile class supporting single point and single part polygon shapes.
    Shapes are passed in as a list of points.
    """
    def __init__(self,shapeType=1,Xmin=0,Ymin=0,Xmax=0,Ymax=0,Zmin=0,Zmax=0,Mmin=0,Mmax=0):
        self.fileCode=9994
        self.version=1000
        #number of 16-bit words
        self.size=50

        self.shapeType=shapeType
        self.Xmin=Xmin
        self.Ymin=Ymin
        self.Xmax=Xmax
        self.Ymax=Ymax
        self.Zmin=Zmin
        self.Zmax=Zmax
        self.Mmin=Mmin
        self.Mmax=Mmax

        self.shapes=[]        

    def add(self,shape):
        for p in shape:
            if p[0]<self.Xmin:
                self.Xmin=p[0]
            elif p[0]>self.Xmax:
                self.Xmax=p[0]
            if p[1]<self.Ymin:
                self.Ymin=p[1]
            elif p[1]>self.Ymax:
                self.Ymax=p[1]

        if self.shapeType==1:
            self.size+=10
            self.shapes.append(shape.pop())
        elif self.shapeType==5:
            self.size+=28+(8*len(shape))
            self.shapes.append(shape)

    def writeFile(self,outName):
        outShp=open(outName+".shp",'wb')
        outShx=open(outName+".shx",'wb')
        outDbf=open(outName+".dbf",'wb')
        self.write(outShp,outShx,outDbf)
        outShp.close()
        outShx.close()
        outDbf.close()

    def write(self,shp,shx,dbf):
        #shp file header
        #byte 0, File Code
        shp.write(struct.pack('>i', self.fileCode))
        #byte 4, Unused
        shp.write(struct.pack('>i', 0))
        #byte 8, Unused
        shp.write(struct.pack('>i', 0))
        #byte 12, Unused
        shp.write(struct.pack('>i', 0))
        #byte 16, Unused
        shp.write(struct.pack('>i', 0))
        #byte 20, Unused
        shp.write(struct.pack('>i', 0))
        #byte 24, File Length, total length of file in 16-bit words
        #this must be determined after file creation.
        shp.write(struct.pack('>i', self.size))
        #byte 28, Version, integer
        shp.write(struct.pack('<i', self.version))
        #byte 32, shape type
        shp.write(struct.pack('<i',self.shapeType))
        #byte 36, Bounding Box Xmin
        shp.write(struct.pack('<d',self.Xmin))
        #byte 44 Bounding Box Ymin
        shp.write(struct.pack('<d',self.Ymin))
        #byte 52 Bounding Box Xmax
        shp.write(struct.pack('<d',self.Xmax))
        #byte 60 Bounding Box Ymax
        shp.write(struct.pack('<d',self.Ymax))
        #byte 68* Bounding Box Zmin
        shp.write(struct.pack('<d',self.Zmin))
        #byte 76* Bounding Box Zmax
        shp.write(struct.pack('<d',self.Zmax))
        #byte 84* Bounding Box Mmin
        shp.write(struct.pack('<d',self.Mmin))
        #byte 92* Bounding Box Mmax
        shp.write(struct.pack('<d',self.Mmax))

        #shx file header
        #byte 0, File Code
        shx.write(struct.pack('>i', self.fileCode))
        #byte 4, Unused
        shx.write(struct.pack('>i', 0))
        #byte 8, Unused
        shx.write(struct.pack('>i', 0))
        #byte 12, Unused
        shx.write(struct.pack('>i', 0))
        #byte 16, Unused
        shx.write(struct.pack('>i', 0))
        #byte 20, Unused
        shx.write(struct.pack('>i', 0))
        #byte 24, File Length, total length of file in 16-bit words
        shx.write(struct.pack('>i', 50+(4*len(self.shapes))))
        #byte 28, Version, integer
        shx.write(struct.pack('<i', self.version))
        #byte 32, shape type
        shx.write(struct.pack('<i',self.shapeType))
        #byte 36, Bounding Box Xmin
        shx.write(struct.pack('<d',self.Xmin))
        #byte 44 Bounding Box Ymin
        shx.write(struct.pack('<d',self.Ymin))
        #byte 52 Bounding Box Xmax
        shx.write(struct.pack('<d',self.Xmax))
        #byte 60 Bounding Box Ymax
        shx.write(struct.pack('<d',self.Ymax))
        #byte 68* Bounding Box Zmin
        shx.write(struct.pack('<d',self.Zmin))
        #byte 76* Bounding Box Zmax
        shx.write(struct.pack('<d',self.Zmax))
        #byte 84* Bounding Box Mmin
        shx.write(struct.pack('<d',self.Mmin))
        #byte 92* Bounding Box Mmax
        shx.write(struct.pack('<d',self.Mmax))

        #write shapes
        if self.shapeType==1:
            contentLength=10
            for id,p in enumerate(self.shapes):
                #record header
                #record numbers start at 1
                shp.write(struct.pack('>i',id))
                #content length
                shp.write(struct.pack('>i',contentLength))

                #record contents
                #print float(i[0]),float(i[1])
                shp.write(struct.pack('<i',self.shapeType))
            
                shp.write(struct.pack('<d',p[0]))
                shp.write(struct.pack('<d',p[1]))

                #writing index records
                #size=record header+content length
                shx.write(struct.pack('>i',50+((contentLength+4)*id)))
                shx.write(struct.pack('>i',contentLength))
                               
        elif self.shapeType==5:
             for id,s in enumerate(self.shapes):
                contentLength=24+(8*len(s))
                #record header
                #record numbers start at 1
                shp.write(struct.pack('>i',id))
                #content length
                shp.write(struct.pack('>i',contentLength))

                #record contents
                shp.write(struct.pack('<i',self.shapeType))

                #bound box for polygon
                temp=apply(zip,s)
                box=map(min,temp)+map(max,temp)
                for m in box:
                    shp.write(struct.pack('<d',m))

                #number of parts        
                shp.write(struct.pack('<i',1))
                #number of points
                shp.write(struct.pack('<i',len(s)))
                #parts index
                shp.write(struct.pack('<i',0))

                #points
                for p in s:
                    #shape type for point
                    #x coordinate
                    shp.write(struct.pack('<d',float(p[0])))
                    #y coordinate
                    shp.write(struct.pack('<d',float(p[1])))

                #writing index records
                #size=record header+content length
                shx.write(struct.pack('>i',50+((contentLength+4)*id)))
                shx.write(struct.pack('>i',contentLength))
                
        dbftool.dbfwriter(dbf, ["default"], [('N', 1, 6)], [[0]]*len(self.shapes))


if __name__=="__main__":
    print
    s=Shapefile(shapeType=5)
    for p in hexagonCentroids(0,11,0,11,1):
        s.add(hexagon(p[0],p[1],0.5))
    s.writeFile("E:/Data/test")