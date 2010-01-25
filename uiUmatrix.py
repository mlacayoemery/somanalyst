import sys
import lib.som.umatrix

def uMatrix(inName,outName):
    """
    Calculates the U-matrix for a SOM.

    :arguments:
      inName
       The input SOM filename.
      outName
       The ouput U-matrix filename.
    """
    lib.som.umatrix.uMatrix(inName,outName)
    
if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    uMatrix(inName,outName)