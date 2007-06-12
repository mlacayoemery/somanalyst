class GCF:
    def __init__ (self, dim, topo="", x=-1, y=-1, hood="", nodes=[],name="",centroidsDist=1):
        #file parsing
        if type(dim)==int:
            self.dim=dim
            self.topo=topo
            self.x=x
            self.y=y
            self.hood=hood
            self.nodes=nodes
        elif type(dim)==file:
            format=dim.readline().split()
            self.dim=int(format[0])
            self.topo=format[1]
            self.x=int(format[2])
            self.y=int(format[3])
            self.hood=format[4]
            self.nodes=[map(float,i.split()) for i in dim.readlines()]

        self.centroidsDist=centroidsDist
        self.centroids=[]
        self.polygons=[]

        ##Centroids
        #neurons listed from left to right, top to bottom
        if self.topo=="rect":
            for lcvY in range(self.y):
                #loop over colomuns
                for lcvX in range(self.x,0,-1):
                    self.centroids.append([float(lcvX*self.centroidsDist),float(lcvY*self.centroidsDist)])
        elif self.topo=='hexa':
            #caluclate the changes for centroids
            deltaY=self.centroidsDist*((3.0/4)**0.5)
            deltaX=self.centroidsDist*float(1)

            #set the orgin to start at 0,0 for the first point
            hexX=0-deltaX
            hexY=0
            for lcvY in range(self.y):
                for lcvX in range(self.x):
                    #increment x coordinate
                    hexX=hexX+deltaX
                    self.centroids.append([hexX,hexY])

                #offset x coordinate for alternating rows        
                if (lcvY+1)%2:
                    hexX=0-(deltaX/2)
                else:
                    hexX=0-deltaX
                #increment y coordinate
                hexY=hexY+deltaY

        ##Polygons
        if self.topo=="rect":
            for i in self.centroids:
                #center point
                pX=i[0]
                pY=i[1]
                #derive extrema
                minX=pX-(0.5*self.centroidsDist)
                maxX=pX+(0.5*self.centroidsDist)
                minY=pY-(0.5*self.centroidsDist)
                maxY=pY+(0.5*self.centroidsDist)
                #bounding box
                Box=[minX,minY,maxX,maxY]
                #starts from top most, left most, and goes clock-wise
                Points=[Box,[[minX,maxY],[maxX,maxY],[maxX,minY],[minX,minY]]]
                self.polygons.append(Points)

        elif self.topo=='hexa':
            for i in self.centroids:
                #center point
                pX=i[0]
                pY=i[1]
                #sides numberd in order of min length
                side2=0.5*self.centroidsDist
                side1=side2/(3**0.5)
                side3=2*side1
                #derive extreama
                minX=pX-side2
                maxX=pX+side2
                minY=pY-side3
                maxY=pY+side3
                #bounding box
                Box=[minX,minY,maxX,maxY]
                #starts from top most, left most, and goes clock-wise        
                Points=[Box,[[pX,pY+side3],[pX+side2,pY+side1],[pX+side2,pY-side1],[pX,pY-side3],[pX-side2,pY-side1],[pX-side2,pY+side1]]]
                self.polygons.append(Points)
                    
        #create name of parameters joined with spaces
        if name == "":
            self.name=" ".join(map(str,[self.dim,self.topo,self.x,self.y,self.hood]))
        else:
            self.name=name

    def __str__ (self):
        return self.name

    def __getitem__ (self,i):
        return self.nodes[i]

    def __len__ (self):
        return len(self.nodes)