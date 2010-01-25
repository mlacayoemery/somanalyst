import sys
import lib.som.normZ

def normalize(inName,outName,direction,zeroDivision,decimalPlaces,fieldNames):
    """
    Creates a DBF with Z-score normalized values from an existing DBF.

    :arguments:
      inName
       The input DBF filename.
      outName
       The ouput DBF filename.
      direction
       The direction in which to determine minimum and maximum values in the input range.
      zeroDivision
       The value to assign if their is a division by zero. 
      decimalPlace
       The number of decimal places to which numbers should be rounded.
      fieldNames
       The fields on which to perform the normalization.       
    """
    lib.som.normZ.normalize(inName,outName,direction,zeroDivision,decimalPlaces,fieldNames)
    
if __name__ == "__main__":
    inName = sys.argv[1]
    direction = sys.argv[2]
    outName = sys.argv[3]
    if sys.argv[4]=="#":
        zeroDivision=0
    else:
        zeroDivision=float(sys.argv[4])
    if sys.argv[5]=="#":
        decimalPlaces=0
    else:
        decimalPlaces = int(sys.argv[5])
    if sys.argv[6] == "#":
        fieldNames=[]
    else:
        fieldNames = sys.argv[6].split(";")
    normalize(inName,outName,direction,zeroDivision,decimalPlaces,fieldNames)