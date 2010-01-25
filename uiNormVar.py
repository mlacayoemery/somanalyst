import sys
import lib.som.normVar

def normalize(inName,outName,fieldNames,normBy,zeroDivision,decimalPlaces):
    """
    Creates a DBF with values normalized by a column from within an existing DBF.

    :arguments:
      inName
       The input DBF filename.
      outName
       The ouput DBF filename.
      normBy
       The column for normalizing values.
      zeroDivision
       The value to assign if their is a division by zero. 
      decimalPlace
       The number of decimal places to which numbers should be rounded.
    """
    lib.som.normVar.normalize(inName,outName,fieldNames,normBy,zeroDivision,decimalPlaces)
    
if __name__=="__main__":
    inName=sys.argv[1]
    normBy=sys.argv[2]
    outName=sys.argv[3]
    zeroDivision=float(sys.argv[4])
    if sys.argv[5]=="#":
        decimalPlaces=0
    else:
        decimalPlaces=int(sys.argv[5])
    if sys.argv[6]=="#":
        fieldNames=[]
    else:
        fieldNames=sys.argv[6].split(";")
    
    normalize(inName,outName,fieldNames,normBy,zeroDivision,decimalPlaces)