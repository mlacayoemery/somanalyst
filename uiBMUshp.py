import sys
import lib.som.ATRtoSHP

if __name__=="__main__":
    bmufile=sys.argv[1]
    outfile=sys.argv[3]
    if sys.argv[4]!="#":
        labels=sys.argv[4]
    else:
        labels=None
    lib.som.ATRtoSHP.BMUtoSHP(bmufile,outfile,labels)    