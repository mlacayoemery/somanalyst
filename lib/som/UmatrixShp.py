#Martin Lacayo-Emery
#11/25/2008

from ..shp import shapefile
from ..shp import geometry
import SOMclass

def UmatrixShp(inName,outName,shapeType,decimalPlaces,quadrant,radius,doubleLinks,edges,value):
    shapeType=shapefile.shapeTypes[shapeType]
    
    som=SOMclass.SOM()
    som.readFile(inName)

    if som.topology == "rect":
        raise ValueError, "Rectangular topology is not implemented."
    
    #determin scaling for quadrant
    if quadrant==1:
        xscale=1
        yscale=1
    elif quadrant==2:
        xscale=-1
        yscale=1
    elif quadrant==3:
        xscale=-1
        yscale=-1
    elif quadrant==4:
        xscale=1
        yscale=-1
    else:
        raise ValueError, str(quadrant)+" invalid quadarant. Must be 1, 2, 3, or 4."
    
    shp=shapefile.Shapefile(shapeType)

    #loop over som
    for i in range(som.xdimension):
        for j in range(som.ydimension):

            total=0
            number=0
            
            shapes=[]
            #calculate geometry
            if shapeType==3:
                #get centroid
                x,y=geometry.hexagonCentroid(i,j)
                #get hexagon points
                points=geometry.hexagon(x,y,radius/2)
                #add edges
                hex=geometry.closedSet(points[1:]+[points[0]])                
                for lcv in range(6):
                    shapes.append([hex[lcv],hex[lcv+1]])
                    
            elif shapeType==5:
                #get centroid
                x,y=geometry.hexagonCentroid(i,j)
                #get hexagon points
                points=geometry.hexagon(x,y,radius/2)
                hex=geometry.closedSet(points[1:]+[points[0]])
                #add hexagons
                for lcv in range(6):
                    x1,y1=hex[lcv]
                    x2,y2=hex[lcv+1]
                    shapes.append(geometry.closedSet(geometry.hexagon((x1+x2)/2,(y1+y2)/2,radius/4)))                
            
            #calculate values and add geometry starting at 3 o'clock, going clockwise
            k=0
            if i == som.xdimension - 1:
                if edges:
                    shp.add(shapes[k],[value])
            else:
                u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j][i+1]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)

            k=1
            if j == som.ydimension - 1 or i == som.xdimension-1:
                if edges:
                    shp.add(shapes[k],[value])
            else:
                if (j+1)%2==1:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i]),decimalPlaces))
                else:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i+1]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)

            k=2                
            if (j+1)%2==1 and i==0:
                if edges:
                    shp.add(shapes[k],[value])
            else:
                print j, i
                if (j+1)%2==1:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i-1]),decimalPlaces))
                else:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)                    

            k=3                
            if i == 0:
                if edges:
                    shp.add(shapes[k],[value])
            else:
                u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j][i-1]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                if doubleLinks:
                    shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)

            k=4                
            if j == 0 or ((j+1)%2==1 and i == 0):
                if edges:
                    shp.add(shapes[k],[value])
            else:
                if (j+1)%2==1:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i]),decimalPlaces))
                else:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i]),decimalPlaces))
                u=u[:u.rfind(".")+1+decimalPlaces]
                if doubleLinks:
                    shp.add(shapes[k],[u])
                number=number+1
                total=total+float(u)

            k=5               
            if j == 0 or ((j+1)%2!=1 and i == som.xdimension-1):
                if edges:
                    shp.add(shapes[k],[value])
            else:
                if (j+1)%2==1:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i]),decimalPlaces))
                else:
                    u=str(round(SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i+1]),decimalPlaces))
            u=u[:u.rfind(".")+1+decimalPlaces]
            if doubleLinks:
                shp.add(shapes[k],[u])
            number=number+1
            total=total+float(u)

            if shapeType==5 and number > 0:
                u=str(round(total/number,decimalPlaces))
                u=u[:u.rfind(".")+decimalPlaces]                
                shp.add(geometry.closedSet(geometry.hexagon(x,y,radius/4)),[u])

    shp.table.refreshSpecs()
    shp.table.fieldnames=["U"]
    shp.writeFile(outName[:outName.rfind(".")])