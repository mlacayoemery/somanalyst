#Martin Lacayo-Emery

import sys, SOMclass

def BMUtoSHP(bmufile,outfile,labels):
    bmu=SOMclass.BMU()
    bmu.readFile(bmufile)
    bmu.writeShapefile(outfile)
    if labels:
        dat=SOMclass.DAT()
        dat.readFile(labels)
        dbf1=bmu.DBF()
        dbf2=dat.DBF()
        dbf1.extend(dbf2)
        dbf1.writeFile(outfile[:outfile.rfind('.')]+".dbf")

if __name__=="__main__":
    bmufile=sys.argv[1]
    outfile=sys.argv[2]
    if sys.argv[4]!="#":
        labels=sys.argv[4]
    else:
        labels=None
    BMUtoSHP(bmufile,outfile,labels)    