import sys
import lib.som.CODtoSHP

def CODtoSHP(inName,outName,shapeType,labelData,labelNeurons,radius):
    """
    Creates a shapfile from a codebook file.

    :arguments:
      inName
       The input codebook filename.
      outName
       The output shapefile name.
      shapeType
       The type of shapes to create, either polygon or point.
      labelData *optional*
       A data file that contains the labels for the column values.
      labelNeurons *optional*
       Whether or not neurons should be labeled by their best match to the data.
      radius *optional*
       The radius of the polygons to create.
    """
    lib.som.CODtoSHP.CODtoSHP(inName,outName,shapeType,labelData,labelNeurons,radius)
    
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
    CODtoSHP(inName,outName,shapeType,labelData,labelNeurons,radius)