import sys, os

#supports executables in long path names
#does not support output into long path names

def visual(cin,din,dout,noskip="#",buffer="#"):
    #get local path for visual
    local = sys.argv[0]
    visual = "\""+"\\".join(local.split("\\")[:-2])+"\\SOM_PAK\\visual.exe"+"\""

    #add parametes to the system call
    visual+=" -cin "+cin
    visual+=" -din "+din
    visual+=" -dout "+dout

    if noskip != '#':
        visual+=" -noskip "+noskip
    if buffer != '#':
        visual+=" -buffer "+buffer
    #execute command
    print visual
    return os.system(visual)        

if __name__=="__main__":
    #codebook file
    cin = sys.argv[1]
    #input data
    din = sys.argv[2]
    #output filename
    dout = sys.argv[3]
    #do not skip masked vectors
    noskip = sys.argv[4]
    #buffer reading of data
    buffer = sys.argv[5]

    visual(cin,din,dout,noskip,buffer)