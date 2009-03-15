import sys, SOMclass, databasefile

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
        
            dbf.addRow([round(total/number,6)])
    dbf.writeFile(outName)

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    uMatrix(inName,outName)