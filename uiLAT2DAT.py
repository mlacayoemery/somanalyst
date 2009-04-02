import sys
import lib.som.LAT2DAT

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    lib.som.LAT2DAT.LAT2DAT(inName,outName)