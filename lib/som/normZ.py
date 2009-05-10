from ..shp import databasefile

def normalize(inName,outName,direction,zeroDivision,decimalPlaces,fieldNames):
    inTable=databasefile.DatabaseFile([],[],[],inName)
    fieldIndicies=[]
    zeroDivision=str(zeroDivision)
    if len(fieldNames)==0:
        for id,f in enumerate(inTable.fieldspecs):
            if f[0]=="N":
                fieldIndicies.append(id)
    else:
        for f in fieldNames:
            fieldIndicies.append(inTable.index(f))

    outTable=databasefile.DatabaseFile(map(inTable.fieldnames.__getitem__,fieldIndicies),
                                       map(inTable.fieldspecs.__getitem__,fieldIndicies),
                                       [map(float,map(row.__getitem__,fieldIndicies)) for row in inTable])


    if direction=="column":
        temp=apply(zip,outTable.records)
        rows=float(len(outTable))
        averages=[s/rows for s in map(sum,temp)]
        stddevs=[]
        for rowID,row in enumerate(temp):
            stddevs.append(sum([v-averages[rowID] for v in row])/rows)
            
        for rowID,row in enumerate(outTable.records):
            for id,n in enumerate(row):
                try:
                    outTable.records[rowID][id]=str(round((n-averages[id])/stddevs[id],decimalPlaces))
                    outTable.records[rowID][id]=outTable.records[rowID][id][:outTable.records[rowID][id].rfind(".")+1+decimalPlaces]
                except ZeroDivisionError:
                    outTable.records[rowID][id]=zeroDivision

    elif direction=="global":
        records=float(len(outTable.records)*len(outTable.records[0]))
        average=sum(map(sum,outTable.records))/records
        stddev=0
        for row in outTable:
            for value in row:
                stddev+=value-average
        stddev=stddev/records
        
        for rowID,row in enumerate(outTable.records):
            for id,n in enumerate(row):
                try:
                    outTable.records[rowID][id]=str(round((n-average)/stddev,decimalPlaces))
                    outTable.records[rowID][id]=outTable.records[rowID][id][:outTable.records[rowID][id].rfind(".")+1+decimalPlaces]
                except ZeroDivisionError:
                    outTable.records[rowID][id]=zeroDivision

    elif (direction=="row"):
        for rowID,row in enumerate(outTable.records):
            average=sum(row)/len(row)
            stddev=sum([v-average for v in row])/len(row)
            for id,n in enumerate(row):
                try:
                    outTable.records[rowID][id]=str(round((n-average)/stddev,decimalPlaces))
                    outTable.records[rowID][id]=outTable.records[rowID][id][:outTable.records[rowID][id].rfind(".")+1+decimalPlaces]
                except ZeroDivisionError:
                    outTable.records[rowID][id]=zeroDivision

    print outTable.records

    for rowId,row in enumerate(outTable):
        for columnId,value in enumerate(row):
            inTable[rowId][fieldIndicies[columnId]]=value

    outTable.dynamicSpecs()
    for id, spec in enumerate(outTable.fieldspecs):
        inTable.fieldspecs[fieldIndicies[id]]=spec

    inTable.writeFile(outName)