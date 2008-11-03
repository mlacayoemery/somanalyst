#Martin Lacayo-Emery

import sys

def qError(v1,v2):
    return sum(map(lambda v: (v[0]-v[1])**2,zip(v1,v2)))**0.5

def match(som,vector):
    match=[0,0,qError(d,som[0][0])]
    for y,row in enumerate(som):
        for x,n in enumerate(row):
            tempMatch=[x,y,qError(vector,n)]
            if match[2]>tempMatch[2]:
                match=tempMatch

def bmu(som,data):
    matches=[]    
    for d in data:
        matches.append(match(som,d))
    return matches        
                
                

def vsom(cin,din,dout,noskip,buffer):
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

    matches=bmu(som,data)    

    dout=open(dout,'w')
    dout.write(' '.join(map(str,header)))
    for m in matches:
        dout.write("\n"+' '.join(map(str,m)))
    dout.close()

    

if __name__=="__main__":
    #codebook file
    cin=sys.argv[1]
    #input data
    din=sys.argv[2]
    #output filename
    dout=sys.argv[3]
    #do not skip data vectors
    noskip=sys.argv[4]
    #buffered reading of data
    buffer=sys.argv[5]

    vsom(cin,din,dout,noskip,buffer) 