import sys
import lib.som.ATRtoSHP

def BMUtoSHP(bmufile,outfile,labels,quadrant,spacing,placement,distance):
    """
    Creates a shapefile from a BMU file.

    :arguments:
      bmufile
       The input BMU filename.
      outfile
       The ouput shapefile name.
      labels *optional*
       A data file that contains the labels for the column values.
      quadrant *optional*
       The Cartesian quadrant to use.
      spacing *optional*
       The spacing between units in the SOM.
      placement *optional*
       The method for placement within a neuron.
      distance *optional*
       The maximum distance for the placement.
    """
    lib.som.ATRtoSHP.BMUtoSHP(bmufile,outfile,labels,quadrant,spacing,placement,distance)

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
    BMUtoSHP(bmufile,outfile,labels,quadrant,spacing,placement,distance)
