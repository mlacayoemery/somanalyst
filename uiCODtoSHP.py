import sys
import lib.som.CODtoSHP

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    shapeType=sys.argv[3]
    if sys.argv[4]!="#":
        labelData=sys.argv[4]
    else:
        labelData=None
    radius=float(sys.argv[5])
    lib.som.CODtoSHP.CODtoSHP(inName,outName,shapeType,labelData,radius)