import sys

def UnixToWin(inName,outName):
    inFile=open(inName)
    outFile=open(outName,'w')
    outFile.write('\n'.join([l.strip() for l in inFile.readlines()]))
    inFile.close()
    outFile.close()


if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    UnixToWin(inName,outName)