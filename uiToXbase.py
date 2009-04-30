import sys
import lib.som.toXbase

if __name__=="__main__":
    inName = sys.argv[1]
    inType = sys.argv[2]
    outName = sys.argv[3]
    if sys.argv[4] == "true":
        detectTypes = True
    else:
        detectTypes = False

    lib.som.toXbase.toXbaseFile(inName,inType,outName,detectTypes)    