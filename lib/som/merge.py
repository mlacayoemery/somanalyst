import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

def merge(inNames,mergeType,outName,detectTypes):
    d=databasefile.DatabaseFile([],[],[],inNames.pop(0))
    if mergeType=="vertical (append rows)":
        for f in inNames:
            d.append(databasefile.DatabaseFile([],[],[],f))
    elif mergeType=="horizontal (append columns)":                     
        for f in inNames:
            d.extend(databasefile.DatabaseFile([],[],[],f))
    else:
        raise ValueError, "Combine type "+mergeType+" not defined."
    if detectTypes:
        d.dynamicSpecs()
    d.writeFile(outName)
