import sys

if len(sys.argv)==3:
    iName=sys.argv[1]
    oName=sys.argv[2]
else:
    iName="D:/users/gregg/som.cod"
    oName="D:/users/gregg/rank.cod"

ifile=open(iName)
lines=ifile.readlines()
ifile.close()
ofile=open(oName,'w')

def get2nd(t):
    return t[1]

ofile.write(lines[0])
for l in lines[1:]:
    oline = map(float,l.strip().split(" "))
    oline=zip(oline,range(len(oline)))
    oline.sort(reverse=True)
    ofile.write(' '.join(map(str,map(get2nd,oline)))+"\n")

ofile.close()    
        
        
    
    

    