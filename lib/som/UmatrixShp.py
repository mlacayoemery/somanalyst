#Martin Lacayo-Emery
#11/25/2008

from ..shp import shapefile
from ..shp import geometry
import SOMclass

def UmatrixShp(inName,outName,shapeType,decimalPlaces,radius,doubleLinks,edges,value):
    shapeType=shapefile.shapeTypes[shapeType]
    
    som=SOMclass.SOM()
    som.readFile(inName)

    shp=shapefile.Shapefile(shapeType)

    for i in range(som.xdimension):
        for j in range(som.ydimension):

            total=0
            number=0
            
            shapes=[]
            if shapeType==3:
                x,y=geometry.hexagonCentroid(i,j)
                points=geometry.hexagon(x,y,radius/2)
                hex=geometry.closedSet(points[1:]+[points[0]])                
                for lcv in range(6):
                    shapes.append([hex[lcv],hex[lcv+1]])
            elif shapeType==5:
                x,y=geometry.hexagonCentroid(i,j)
                points=geometry.hexagon(x,y,radius/2)
                hex=geometry.closedSet(points[1:]+[points[0]])
                for lcv in range(6):
                    x1,y1=hex[lcv]
                    x2,y2=hex[lcv+1]
                    shapes.append(geometry.closedSet(geometry.hexagon((x1+x2)/2,(y1+y2)/2,radius/4)))
                
                
            #starting at noon, going clockwise
            k=0
            try:
                if i == som.xdimension - 1:
                    raise IndexError
                u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j][i+1]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)
            except IndexError:
                if edges:
                    shp.add(shapes[k],[value])

            k=k+1
            try:
                #last row
                if j == som.ydimension - 1:
                    raise IndexError
                #odd row
                if (j+1)%2==1:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i]),decimalPlaces))
                #last row    
                elif i == som.xdimension-1:
                    raise IndexError
                #even 
                else:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i+1]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)
            except IndexError:
                if edges:
                    shp.add(shapes[k],[value])

            k=k+1                
            try:
                if (j+1)%2==1:
                    if i==0:
                        raise IndexError
                    else:
                        u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i-1]),decimalPlaces))
                else:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)
            except IndexError:
                if edges:
                    shp.add(shapes[k],[value])

            k=k+1                
            try:
                if i == 0:
                    raise IndexError
                u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j][i-1]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                if doubleLinks:
                    shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)
            except IndexError:
                if edges:
                    shp.add(shapes[k],[value])

            k=k+1                
            try:
                if j == 0:
                    raise IndexError
                if (j+1)%2==1:
                    if i == 0:
                        raise IndexError
                    else:
                        u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i]),decimalPlaces))
                else:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                if doubleLinks:
                    shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)
            except IndexError:
                if edges:
                    shp.add(shapes[k],[value])

            k=k+1               
            try:
                if j == 0:
                    raise IndexError
                if (j+1)%2==1:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i]),decimalPlaces))
                elif i == som.xdimension-1:
                    raise IndexError
                else:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i+1]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                if doubleLinks:
                    shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)
            except IndexError:
                if edges:
                    shp.add(shapes[k],[value])

            if shapeType==5 and number > 0:
                u=str(round(total/number,decimalPlaces))
                u=u[:u.rfind(".")+decimalPlaces]                
                shp.add(geometry.closedSet(geometry.hexagon(x,y,radius/4)),[u])

    shp.table.refreshSpecs()
    shp.table.fieldnames=["U"]
    shp.writeFile(outName[:outName.rfind(".")])