import sys
import lib.som.extent

if __name__=="__main__":
    ifile=sys.argv[1].split('.')[0]
    ofile=sys.argv[3].split('.')[0]
    lib.som.extent.extent(ifile,ofile)