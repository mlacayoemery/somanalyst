import sys, os

#supports executables in long path names
#does not support output into long path names

def vsom(cin,din,cout,rlen,alpha,radius,rand='#',fixed="#",weights="#",buffer='#',alpha_type="#",snapfile="#",snapinterval="#",path="\\bin\\SOM_PAK\\"):
    #get local path for vsom
    local = sys.argv[0]
    vsom = "\""+"\\".join(local.split("\\")[:-1])+path+"vsom.exe"+"\""

    #add parametes to the system call
    vsom+=" -cin "+cin
    vsom+=" -din "+din
    vsom+=" -cout "+cout
    vsom+=" -rlen "+rlen
    vsom+=" -alpha "+alpha
    vsom+=" -radius "+radius

    if rand != '#':
        vsom+=" -rand "+rand
    if fixed != '#':
        vsom+=" -fixed "+fixed
    if weights != '#':
        vsom+=" -weights "+weights
    if buffer != '#':
        vsom+=" -buffer "+buffer
    if alpha_type != '#':
        vsom+=" -alpha_type "+alpha_type
    if snapfile != '#':
        vsom+=" -snapfile "+snapfile
    if snapinterval != '#':
        vsom+=" -snapinterval "+snapinterval

    #execute command
    print vsom
    return os.system(vsom)        

if __name__=="__main__":
    #initial codebook file
    cin = sys.argv[1]
    #teaching data
    din = sys.argv[2]
    #output codebook filename
    cout = sys.argv[6]
    #running length of teaching
    rlen = sys.argv[3]
    #initial alpha value
    alpha = sys.argv[4]
    #initial radius of neighborhood
    radius = sys.argv[5]
    #metric
    metric = sys.argv[7]
    #seed for random number generator
    rand = sys.argv[8]
    #use fixed points
    fixed = sys.argv[9]
    #use weights
    weights =sys.argv[10]
    #buffer reading of data
    buffer = sys.argv[11]
    #type of alpha
    alpha_type = sys.argv[12]
    #snapshot filename
    snapfile = sys.argv[13]
    #snapshot interavl
    snapinterval=sys.argv[14]

    if metric=="Euclidean":
        path="\\bin\\SOM_PAK\\"
    else:
        path="\\bin\\Cosine\\"
        
    vsom(cin,din,cout,rlen,alpha,radius,rand,fixed,weights,buffer,alpha_type,snapfile,snapinterval,path)