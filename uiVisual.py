import sys, os

#supports executables in long path names
#does not support output into long path names

def visual(cin,din,dout,noskip="#",buffer="#",path="\\bin\\SOM_PAK\\"):
    """
    Creates a BMU file by projecting data onto a SOM.

    :arguments:
      cin
       The input codebook file.
      din
       The input data file.
      dout
       The output BMU file.
      noskip *optional*
       Do not skip data vectors that have all components masked off.
      buffer *optional*
       A read buffer in number of lines size.
    """
    #get local path for visual
    local = sys.argv[0]
    visual = "\""+"\\".join(local.split("\\")[:-1])+path+"visual.exe"+"\""

    #add parametes to the system call
    visual+=" -cin "+cin
    visual+=" -din "+din
    visual+=" -dout "+dout

    if noskip != '#':
        visual+=" -noskip "+noskip
    if buffer != '#':
        visual+=" -buffer "+buffer
    #execute command
    return os.system(visual)        

if __name__=="__main__":
    #codebook file
    cin = sys.argv[1]
    #input data
    din = sys.argv[2]
    #output filename
    dout = sys.argv[3]
    #metric
    metric = sys.argv[4]
    #do not skip masked vectors
    noskip = sys.argv[5]
    #buffer reading of data
    buffer = sys.argv[6]

        
    if metric=="Euclidean":
        path="\\bin\\SOM_PAK\\"
    else:
        path="\\bin\\Cosine\\"    

    visual(cin,din,dout,noskip,buffer,path)