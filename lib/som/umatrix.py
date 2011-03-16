import SOMclass
from ..shp import databasefile

def uMatrix(inName,outName,decimalPlaces,metric):
    som=SOMclass.SOM()
    som.readFile(inName)

    if som.topology=="rect":
        raise TypeError, "U-matricies for rectangular topology is not supported."
    
    dbf=databasefile.DatabaseFile(["U"],[['N',9,decimalPlaces]],[])
    for i in range(som.xdimension):
        for j in range(som.ydimension):
            total=0
            number=0

            try:
                if i == som.xdimension - 1:
                    raise IndexError
                number=number+1
                total=total+SOMclass.qError(som.vectors[j][i],som.vectors[j][i+1])
            except IndexError:
                pass

            try:
                #last row
                if j == som.ydimension - 1:
                    raise IndexError
                #odd row
                if (j+1)%2==1:
                    number=number+1
                    total=total+SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i])
                #last row    
                elif i == som.xdimension-1:
                    raise IndexError
                #even 
                else:
                    number=number+1
                    total=total+SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i+1])
            except IndexError:
                pass

            try:
                if (j+1)%2==1:
                    if i==0:
                        raise IndexError
                    else:
                        number=number+1
                        total=total+SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i-1])
                else:
                    number=number+1
                    total=total+SOMclass.qError(som.vectors[j][i],som.vectors[j+1][i])
            except IndexError:
                pass
            
            try:
                if i == 0:
                    raise IndexError
                number=number+1
                total=total+SOMclass.qError(som.vectors[j][i],som.vectors[j][i-1])
            except IndexError:
                pass
            
            try:
                if j == 0:
                    raise IndexError
                if (j+1)%2==1:
                    if i == 0:
                        raise IndexError
                    else:
                        number=number+1
                        total=total+SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i])
                else:
                    number=number+1
                    total=total+SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i])
            except IndexError:
                pass

            try:
                if j == 0:
                    raise IndexError
                if (j+1)%2==1:
                    number=number+1
                    total=total+SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i])
                elif i == som.xdimension-1:
                    raise IndexError
                else:
                    number=number+1
                    total=total+SOMclass.qError(som.vectors[j][i],som.vectors[j-1][i+1])
            except IndexError:
                pass

            total=str(round(total/number,decimalPlaces))
            total=total[:total.rfind(".")+decimalPlaces+1]                
                
            dbf.addRow([total])
    dbf.refreshSpecs()
    dbf.writeFile(outName)