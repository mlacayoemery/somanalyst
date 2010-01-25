import sys
from ..shp import databasefile

def select(inName,selectionType,outName,columns,start,step,stop,detectTypes):
    d=databasefile.DatabaseFile([],[],[],inName)

    if selectionType=="rows":
        if start!=0 or step!=1 or stop!=-1:
            #convert stop to positive index
            stop=len(d)+stop
            #construct indicies to remove
            remove=list(set(range(len(d))).difference(range(start,stop,step)))
            remove.sort(reverse=True)
            for i in remove:
                d.removeRow(i)
    elif selectionType=="columns":
        if start!=0 or step!=1 or stop!=-1:
            #convert stop to positive index
            stop=len(d.fieldnames)+stop
            #construct indicies to remove
            remove=list(set(range(len(d.fieldnames))).difference(range(start,stop,step)))
            remove.sort(reverse=True)
            for i in remove:
                d.removeColumn(i)
    
    #if columns selected
    if len(columns)!=0:
        remove=list(set(range(len(d.fieldnames))).difference(map(d.index,columns)))
        remove.sort(reverse=True)
        for i in remove:
            d.removeColumn(i)
                
    if detectTypes==True:
        d.dynamicSpecs()

    d.writeFile(outName)        