#Martin Lacayo-Emery

import sys
import SOMclass

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