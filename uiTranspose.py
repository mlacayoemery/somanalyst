import sys
import lib.som.transpose

if __name__=="__main__":
    inName=sys.argv[1]
    if sys.argv[2]=="#":
        raise ValueError, "You must select at least one column."
    else:
        columns=sys.argv[2].split(";")
    outName=sys.argv[3]
    if sys.argv[4]=="true":
        splitHeader=True
    else:
        splitHeader=False
    if sys.argv[5]=="true":
        detectTypes=True
    else:
        detectTypes=False

    lib.som.transpose.transpose(inName,columns,outName,splitHeader,detectTypes)        