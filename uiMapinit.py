import sys, os

#supports executables in long path names
#does not support output into long path names

def mapinit(din,cout,topol,neigh,xdim,ydim,init,rand='#',buffer='#'):
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