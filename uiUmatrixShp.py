import sys
import lib.som.UmatrixShp
import lib.shp.databasefile

def UmatrixShp(inName,outName,shapeType,decimalPlaces,quadrant,radius,doubleLinks,edges,value):
    """
    Creates a shapfile from a codebook file with between node Q-errors .

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
    lib.som.UmatrixShp.UmatrixShp(inName,outName,shapeType,decimalPlaces,quadrant,radius,doubleLinks,edges,value)
##    if umatrix!=False:
##        outName=outName[:outName.rfind(".")]+".dbf"
##        d=lib.shp.databasefile.DatabaseFile(None,None,None,outName)
##        u=lib.shp.databasefile.DatabaseFile(None,None,None,umatrix)
##        d.extend(u)
##        d.writeFile(outName)    
    
if __name__=="__main__":
    inName=sys.argv[1]
    shapeType=sys.argv[2]
    decimalPlaces=int(sys.argv[3])
    outName=sys.argv[4]
    quadrant=int(sys.argv[5])
    radius=float(sys.argv[6])

    if sys.argv[7]=="#" or sys.argv[7]=="false":
        doubleLinks=False
    else:
        doubleLinks=True        
    if sys.argv[8]=="#" or sys.argv[8]=="false":
        edges=False
    else:
        edges=True
    if sys.argv[9]!="#":
        value=float(sys.argv[9])
    else:
        edges=False
        value=None
    UmatrixShp(inName,outName,shapeType,decimalPlaces,quadrant,radius,doubleLinks,edges,value)