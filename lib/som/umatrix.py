import SOMclass
from ..shp import databasefile

def uMatrix(inName,outName):
    som=SOMclass.SOM()
    som.readFile(inName)
    dbf=databasefile.DatabaseFile(["Uvalue"],[['N',9,6]],[])
    for i in range(som.ydimension):
        for j in range(som.xdimension):
            centroid=som.vectors[i][j]
            total=0
            number=0
            #starting at noon, going clockwise
            try:
               total+=SOMclass.qError(centroid,som.vectors[i+1][j])
               number+=1
            except IndexError:
                pass
            try:
               total+=SOMclass.qError(centroid,som.vectors[i][j+1])
               number+=1
            except IndexError:
                pass
            try:
               total+=SOMclass.qError(centroid,som.vectors[i-1][j])
               number+=1
            except IndexError:
                pass
            try:
               total+=SOMclass.qError(centroid,som.vectors[i-1][j-1])
               number+=1
            except IndexError:
                pass
            try:
               total+=SOMclass.qError(centroid,som.vectors[i][j-1])
               number+=1
            except IndexError:
                pass
            try:
               total+=SOMclass.qError(centroid,som.vectors[i+1][j-1])
               number+=1
            except IndexError:
                pass
            value=str(round(total/number,6))
            dbf.addRow([value[:values.rfind(".")+6]])
    dbf.writeFile(outName)