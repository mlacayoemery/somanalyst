import sys
from ..shp import databasefile

def DBFtoDAT(inName,labels,outName):
    d=databasefile.DatabaseFile(None,None,None,inName)
    outFile=open(outName,'w')
    indicies=map(d.index,labels)
    indicies.reverse()

    outFile.write(str(len(d.fieldnames)-len(labels)))

    labelHeaders=map(d.fieldnames.pop,indicies)
    labelHeaders.reverse()
    outFile.write("\n#n "+' '.join(d.fieldnames+labelHeaders))

    for row in d:
        rowLabels=[label.strip().replace(" ","_") for label in map(row.pop,indicies)]
        rowLabels.reverse()
        outFile.write("\n"+' '.join(row+rowLabels))
    outFile.close()