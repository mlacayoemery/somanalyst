from ..shp import shapefile

groupTypes={"polyline":3}
valueTypes={"minimum":1, "average":2, "maximum":3}

def group(inName,groupBy,groupType,valueType,outName,sortBy,decimalPlaces):
    """
    Groups the shapes in a shapefile based on the parameters

    :arguments:
      inName
       The input shapefile name.
      groupBy
       The field name by which to group shapes.
      groupType
       The type of grouping to create.
      valueType
       The type of value to use for the output table.
      outName
       The ouput shapefile name.
      sortBy (*optional*)
       A field name to sort on.
    """

    #read the input shapefile    
    s=shapefile.Shapefile(1)
    s.readFile(inName)

    #group shapes as necessary
    #s.table.typecast()
    groupIndex=s.table.index(groupBy)
    shapes={}
    if sortBy==None:
        for id,row in enumerate(s.table):
            groupByID=row[groupIndex]
            #create a new grouping
            if not shapes.has_key(groupByID):
                shapes[groupByID]={}
                shapes[groupByID]["shape"]={}
                shapes[groupByID]["shape"][id]=s[id]
                shapes[groupByID]["parts"]=1
                shapes[groupByID]["values"]=s.table[id]
            #add the current shape to an existing grouping
            else:
                shapes[groupByID]["shape"][id]=s[id]
                shapes[groupByID]["parts"]=1+shapes[groupByID]["parts"]
                if valueType == 1:
                    shapes[groupByID]["values"]=map(min,zip(s.table[id],shapes[groupByID]["values"])) 
                elif valueType == 2:
                    shapes[groupByID]["values"]=map(sum,zip(s.table[id],shapes[groupByID]["values"]))
                elif valueType == 3:
                    shapes[groupByID]["values"]=map(max,zip(s.table[id],shapes[groupByID]["values"]))
    else:
        sortIndex=s.index(sortBy)
        for id,row in enumerate(s.table):
            groupByID=row[groupIndex]
            sortByID=row[sortIndex]
            #create a new grouping
            if not shapes.has_key(groupByID):
                shapes[groupByID]={}
                shapes[groupByID]["shape"]={}
                shapes[groupByID]["shape"][sortByID]=s[id]
                shapes[groupByID]["parts"]=1
                shapes[groupByID]["values"]=s.table[id]
            #add the current shape to an existing grouping    
            else:
                shapes[groupByID]["shape"][sortByID]=s[id]
                shapes[groupByID]["parts"]=1+shapes[groupByID]["parts"]
                if valueType == 1:
                    shapes[groupByID]["values"]=map(min,zip(s.table[id],shapes[groupByID]["values"])) 
                elif valueType == 2:
                    shapes[groupByID]["values"]=map(sum,zip(s.table[id],shapes[groupByID]["values"]))
                elif valueType == 3:
                    shapes[groupByID]["values"]=map(max,zip(s.table[id],shapes[groupByID]["values"]))

    #create a new shapefile
    o=shapefile.Shapefile(3)

    #loop over each shape grouping in order and add to new shapefile
    places=shapes.keys()
    places.sort()    
    for l in places:
        times=shapes[l]["shape"].keys()
        times.sort()
        shape=[]
        for t in times:
            shape.append(shapes[l]["shape"][t])
        o.add(shape)

    #copy attribute table to shapefile
    o.table.fieldnames=s.table.fieldnames
    o.table.fieldspecs=s.table.fieldspecs
    o.table.records=[]

    if valueType==2:
        for l in places:
            #calculate average and convert to string
            temp=map(str,map((1/len(shapes[l]["shape"])).__mul__,shapes[l]["values"]))
            #truncate values
            temp=[v[:outTable.records[rowID][id].rfind(".")+1+decimalPlaces] for v in temp]
            o.table.addRow(temp)
        o.table.dynamicspecs()
    else:
        for l in places:
            o.table.addRow(shapes[l]["values"])

    o.writeFile(outName)