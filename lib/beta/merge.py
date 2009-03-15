import sys

files=sys.argv[1].split(';')
output=sys.argv[2]
column=sys.argv[4]

o=open(output,'w')
f=open(files[0],'r')
o.write(f.readline().strip())
o.write(","+column+"\n")
f.close()

for i in files:
    stem=i.split('\\')[-1].split('.')[0]
    f=open(i,'r')
    f.readline()
    for l in f.readlines():
        o.write(l.strip())
        o.write(","+stem+"\n")
    f.close()
o.close()
        
   

