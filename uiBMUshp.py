import sys
import lib.som.ATRtoSHP

if __name__=="__main__":
    bmufile=sys.argv[1]
    outfile=sys.argv[3]
    if sys.argv[4]!="#":
        labels=sys.argv[4]
    else:
        labels=None
    quadrant=int(sys.argv[5])
    spacing=float(sys.argv[6])
    if sys.argv[7]=="center":
        placement=1
    else:
        placement=2
    distance=float(sys.argv[8])
    lib.som.ATRtoSHP.BMUtoSHP(bmufile,outfile,labels,quadrant,spacing,placement,distance)
