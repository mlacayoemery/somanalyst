#Martin Lacayo-Emery
#11/1/2008

def LAT2DAT(inName,outName):
    inFile=open(inName,'r')
    outFile=open(outName,'w')

    header=inFile.readline().strip().split(',')
    outFile.write(str(len(header)-2))

    outFile.write("\n#n "+' '.join(header[2:]+header[:2]))
    for l in inFile.readlines():
        line=l.strip().split(',')
        outFile.write("\n"+' '.join(line[2:]+line[:2]))
    inFile.close()
    outFile.close()