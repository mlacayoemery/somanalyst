from ..shp import databasefile

def normalize(inName,outName,fieldNames,normBy,zeroDivision,decimalPlaces):
    inTable=databasefile.DatabaseFile([],[],[],inName)
    normIndex=inTable.index(normBy)
    zeroDivision=str(zeroDivision)
    
    fieldIndicies=[]
    if len(fieldNames)==0:
        for id,f in enumerate(inTable.fieldspecs):
            if f[0]=="N":
                fieldIndicies.append(id)
        fieldIndicies.pop(fieldIndicies.index(normIndex))
    else:
        for f in fieldNames:
            fieldIndicies.append(inTable.index(f))

    outTable=databasefile.DatabaseFile(map(inTable.fieldnames.__getitem__,fieldIndicies),
                                       map(inTable.fieldspecs.__getitem__,fieldIndicies),
                                       [map(float,map(row.__getitem__,fieldIndicies)) for row in inTable])


    for rowID,row in enumerate(outTable.records):
        denom=float(inTable[rowID][normIndex])
        for id,n in enumerate(row):
            try:
                outTable.records[rowID][id]=str(round(n/denom,decimalPlaces))
                outTable.records[rowID][id]=outTable.records[rowID][id][:outTable.records[rowID][id].rfind(".")+1+decimalPlaces]
            except ZeroDivisionError:
                outTable.records[rowID][id]=zeroDivision

    for rowId,row in enumerate(outTable):
        for columnId,value in enumerate(row):
            inTable[rowId][fieldIndicies[columnId]]=value

    outTable.dynamicSpecs()
    for id, spec in enumerate(outTable.fieldspecs):
        inTable.fieldspecs[fieldIndicies[id]]=spec

    inTable.writeFile(outName)