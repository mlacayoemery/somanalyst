from ..shp import shapefile

groupTypes={"polyline":3}
valueTypes={"average":1}

def group(inName,groupBy,groupType,valueType,outName,sortBy):
    s=shapefile.Shapefile(1)
    s.readFile(inName)
    groupIndex=s.table.index(groupBy)
    shapes={}
    if sortBy==None:
        for id,row in enumerate(s.table):
            groupByID=row[groupIndex]
            if not shapes.has_key(groupByID):
                shapes[groupByID]={}
                shapes[groupByID]["shape"]={}
                shapes[groupByID]["shape"][id]=s[id]
                shapes[groupByID]["parts"]=1
                shapes[groupByID]["values"]=s.table[id]
            else:
                shapes[groupByID]["shape"][id]=s[id]
                shapes[groupByID]["parts"]=1+shapes[groupByID]["parts"]
                shapes[groupByID]["values"]=map(max,zip(s.table[id],shapes[groupByID]["values"]))
    else:
        sortIndex=s.index(sortBy)
        for id,row in enumerate(s.table):
            groupByID=row[groupIndex]
            sortByID=row[sortIndex]
            if not shapes.has_key(groupByID):
                shapes[groupByID]={}
                shapes[groupByID]["shape"]={}
                shapes[groupByID]["shape"][sortByID]=s[id]
                shapes[groupByID]["parts"]=1
                shapes[groupByID]["values"]=s.table[id]                
            else:
                shapes[groupByID]["shape"][sortByID]=s[id]
                shapes[groupByID]["parts"]=1+shapes[groupByID]["parts"]
                shapes[groupByID]["values"]=map(max,zip(s.table[id],shapes[groupByID]["values"]))

    o=shapefile.Shapefile(3)
    places=shapes.keys()
    places.sort()
    for l in places:
        times=shapes[l]["shape"].keys()
        times.sort()
        shape=[]
        for t in times:
            shape.append(shapes[l]["shape"][t])
        o.add(shape)

    o.table.fieldnames=s.table.fieldnames
    o.table.fieldspecs=s.table.fieldspecs
    o.table.records=[]
    for l in places:
        o.table.addRow(shapes[l]["values"])
    o.writeFile(outName)