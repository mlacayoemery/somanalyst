#Martin Lacayo-Emery

import sys
import SOMclass

def BMUtoSHP(bmufile,outfile,labels,quadrant,spacing,placement,distance):
    bmu=SOMclass.BMU()
    bmu.readFile(bmufile)
    bmu.spacing=spacing
    if placement==2:
        bmu.distance=distance
    bmu.writeShapefile(outfile)
    if labels:
        dat=SOMclass.DAT()
        dat.readFile(labels)
        dbf1=bmu.DBF()
        dbf2=dat.DBF()
        dbf2.dynamicSpecs()
        dbf1.extend(dbf2)
        dbf1.writeFile(outfile[:outfile.rfind('.')]+".dbf")