#Martin Lacayo-Emery

def qError(v1,v2):
    return sum(map(lambda v: (v[0]-v[1])**2,zip(v1,v2)))**0.5

class DAT:
    """
    A class to store vector data
    """
    def __init__(self,dimensions=None,vectors=None):
        self.dimensions=dimensions
        self.vectors=vectors

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
        self.vectors=[map(float,v.strip().split()[:self.dimensions]) for v in inFile.readlines()]

    def writeMatchFile(self,s,outName):
        s.writeMatchFile(self.vectors,outName)

class SOM:
    """
    A class to store self-organizing maps.
    """

    #initializers    
    def __init__(self,dimensions=None,topology=None,xdimension=None,ydimension=None,neighborhoodType=None,vectors=None):
        self.dimensions=dimensions
        self.topology=topology
        self.xdimension=xdimension
        self.ydimension=ydimension
        self.neighborhoodType=neighborhoodType
        self.vectors=vectors

    #search
    def bestMatch(self,vector,decimals=5):
        """
        returns the indicies and quantization error for the neuron that best matches the input vector
        """
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
        outFile=open(outName,'w')
        self.writeMatch(vectorList,outFile)
        outFile.close()

    def writeMatch(self,vectorList,outFile):
        """
        writes the results of a batch match to the file stream
        """
        matches=self.batchMatch(vectorList)
        outFile.write(" ".join(map(str,[self.dimensions,self.topology,self.xdimension,self.ydimension,self.neighborhoodType])))
        for m in matches:
            outFile.write("\n"+" ".join(map(str,m)))
        
    def readFile(self,inName):
        """
        reads in a codebook file into the SOM class from a filename
        """
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

        #skip comments
        loc=inFile.tell()
        while inFile.readline()[0]=="#":
            loc=inFile.tell()
        inFile.seek(loc)

        #read in som
        self.vectors=[]
        for i in range(self.ydimension):
            row=[]
            for j in range(self.xdimension):
                #read in one neuron, skip extra values, and typecast values
                row.append(map(float,inFile.readline().strip().split()[:self.dimensions]))
            self.vectors.append(row)

    def writeFile(self,outName):
        """
        writes a codebook file to the filename
        """        
        outFile=open(outName,'w')
        self.write(outFile)
        outFile.close()

    def write(self,outFile):
        """
        writes a codebook file to the file stream
        """
        outFile.write(" ".join(map(str,[self.dimensions,self.topology,self.xdimension,self.ydimension,self.neighborhoodType])))
        for i in range(self.xdimension):
            for j in range(self.ydimension):
                outFile.write("\n"+" ".join(map(str,self.vectors[i][j])))


if __name__=="__main__":
    s = SOM()
    d = DAT()
    s.readFile("E:/Data/init.cod")
    d.readFile("E:/Data/data.txt")
    d.writeMatchFile(s,"E:/Data/bmu.txt")
