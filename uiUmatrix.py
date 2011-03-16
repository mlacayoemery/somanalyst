import sys
import lib.som.umatrix

def uMatrix(inName,outName,decimalPlaces,metric):
    """
    Calculates the U-matrix for a SOM.

    :arguments:
      inName
       The input SOM filename.
      outName
       The ouput U-matrix filename.
      decimalPlaces
       The number of decimals to round to.
    """
    lib.som.umatrix.uMatrix(inName,outName,decimalPlaces,metric)
    
if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    decimalPlaces=int(sys.argv[3])
    metric=sys.argv[4]
        
    uMatrix(inName,outName,decimalPlaces,metric)