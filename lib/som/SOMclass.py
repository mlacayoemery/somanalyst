#Martin Lacayo-Emery

import decimal
import random
from ..shp import databasefile
from ..shp import shapefile
from ..shp import geometry

idRow=True

def qError(v1,v2):
    return sum(map(lambda v: (v[0]-v[1])**2,zip(v1,v2)))**0.5

def round6(x):
    return round(x,6)

class BMU:
    """
    A class to store best matching unit data
    """
    def __init__(self):
        dimensions=0
        topology=""
        xdimension=0
        ydimension=0
        neighborhoodType=""
        vectors=[]
        comments={}
        labels=[]
        spacing=1
        distance=0
        xOrigin=0
        yOrigin=0
        quadrant=1
        self.dimensions=dimensions
        self.topology=topology
        self.xdimension=xdimension
        self.ydimension=ydimension
        self.neighborhoodType=neighborhoodType
        self.vectors=vectors
        self.comments=comments
        self.labels=labels
        self.spacing=spacing
        self.distance=distance
        self.xOrigin=xOrigin
        self.yOrigin=yOrigin
        self.quadrant=quadrant

    def readFile(self,inName):
        inFile=open(inName)
        self.read(inFile)
        inFile.close()

    def read(self,inFile):
        #parse and typecast the header
        self.dimensions,self.topology,self.xdimension,self.ydimension,self.neighborhoodType=inFile.readline().strip().split()
        self.dimensions=int(self.dimensions)-1
        self.xdimension=int(self.xdimension)
        self.ydimension=int(self.ydimension)

        #validate header values
        if self.dimensions<0:
            raise ValueError, str(self.dimensions)+" is not a supported number of dimensions, only natural numbers are supported."
        if self.topology!="hexa" and self.topology!="rect":
            raise ValueError, str(self.topology)+" is not a supported topology, only \"hexa\" or \"rect\" is supported."
        if self.xdimension<0:
            raise ValueError, str(self.xdimension)+" is not a supported X dimension, only natural numbers are supported."
        if self.ydimension<0:
            raise ValueError, str(self.ydimension)+" is not a supported Y dimension, only natural numbers are supported."
        if self.neighborhoodType!="gaussian" and self.neighborhoodType!="bubble":
            raise ValueError, str(self.neighborhoodType)+" is not a supported neighborhood type, only \"gaussian\" or \"bubble\" is supported."

        #read comments, read ahead and skip back if not comment
        loc=inFile.tell()
        line=inFile.readline().strip().split()
        while line[0][0]=="#":
            self.comments[line[0]]=line[1:]
            loc=inFile.tell()
            line=inFile.readline().strip().split()
        inFile.seek(loc)

        #read in som in row major order
        self.vectors=[]
        self.labels=[]
        for line in inFile.readlines():
            l=line.strip().split()
            self.vectors.append(map(int,l[:2]))
            self.labels.append(l[2:])
        
    def writeShapefile(self,inName):
        shp=shapefile.Shapefile(1)
        if self.quadrant==1:
            xscale=1
            yscale=1
        elif self.quadrant==2:
            xscale=-1
            yscale=1
        elif self.quadrant==3:
            xscale=-1
            yscale=-1
        elif self.quadrant==4:
            xscale=1
            yscale=-1
        else:
            raise ValueError, str(quadrant)+" invalid quadarant. Must be 1, 2, 3, or 4."        

        if self.distance==0:
            for i,j in self.vectors:
                x,y=geometry.hexagonCentroid(i,j,self.xOrigin,self.yOrigin,self.spacing)
                shp.add([(x*xscale,y*yscale)])
        else:        
            for i,j in self.vectors:
                x,y=geometry.hexagonCentroid(i,j,self.xOrigin,self.yOrigin,self.spacing)
                xShift=((random.random()*2)-1)*self.distance
                x=x+xShift
                yMaxShift=(self.distance**2-xShift**2)**0.5
                yShift=((random.random()*2)-1)*yMaxShift
                y=y+yShift
                shp.add([(x*xscale,y*yscale)])
            
        shp.writeFile(inName[:inName.rfind(".")])

    def writeDBF(self,outName):
        self.DBF.writeFile(outName)

    def DBF(self):
        #print self.la
        labelLen=len(self.labels[0])
        fieldspecs=(zip(['N']*self.dimensions,[0]*self.dimensions,[0]*self.dimensions)+
                    zip(['C']*labelLen,[0]*labelLen,[0]*labelLen))
        if self.comments.has_key("#n"):
            fieldnames=self.comments["#n"]
        else:
            fieldnames=["Xindex","Yindex","Qerror"]+map("attr".__add__,map(str,range(1,self.dimensions+labelLen-3)))
        #print fieldspecs
        if idRow:
            dbf=databasefile.DatabaseFile(["ID"]+fieldnames,[('N', 6, 0)]+fieldspecs,[])
            for id,v in enumerate(self.vectors):
                dbf.addRow([id+1]+v+self.labels[id])
        else:
            dbf=databasefile.DatabaseFile(fieldnames,fieldspecs,[])
            for id,v in enumerate(self.vectors):
                dbf.addRow(v+self.labels[id])
        dbf.dynamicSpecs()
        #print dbf.fieldspecs
        #print dbf.records
        return dbf            

