class Content:
    def __init__(self,ShapeType=0,Xmin=0.0,Ymin=0.0,Xmax=0.0,Ymax=0.0,NumParts=0,NumPoints=0,Parts=[0],Points=[]):
        #Null Shape
        if ShapeType==0:
            self.ShapeType=ShapeType

            #pack
            self.bytes=struct.pack('<i',self.ShapeType)
        #Point
        elif ShapeType==1:
            self.ShapeType=ShapeType
            self.X=Points[0][0]
            self.Y=Points[0][1]

            #pack
            self.bytes=struct.pack('<i',self.ShapeType)
            self.bytes+=struct.pack('<d',self.X)
            self.bytes+=struct.pack('<d',self.Y)
            
        #Polygon
        elif ShapeType==5:
            self.ShapeType=ShapeType

            #Box
            self.Xmin=Xmin
            self.Ymin=Ymin
            self.Xmax=Xmax
            self.Ymax=Ymax

            self.NumParts=NumParts
            self.NumPoints=NumPoints
            self.Parts=Parts
            self.Points=Points

            #pack
            self.bytes=struct.pack('<i',ShapeType)

            #box
            self.bytes+=struct.pack('<d',self.Xmin)
            self.bytes+=struct.pack('<d',self.Ymin)
            self.bytes+=struct.pack('<d',self.Xmax)
            self.bytes+=struct.pack('<d',self.Ymax)

            self.bytes+=struct.pack('<i',self.NumParts)
            self.bytes+=struct.pack('<i',self.NumPoints)

            #parts index    
            for i in self.Parts:
                self.bytes+=struct.pack('<i',i)

            #points            
            for p in self.Points:
                self.bytes+=struct.pack('<d',p[0])
                self.bytes+=struct.pack('<d',p[1])

    def __str__ (self):
        return self.bytes
    