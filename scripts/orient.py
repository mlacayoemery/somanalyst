#Martin Lacayo-Emery
#11/9/2008

import sys

def qError(v1,v2):
    return sum(map(lambda v: (v[0]-v[1])**2,zip(v1,v2)))**0.5

def orient(orientName,inName,outName):
    orientFile=open(orientName,'r')
    inFile=open(inName,'r')
    orientheader=orientFile.readline().strip().split()
    header=inFile.readline().strip().split()

    orientLines=[orientFile.readlines()
    if orientheader==header:
        
    

if __name__=="__main__":
    orientName=sys.argv[1]
    inName=sys.argv[2]
    outName=sys.argv[3]
    orient(orientName,inName,outName)