#Martin Lacayo-Emery
#11/25/2008

import sys, shapefile, SOMclass

def CODtoSHP(inName,outName,shapeType,labelData,radius):
    cod=SOMclass.SOM()
    cod.readFile(inName)

    #add labels from input data to neurons based on qerror
    if labelData:
        dat=SOMclass.DAT()
        dat.readFile(labelData)
        cod.matchLabel(dat.vectors,dat.labels)
        
    if shapeType=="point":
        shp=shapefile.Shapefile(1)
        for p in shapefile.hexagonCentroids(0,cod.xdimension,0,cod.ydimension,radius):
            shp.add([p])
    elif shapeType=="polygon":
        shp=shapefile.Shapefile(5)
        for x,y in shapefile.hexagonCentroids(0,cod.xdimension,0,cod.ydimension,radius):
            shp.add(shapefile.hexagon(x,y,radius/2))
    else:
        raise ValueError, "Shape type"+str(shapeType)+"is not supported."

    #copy codebook table to shapefile and write out            
    shp.table=cod.DBF()
    shp.writeFile(outName[:outName.rfind(".")])
    
if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    shapeType=sys.argv[3]
    if sys.argv[4]!="#":
        labelData=sys.argv[4]
    else:
        labelData=None
    radius=float(sys.argv[5])
    CODtoSHP(inName,outName,shapeType,labelData,radius)