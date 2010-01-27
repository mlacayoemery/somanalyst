from ..shp import databasefile

def normalize(inName,outName,direction,zeroDivision,decimalPlaces,fieldNames):
    """
    Creates a Z-score normalized database file.

    :arguments:
      inName
       The input database file name.
      outName
       The ouput database file name.
      direction
       The direction in which to perform the normalization.
      zeroDivision
       The value to assign if there is a division by zero.
      decimalPlaces
       The number of decimal place to which to round numbers.
      fieldNames
       The names of the fields on which to perform the normalization.
    """

    #convert value for later
    zeroDivision=str(zeroDivision)
    
    #temporay variables    
    inTable=databasefile.DatabaseFile([],[],[],inName)
    fieldIndicies=[]

    #get field indicies for values to normalize
    if len(fieldNames)==0:
        for id,f in enumerate(inTable.fieldspecs):
            if f[0]=="N":
                fieldIndicies.append(id)
    else:
        for f in fieldNames:
            fieldIndicies.append(inTable.index(f))

    #create table with copy of values
    outTable=databasefile.DatabaseFile(map(inTable.fieldnames.__getitem__,fieldIndicies),
                                       map(inTable.fieldspecs.__getitem__,fieldIndicies),
                                       [map(float,map(row.__getitem__,fieldIndicies)) for row in inTable])

    #calculate values down columns
    if direction=="column":
        #calculate the average for each column
        temp=apply(zip,outTable.records)
        rows=float(len(outTable))
        averages=[s/rows for s in map(sum,temp)]

        #calculate the std deviation for each column
        stddevs=[]
        for rowID,row in enumerate(temp):
            stddevs.append((sum([(v-averages[rowID])**2 for v in row])/(rows-1))**0.5)
            
        for rowID,row in enumerate(outTable.records):
            for colID,v in enumerate(row):
                try:
                    #calculate Z-score, round and truncate
                    temp=str(round((v-averages[colID])/stddevs[colID],decimalPlaces))
                    temp=temp[:temp.rfind(".")+1+decimalPlaces]
                    outTable.records[rowID][colID]=temp
                except ZeroDivisionError:
                    outTable.records[rowID][colID]=zeroDivision

    elif direction=="global":
        records=float(len(outTable.records)*len(outTable.records[0]))
        average=sum(map(sum,outTable.records))/records
        stddev=0
        for row in outTable:
            for value in row:
                stddev+=(value-average)**2
        stddev=(stddev/(records-1))**0.5
        
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
            stddev=(sum([(v-average)**2 for v in row])/(len(row)-1))**0.5
            for id,n in enumerate(row):
                try:
                    outTable.records[rowID][id]=str(round((n-average)/stddev,decimalPlaces))
                    outTable.records[rowID][id]=outTable.records[rowID][id][:outTable.records[rowID][id].rfind(".")+1+decimalPlaces]
                except ZeroDivisionError:
                    outTable.records[rowID][id]=zeroDivision

    #copy Z-scores back into original table
    for rowId,row in enumerate(outTable):
        for columnId,value in enumerate(row):
            inTable[rowId][fieldIndicies[columnId]]=value

    #determine field specs for Z-score columns and copy to original table
    outTable.dynamicSpecs()
    for id, spec in enumerate(outTable.fieldspecs):
        inTable.fieldspecs[fieldIndicies[id]]=spec

    inTable.writeFile(outName)