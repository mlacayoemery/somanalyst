#Martin Lacayo-Emery

import sys, visual

def HexToRect(x,y):
    #if odd
    if (y+1)%2:
        #no x offset
        return (x,y)
    else:
        return (x-.05,y)

def RectToHex(x,y):
    #if odd
    if (y+1)%2:
        #no x offset
        return (x,y)
    else:
        return (x+.05,y)

#returns a list of neighbors 1 radius
def neighbors(x,y,xdim,ydim):
    if x==0:
        #left
        pass
        if y==0:
            #bottom left cornner
            pass
        elif y==ydim:
            #top left cornner
            pass
        else:
            #left edge
            pass
    elif x==xdim:
        #right
        pass
        if y==0:
            #bottom right corrner
            pass
        elif y==ydim:
            #top right cornner
            pass
        else:
            #right edge
            pass
    elif y==0:
        #bottom edge
        pass
    elif y==ydim:
        #top edge
        pass
    else:
        #middle piece
        pass

def activate(x,y,radius):
    

def inverseT(a,run,rlen):
    return a*(1-(run/float(rlen)))

def vsom(cin,din,cout,rlen,alpha,radius,rand,fixed,weights,buffer,alpha_type,snapfile,snapinterval):
    cin=open(cin,'r')
    header=cin.readline().strip().split()

    din=open(din,'r')
    dimensions=int(din.readline())
    
    if dimensions!=int(header[0]):
        raise ValueError, "The dimensions between the data and the som do not match."

    xdim=int(header[2])
    ydim=int(header[3])

    som=[]
    for y in range(ydim):
        row=[]
        for x in range(xdim):
            row.append(map(float,cin.readline().strip().split()))
        som.append(row)
    cin.close()

    data=[map(float,l.strip().split()) for l in din.readlines()]
    din.close()

    run=0
    neighborhood=radius
    #full runs
    for i in range(rlen/len(data)):
        run+=1
        alpha=inverseT(alpha,run,rlen)
        neighborhood=radius-inverseT(radius,run-1,rlen)
        active=visual.match(som,data[i])

    #partial run
    for i in range(rlen%len(data)):
        run+=1
        alpha=inverseT(alpha,run,rlen)
        neighborhood=radius-inverseT(radius,run-1,rlen)
        active=visual.match(som,data[i])
        
        

if __name__=="__main__":
    #initial codebook
    cin=sys.argv[1]
    #teaching data
    din=sys.argv[2]
    #output codebook
    cout=sys.argv[3]
    #running length
    rlen=int(sys.argv[4])
    #initial alpha value
    alpha=float(sys.argv[5])
    #initial radius
    radius=float(sys.argv[6])
    #random seed
    rand=sys.argv[7]
    #use fixed points
    fixed=sys.argv[8]
    #use weights
    weights=sys.argv[9]
    #read buffer
    buffer=sys.argv[10]
    #type of alpha decrease: linear or inverse t
    alpha_type=sys.argv[11]
    #snapshot filename
    snapfile=sys.argv[12]
    #interval between snapshots
    snapinterval=sys.argv[13]