#Martin Lacayo-Emery
#11/25/2008

from ..shp import shapefile
from ..shp import geometry
import SOMclass

def CODtoSHP(inName,outName,shapeType,labelData,radius):
    cod=SOMclass.SOM()
    cod.readFile(inName)

    #add labels from input data to neurons based on qerror
    if labelData:
        dat=SOMclass.DAT()
        dat.readFile(labelData)
        cod.matchLabel(dat.vectors,dat.labels,dat.comments)
        
        
    if shapeType=="point":
        shp=shapefile.Shapefile(1)
        for p in geometry.hexagonGrid(0,cod.xdimension,0,cod.ydimension,radius):
            shp.add([p])
    elif shapeType=="polygon":
        shp=shapefile.Shapefile(5)
        for x,y in geometry.hexagonGrid(0,cod.xdimension,0,cod.ydimension,radius):
            shp.add(geometry.hexagon(x,y,radius/2))
    else:
        raise ValueError, "Shape type"+str(shapeType)+"is not supported."

    #copy codebook table to shapefile and write out            
    shp.table=cod.DBF()
    shp.writeFile(outName[:outName.rfind(".")])