import sys
import lib.som.CODtoSHP
import lib.shp.databasefile

def CODtoSHP(inName,outName,shapeType,labelData,labelNeurons,radius,quadrant,umatrix=False):
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
    lib.som.CODtoSHP.CODtoSHP(inName,outName,shapeType,labelData,labelNeurons,radius,quadrant)
    if umatrix!=False:
        outName=outName[:outName.rfind(".")]+".dbf"
        d=lib.shp.databasefile.DatabaseFile(None,None,None,outName)
        u=lib.shp.databasefile.DatabaseFile(None,None,None,umatrix)
        d.extend(u)
        d.writeFile(outName)    
    
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
    if sys.argv[6]!="#":
        umatrix=sys.argv[6]
    else:
        umatrix=False        
    radius=float(sys.argv[8])
    quadrant=int(sys.argv[7])
    CODtoSHP(inName,outName,shapeType,labelData,labelNeurons,radius,quadrant,umatrix)