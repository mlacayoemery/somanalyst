import sys
import lib.som.extent

if __name__=="__main__":
    ifile=sys.argv[1]
    ofile=sys.argv[2].split('.')[0]
    lib.som.extent.extent(ifile,ofile)