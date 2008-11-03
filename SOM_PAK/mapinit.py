#Martin Lacayo-Emery

import sys, random

def randinit(xdim,ydim,dimensions):
    som=[]
    for x in range(xdim):
        row=[]
        for y in range(ydim):
            neuron=[]
            for z in range(dimensions):
                neuron.append(random.random())
            row.append(neuron)
        som.append(row)

    return som        

def mapinit(din="c:\data.dat",cout="c:\init.cod",topol="hexa",neigh="gaussian",xdim=20,ydim=20,init="rand",rand=0,buffer=0):    
    din=open(din,'r')
    dimensions=int(din.readline())
    din.close()

    cout=open(cout,'w')
    cout.write(" ".join(map(str,[dimensions,topol,xdim,ydim,neigh])))
    cout.write("\n# random seed: "+str(rand))
    
    if init=="rand":
        random.seed(rand)
        som=randinit(xdim,ydim,dimensions)
    elif init=="lin":
        raise ValueError, init+" initialization is not supported at this time."
    else:
        raise ValueError, init+" is not a recognized initialization time."

    for row in som:
        for neuron in row:
            cout.write("\n"+' '.join(map(str,neuron)))

    cout.close()                

if __name__=="__main__":
    #input data
    din=sys.argv[1]
    #output codebook filename
    cout=sys.argv[2]
    #topology: hexa or rect
    topol=sys.argv[3]
    #nighborhood type: bubble or gaussian
    neigh=sys.argv[4]
    #x dimension of map
    xdim=int(sys.argv[5])
    #y dimension of map
    ydim=int(sys.argv[6])
    #initialization type: rand or lin
    init=sys.argv[7]
    #random seed
    rand=int(sys.argv[8])
    #read buffer
    buffer=int(sys.argv[9])

    mapinit(din,cout,topol,neigh,xdim,ydim,init,rand,buffer)    