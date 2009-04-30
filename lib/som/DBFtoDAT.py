import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

def DBFtoDAT(inName,labels,outName):
    d=databasefile.DatabaseFile(None,None,None,inName)
    outFile=open(outName,'w')
    indicies=map(d.index,labels)
    indicies.reverse()

    outFile.write(str(len(d.fieldnames)-len(labels)))

    labelHeaders=map(d.fieldnames.pop,indicies)
    outFile.write("\n#n "+' '.join(d.fieldnames+labelHeaders))

    for row in d:
        rowLabels=map(row.pop,indicies)
        outFile.write("\n"+' '.join(row+rowLabels))
    outFile.close()