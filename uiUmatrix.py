import sys
import lib.som.umatrix

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    lib.som.umatrix.uMatrix(inName,outName)