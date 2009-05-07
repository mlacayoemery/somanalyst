import sys
import lib.som.group

if __name__=="__main__":
    inName=sys.argv[1]
    groupBy=sys.argv[2]
    groupType=lib.som.group.groupTypes[sys.argv[3]]
    valueType=lib.som.group.valueTypes[sys.argv[4]]
    outName=sys.argv[5]
    if sys.argv[6]=="#":
        sortBy=None
    else:
        sortBy=sys.argv[6]
    lib.som.group.group(inName,groupBy,groupType,valueType,outName,sortBy)