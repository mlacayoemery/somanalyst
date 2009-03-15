#input file
ifile="z:/svn/data/example/BMUdata.txt"
ofile="z:/svn/data/example/segs/bmustate"

names=["Alabama","Arizona","Arkansas","California","Colorado",
       "Connecticut","Delaware","District_of_Columbia","Florida","Georgia",
       "Idaho","Illinois","Indiana","Iowa","Kansas",
       "Kentucky","Louisiana","Maine","Maryland","Massachusetts",
       "Michigan","Minnesota","Mississippi","Missouri","Montana",
       "Nebraska","Nevada","New_Hampshire","New_Jersey","New_Mexico",
       "New_York","North_Carolina","North_Dakota","Ohio","Oklahoma",
       "Oregon","Pennsylvania","Rhode_Island","South_Carolina","South_Dakota",
       "Tennessee","Texas","Utah","Vermont","Virginia",
       "Washington","West_Virginia","Wisconsin","Wyoming"]

i=open(ifile,'r')

h=i.readline()

lines=i.readlines()
i.close()

lines2=[]
for id,m in enumerate(range(49)):
    for n in range(9):
        o=open(ofile+names[id]+'-'+str(n)+'.txt','w')
        o.write(h)
        l=lines[m+(49*n)]
        l=l.strip().split(' ')
        l[2]=str(1900+(n*10))
        l=' '.join(l)+'\n'
        l2=lines[m+(49*(n+1))]
        l2=l2.strip().split(' ')
        l2[2]=str(1900+((n+1)*10))
        l2=' '.join(l2)+'\n'
        l=l+l2
        o.write(l)
    o.close()

lines=lines2

##for m in range(49):
##    for n in range (9):
##        o=open(ofile+str(m)+'-'+str(n)+'.txt','w')
##        o.write(h)
##        o.write(lines[m+(49*n)])
##        o.write(lines[m+(49*(n+1))])
##        o.close()  
##      
        
    

    