class DAT:
    """
    A class to store vector data
    """
    def __init__(self):
        dimensions=0
        vectors=[]
        comments={}
        labels=[]
        self.dimensions=dimensions
        self.vectors=vectors
        self.comments=comments
        self.labels=labels

    def readFile(self,inName):
        """
        reads SOM vector data from a file name
        """
        inFile=open(inName,'r')
        self.read(inFile)
        inFile.close()

    def read(self,inFile):
        """
        """
        self.dimensions=int(inFile.readline())
        if self.dimensions<0:
            raise ValueError, str(self.dimensions)+" is not a supported number of dimensions, only natural numbers are supported."

        #read comments
        loc=inFile.tell()
        line=inFile.readline().strip().split()
        self.comments={}
        while line[0][0]=="#":
            self.comments[line[0]]=line[1:]
            loc=inFile.tell()
            line=inFile.readline().strip().split()
        inFile.seek(loc)

        #read in vectors and labels
        self.vectors=[]
        self.labels=[]
        lines=[l.strip().split() for l in inFile.readlines()]
        for l in lines:
            self.vectors.append(map(float,l[:self.dimensions]))
            self.labels.append(l[self.dimensions:])

    def readCSVfile(self,inName,labelColumns=[]):
        """
        opens a CSV file stream, keeps collumns names in nonnumeric as labels
        """
        inFile=open(inName)
        self.readCSV(inFile,labelColumns)
        inFile.close()

    def readLATfile(self,inName):
        """
        opens a CSV file stream, assumes non-numeric data in columns named "Locus" or "Attribute" or "Time"
        """
        self.readCSVfile(inName,["Locus","Attribute","Time"])

    def readCSV(self,inFile,labelColumns):
        """
        """
        self.comments["#n"]=inFile.readline().strip().split(",")
        self.dimensions=len(self.comments["#n"])-len(labelColumns)

        #convert label column names into indicies        
        indicies=[]
        for l in labelColumns:
            indicies.append(self.comments["#n"].index(l))
        indicies.sort(reverse=True)
        temp=[]
        for i in indicies:
            temp.append(self.comments["#n"].pop(i))
        self.comments["#n"].extend(temp)

        #read in data
        self.labels=[]
        self.vectors=[]
        lines=[l.strip().split(",") for l in inFile.readlines()]
        for l in lines:
            tempLabels=[]
            for i in indicies:
                tempLabels.append(l.pop(i))
            self.labels.append(tempLabels)
            self.vectors.append(map(float,l))
            
            

    def writeFile(self,outName):
        """
        """
        outFile=open(outName,'w')
        self.write(outFile)
        outFile.close()

    def write(self,outFile):
        """
        """
        outFile.write(str(self.dimensions))
        for k in self.comments.keys():
            outFile.write("\n"+k+" "+" ".join(self.comments[k]))
        for v,l in zip(self.vectors,self.labels):
            outFile.write("\n"+" ".join(map(str,v)+l))

    def writeShapefile(self,outName):
        pass

    def writeShape(self,outFile):
        pass

    def writeDBF(self,outFile):
        self.DBF().writeFile(outFile)

    def DBF(self):
        fieldspecs=([['N',1,5]]*self.dimensions)+([['C',1,0]]*(len(self.labels[0])))
        if self.comments.has_key("#n"):
            fieldnames=self.comments["#n"]
        else:
            fieldnames=map("attr".__add__,map(str,range(1,self.dimensions+1+len(self.labels[0]))))
        if fieldnames[-1]=="Qerror":
            fieldspecs[-1]=['N',1,5]
        dbf=databasefile.DatabaseFile(fieldnames,fieldspecs,[])
        dbf.dynamicSpecs()
        for id,v in enumerate(self.vectors):
            dbf.addRow(v+self.labels[id])
            for id,l in enumerate(map(len,map(str,v))):
                if l>fieldspecs[id][1]:
                    fieldspecs[id][1]=l
            for id,l in enumerate(map(len,self.labels[id])):
                if l>fieldspecs[self.dimensions+id-1][1]:
                    fieldspecs[self.dimensions+id-1][1]=l
        return dbf


