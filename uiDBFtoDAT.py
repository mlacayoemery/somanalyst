import sys
import lib.som.DBFtoDAT

def DBFtoDAT(inName,labels,outName):
    """
    Creates a SOM data file from the input datbase file.

    :arguments:
      inName
       The input filename.
      labels
       The column headers for the label columns.
      outName
       The output filename.
    """
    lib.som.DBFtoDAT.DBFtoDAT(inName,labels,outName)

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    if sys.argv[3]=="#":
        labels=[]
    else:
        labels=sys.argv[3].split(";")
    DBFtoDAT(inName,labels,outName)