import sys
import lib.som.extent

def extent(ifile,ofile):
    """
    Creates a rectangular extent for a shapefile.

    :arguments:
      ifile
       The input shapefile name.
      ofile
       The output shapefile name.
    """
    lib.som.extent.extent(ifile,ofile)
    
if __name__=="__main__":
    ifile=sys.argv[1].split('.')[0]
    ofile=sys.argv[3].split('.')[0]
    extent(ifile,ofile)