class SOM:
    """
    A class to store self-organizing maps.
    """

    #initializers    
    def __init__(self):
        dimensions=0
        topology=""
        xdimension=0
        ydimension=0
        neighborhoodType=""
        vectors=[]
        comments={}
        labels=[]
        self.dimensions=dimensions
        self.topology=topology
        self.xdimension=xdimension
        self.ydimension=ydimension
        self.neighborhoodType=neighborhoodType
        self.vectors=vectors
        self.comments=comments
        self.labels=labels

    #search
    def bestMatch(self,vector,decimals=5):
        """
        returns the indicies and quantization error for the neuron that best matches the input vector
        """
        #find the best matching unit, return its coordinates
        x,y=0,0
        minError=qError(self.vectors[0][0],vector)
        for i in range(self.ydimension):
            for j in range(self.xdimension):
                q=qError(self.vectors[i][j],vector)
                if q<minError:
                    x,y,minError=j,i,q
        return x,y,round(minError,decimals)

    def batchMatch(self,vectorList):
        """
        returns the indicies and quantization error for the neuron that best matches each of the input vectors
        """
        matches=[]
        for v in vectorList:
            matches.append(self.bestMatch(v))
        return matches

    def writeMatchFile(self,vectorList,outName):
        """
        writes the results of a batch match to the filename
        """
        #open file stream, call self.writeMatch()        
        outFile=open(outName,'w')
        self.writeMatch(vectorList,outFile)
        outFile.close()

    def writeMatch(self,vectorList,outFile):
        """
        writes the results of a batch match to the file stream
        """
        #batch match vectors, write to file stream
        matches=self.batchMatch(vectorList)
        outFile.write(" ".join(map(str,[self.dimensions,self.topology,self.xdimension,self.ydimension,self.neighborhoodType])))
        for m in matches:
            outFile.write("\n"+" ".join(map(str,m)))
        
    def readFile(self,inName):
        """
        reads in a codebook file into the SOM class from a filename
        """
        #open file stream, call self.read()
        inFile=open(inName,'r')
        self.read(inFile)
        inFile.close()

    def read(self,inFile):
        """
        reads in a codebook file into the SOM class from a file stream
        """

        #parse and typecast the header
        self.dimensions,self.topology,self.xdimension,self.ydimension,self.neighborhoodType=inFile.readline().strip().split()
        self.dimensions=int(self.dimensions)
        self.xdimension=int(self.xdimension)
        self.ydimension=int(self.ydimension)

        #validate header values
        if self.dimensions<0:
            raise ValueError, str(self.dimensions)+" is not a supported number of dimensions, only natural numbers are supported."
        if self.topology!="hexa" and self.topology!="rect":
            raise ValueError, str(self.topology)+" is not a supported topology, only \"hexa\" or \"rect\" is supported."
        if self.xdimension<0:
            raise ValueError, str(self.xdimension)+" is not a supported X dimension, only natural numbers are supported."
        if self.ydimension<0:
            raise ValueError, str(self.ydimension)+" is not a supported Y dimension, only natural numbers are supported."
        if self.neighborhoodType!="gaussian" and self.neighborhoodType!="bubble":
            raise ValueError, str(self.neighborhoodType)+" is not a supported neighborhood type, only \"gaussian\" or \"bubble\" is supported."

        #read comments, read ahead and skip back if not comment
        loc=inFile.tell()
        line=inFile.readline().strip().split()
        while line[0][0]=="#":
            self.comments[line[0]]=line[1:]
            loc=inFile.tell()
            line=inFile.readline().strip().split()
        inFile.seek(loc)

        #read in som in row major order
        self.vectors=[]
        self.labels=[]
        for i in range(self.ydimension):
            row=[]
            rowLabels=[]
            for j in range(self.xdimension):
                #read in one neuron, keep extra values as labels
                line=inFile.readline().strip().split()
                row.append(map(float,line[:self.dimensions]))
                rowLabels.append(line[self.dimensions:])            
            self.vectors.append(row)
            self.labels.append(rowLabels)

        #read in remaining lines as comments
        for id,l in enumerate(inFile.readlines()):
            self.comments["comment"+str(id)]=l
                    

    def writeFile(self,outName):
        """
        writes a codebook file to the filename
        """
        #open file stream, call self.write()
        outFile=open(outName,'w')
        self.write(outFile)
        outFile.close()

    def write(self,outFile):
        """
        writes a codebook file to the file stream
        """
        #write header
        outFile.write(" ".join(map(str,[self.dimensions,self.topology,self.xdimension,self.ydimension,self.neighborhoodType])))

        #write commments        
        for k in self.comments.keys():
            outFile.write("#"+''.join(self.comments[k]))

        #write vectors            
        for i in range(self.xdimension):
            for j in range(self.ydimension):
                outFile.write("\n"+" ".join(map(str,self.vectors[j][i])+self.labels[j][i]))

    def writeDBFfile(self,outName):
        outFile=open(outName,'wb')
        self.writeDBF(outFile)
        outFile.close()

    def writeDBF(self,outFile):
        self.DBF().write(outFile)

    def DBF(self):
        fieldspecs=([['N',1,5]]*self.dimensions)+([['C',1,0]]*(len(self.labels[0][0])))
        if self.comments.has_key("#n"):
            fieldnames=self.comments["#n"]
        else:
            fieldnames=map("attr".__add__,map(str,range(1,self.dimensions+1+len(self.labels[0][0]))))
        if fieldnames[-1]=="Qerror":
            fieldspecs[-1]=['N',1,5]
        dbf=databasefile.DatabaseFile(fieldnames,fieldspecs,[])
        dbf.dynamicSpecs()
        for i in range(self.ydimension):
            for j in range(self.xdimension):
                dbf.addRow(self.vectors[i][j]+self.labels[i][j])
                for id,l in enumerate(map(len,map(str,self.vectors[i][j]))):
                    if l>fieldspecs[id][1]:
                        fieldspecs[id][1]=l
                for id,l in enumerate(map(len,self.labels[i][j])):
                    if l>fieldspecs[self.dimensions+id][1]:
                        fieldspecs[self.dimensions+id][1]=l
        return dbf

    def matchLabel(self,vectors,labels,comments):
        if self.labels==[]:
            for i in range(self.ydimension):
                row=[]
                for j in range(self.xdimension):
                    row.append([])
                self.labels.append(row)
            
        for i in range(self.ydimension):
            for j in range(self.xdimension):
                matchIndex,matchQerror=0,qError(self.vectors[i][j],vectors[0])
                for id,v in enumerate(vectors):
                    tempQerror=qError(self.vectors[i][j],v)
                    if tempQerror<matchQerror:
                        matchIndex=id
                        matchQerror=tempQerror
                self.labels[i][j].extend(labels[matchIndex]+[str(matchQerror)])

        if self.comments.has_key("#n"):
            self.comments["#n"].extend(map("attr".__add__,map(str,range(1,len(labels[0])+1)))+["Qerror"])
        elif comments.has_key("#n"):
            self.comments["#n"]=comments["#n"]+["Qerror"]

##if __name__=="__main__":
##    d = DAT()
##    s = SOM()
##    d.readFile("E:/Data/data (2).txt")
##    s.readFile("E:/Data/init.cod")
##    s.matchLabel(d.vectors,d.labels)
##    s.writeDBFfile("E:/Data/init.dbf")
##    d.writeMatchFile(s,"E:/Data/bmu.txt")
