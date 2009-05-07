import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

def transpose(inName,columns,outName,splitHeader,detectTypes):
    d=databasefile.DatabaseFile([],[],[],inName)

    #get reverse sorted list of indicies
    columnIndicies=map(d.index,columns)
    columnIndicies.sort(reverse=True)

    if splitHeader==True:
        oldHeader=[field.split("__") for field in d.fieldnames]
    else:
        oldHeader=[[field] for field in d.fieldnames]
    
    if type(oldHeader[0])==str:
        d.records=[d.fieldnames]+d.records
        headerLen=1
    else:
        d.records=map(list,apply(zip,oldHeader)+d.records)
        headerLen=len(oldHeader[0])

    #create new header name from column
    columns=[]
    for i in columnIndicies:
        columns.append([r.strip() for r in d.removeColumn(i)])
    #columns.reverse()
    columns=apply(zip,columns)
    d.fieldnames=map("".join,zip(["header"]*headerLen,map(str,range(headerLen))))+map("__".join,columns)[headerLen:]

    d.records=map(list,apply(zip,d.records))
    print d.fieldnames
    for r in d.records:
        print len(r)
##
##    #get new columns from old header split if specified
##    header=d.fieldnames
##    if splitHeader==True:
##        header=[field.split("__") for field in header]
##        header=apply(zip,header)
##    d.records=[header]+d.records
##    print d.records[0]
##    for r in d.records:
##        print len(r)
##    #a
##    d.records=map(list,apply(zip,d.records))
##    print
##    for r in d.records:
##        print r
##    print len(d.fieldnames)
##    if type(header[0])==str:
##        d.fieldnames=["header"]+columns
##    else:
##        d.fieldnames=map("header".join,map(str,range(len(header))))+columns
##

    if detectTypes==True:
        d.dynamicSpecs()
    else:
        d.staticSpecs()

    d.writeFile(outName)    