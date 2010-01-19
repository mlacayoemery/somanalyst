import sys, os
#supports executables in long path names
#does not support output into long path names

"""
.. index::
   single: SOM; create
   single: codebook; create
"""

def mapinit(din,cout,topol,neigh,xdim,ydim,init,rand='#',buffer='#'):
    """
    This is the mapinit docstring.

    .. note::

       This function makes system calls to SOM_PAK. SOM_PAK is limited to *non-commercial* use.
    
    :arguments:
      din
       The training data.
      cout
       The codebook to create.
      topol
       The topology of the SOM. This can be hexagonal (hexa) or rectagular (rect).
      neigh
       The neighborhood type. This can be bubble or Gaussian.
      xdim
       The number of units in the X-axis of the SOM.
      ydim
       The number of units in the Y-axis of the SOM.
      init
       The initation type. This can be random or linear.
      rand (optional)
       The random seed. This is the current time by default.
      buffer (optional)
       The size of the read buffer.

    **Usage**

    >>>

    .. seealso::

       `The Self-Organizing Map Program Package <http://www.cis.hut.fi/research/som_pak/som_doc.txt>`_
          Documentation for SOM_PAK.
    """
    #get local path for mapinit
    local = sys.argv[0]
    mapinit = "\""+"\\".join(local.split("\\")[:-1])+"\\bin\\SOM_PAK\\mapinit.exe"+"\""

    #add parametes to the system call
    mapinit+=" -din "+din
    mapinit+=" -cout "+cout
    mapinit+=" -topol "+topol
    mapinit+=" -neigh "+neigh
    mapinit+=" -xdim "+xdim+" -ydim "+ydim
    mapinit+=" -init "+init

    if rand != '#':
        mapinit+=" -rand "+rand
    if buffer != '#':
        mapint+=" -buffer "+buffer
    print mapinit

    #execute command
    return os.system(mapinit)        


if __name__=="__main__":
    #input data
    din = sys.argv[1]
    #output codebook filename
    cout = sys.argv[6]
    #topology type of map, hexa or rect
    topol = sys.argv[2]
    #neighborhood type, bubble or gaussian
    neigh = sys.argv[3]
    #dimensions of map
    xdim = sys.argv[4]
    ydim = sys.argv[5]
    #initialization type, random or linear
    init = sys.argv[7]
    #seed for random number generator
    rand = sys.argv[8]
    #buffered reading of data
    buffer = sys.argv[9]

    mapinit(din,cout,topol,neigh,xdim,ydim,init,rand,buffer)    