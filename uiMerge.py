import sys
import lib.som.merge

if __name__=="__main__":
    inNames=sys.argv[1].split(";")
    mergeType=sys.argv[2]
    outName=sys.argv[3]
    if sys.argv[4]=="true":
        detectTypes=True
    else:
        detectTypes=False

    lib.som.merge.merge(inNames,mergeType,outName,detectTypes)