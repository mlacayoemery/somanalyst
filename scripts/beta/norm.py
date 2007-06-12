import sys

ifile=sys.argv[1]
ofile=sys.argv[2]

i=open(ifile,'r')
o=open(ofile,'w')

o.write(i.readline())

line=i.readline().split()
line=map(float,line)
table=[line]
#copy
min=line*1
max=line*1
cols=len(line)

for l in i.readlines():
    line=l.split()
    line=map(float,line)
    table.append(line)
    for n in range(cols):
        if line[n] < min[n]:
            min[n]=line[n]
        elif line[n] > max[n]:
            max[n]=line[n]

i.close()

for l in table:
    line=[]
    for id,n in enumerate(l):
        line.append((n-min[id])/(max[id]-min[id]))
    line=' '.join(map(str,line))+'\n'
    o.write(line)

o.close()    
        
