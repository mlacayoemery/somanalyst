import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

def toXbaseFile(inName,inType,outName,detectTypes):
    """
    Conversion to Xbase file using paths
    """
    inFile=open(inName,'r')
    fieldnames=inFile.readline().strip().split(",")
    records=[row.strip().split(",") for row in inFile.readlines()]
    d=databasefile.DatabaseFile(fieldnames,None,records)
    d.refreshSpecs()
    d.writeFile(outName)
    #toXbase(inFile,inType,outFile,detectTypes)

def toXbase(inFile,inType,outFile,detectTypes):
    """
    Conversion to Xbase file using file streams read into memory
    """
    ifile=sys.argv[1]
    ofile=sys.argv[2]

    i=open(ifile,'r')
    o=open(ofile,'wb')

    fieldnames =i.readline().strip().split(',')
    table=[l.strip().split(',') for l in i.readlines()]
    i.close()
    fieldwidth=map(len,table[0])

    for l in table:
        for id,j in enumerate(l):
            if len(j)>fieldwidth[id]:
                fieldwidth[id]=len(j)

    fieldspecs=[]
    for w in fieldwidth:
        fieldspecs.append(('C', w, 0))

    #set records
    records = table

    #write dbf
    dbfwriter(o, fieldnames, fieldspecs, records)
    o.close()

def toXbaseFileDirect(inName,inType,outName,detectTypes):
    """
    Conversion to Xbase file using paths and read/written line by line
    """
    pass