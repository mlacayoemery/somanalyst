import sys
import lib.som.CODtoSHP

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[3]
    shapeType=sys.argv[2]
    if sys.argv[4]!="#":
        labelData=sys.argv[4]
    else:
        labelData=None
    if sys.argv[5]=="true":
        labelNeurons=True
    else:
        labelNeurons=False
    radius=float(sys.argv[7])
    quadrant=int(sys.argv[6])
    lib.som.CODtoSHP.CODtoSHP(inName,outName,shapeType,labelData,labelNeurons,radius)