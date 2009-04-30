import sys
import lib.som.DBFtoDAT

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    if sys.argv[3]=="#":
        labels=[]
    else:
        labels=sys.argv[3].split(";")
    lib.som.DBFtoDAT.DBFtoDAT(inName,labels,outName)