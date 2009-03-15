import sys

def Mac2PC(inName,outName):
    inFile=open(inName)
    outFile=open(outName,'w')

    outFile.write(inFile.readline().replace("\r","\n"))    

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    Mac2PC(inName,outName)