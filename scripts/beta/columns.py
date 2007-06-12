import sys

ifile=sys.argv[1]
columns=map(int,sys.argv[2].split(";"))
ofile=sys.argv[3]

i=open(ifile,'r')
o=open(ofile,'w')

for l in i.readlines():
    l=l.strip().split(',')
    line=[]
    for c in columns:
        line.append(l[c])
    o.write(','.join(line)+'\n')

i.close()
o.close()