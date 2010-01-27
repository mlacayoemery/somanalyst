import sys
import lib.som.toXbase

def toXbase(inName,inType,outName,detectTypes):
    """
    Creates a DBF file from the input file

    :arguments:
      inName
       The input filename.
      inType
       The input file type.mro
      outName
       The ouput filename.
      detectTypes
       An optional mode that detects and sets the data types for each column in the output file.
       
    """
    lib.som.toXbase.toXbaseFile(inName,inType,outName,detectTypes)    

if __name__=="__main__":
    inName = sys.argv[1]
    inType = sys.argv[2]
    outName = sys.argv[3]
    if sys.argv[4] == "true":
        detectTypes = True
    else:
        detectTypes = False

    toXbase(inName,inType,outName,detectTypes)