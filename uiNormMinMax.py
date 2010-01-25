import sys
import lib.som.normMinMax

def normalize(inName,outName,start,end,direction,minEqMax,fieldNames,decimalPlaces):
    """
    Creates a DBF with minimum-maxiumum normalized values from an existing DBF.

    :arguments:
      inName
       The input DBF filename.
      outName
       The ouput DBF filename.
      start
       The minimum value to contain in the output range.
      end
       The maximum value to caontain in the output range.
      direction
       The direction in which to determine minimum and maximum values in the input range.
      minEqMax
       The value to assign if the minimum is equal to the maxium. (division by zero)
      fieldNames
       The fields on which to perform the normalization.
      decimalPlace
       The number of decimal places to which numbers should be rounded.
    """
    lib.som.normMinMax.normalize(inName,outName,start,end,direction,minEqMax,fieldNames,decimalPlaces)
    
if __name__ == "__main__":
    inName = sys.argv[1]
    direction = sys.argv[2]
    outName = sys.argv[3]
    start = float(sys.argv[5])
    end = float(sys.argv[6])
    minEqMax = float(sys.argv[4])
    if sys.argv[8]=="#":
        fieldNames = []
    else:
        fieldNames=sys.argv[8].split(";")
    if sys.argv[7]=="#":
        decimalPlaces=0
    else:
        decimalPlaces=int(sys.argv[7])

    normalize(inName,outName,start,end,direction,minEqMax,fieldNames,decimalPlaces)    