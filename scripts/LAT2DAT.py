#Martin Lacayo-Emery
#11/1/2008

import sys

def LAT2DAT(inName,outName):
    inFile=open(inName,'r')
    outFile=open(outName,'w')

    header=inFile.readline().strip().split(',')
    print header
    outFile.write(str(len(header)-2))

    outFile.write("\n#n "+' '.join(header[2:]+header[:2]))
    for l in inFile.readlines():
        line=l.strip().split(',')
        outFile.write("\n"+' '.join(line[2:]+line[:2]))
    inFile.close()
    outFile.close()


if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    LAT2DAT(inName,outName)