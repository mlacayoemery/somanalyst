import sys
import lib.som.ATRtoTRJ


if __name__=="__main__":
    bmufile=sys.argv[1]
    outfile=sys.argv[2]
    lib.som.ATRtoTRJ.ATRtoTRJ(bumfile,outfile)