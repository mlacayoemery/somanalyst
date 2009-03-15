#subset allows a users to subset data

import sys

def subset(iFile,oFile,start,stop,step):
    output=open(oFile,'w')
    result=[str(r) for r in range(start,stop,step)]
    for r in result:
        output.write(r)
        output.write('\n')
    output.close()

if __name__=="__main__":
    iFile=sys.argv[1]
    oFile=sys.argv[2]
    start=int(sys.argv[3])
    stop=int(sys.argv[4])
    step=int(sys.argv[5])

    subset(iFile,oFile,start,stop,step)