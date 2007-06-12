outfile=open('G:/arcSOM/test.txt','w')
outfile.write("Name:Martin\n")
outfile.write("Phone:802-879-1126")
outfile.close()

outfile=open('G:/arcSOM/test.txt','r+')
print
for l in outfile.readlines():
    print l,
    
outfile.seek(5)
outfile.write("Lacayo")
outfile.seek(19)
outfile.write("503-931-4073")
outfile.close()

outfile=open('G:/arcSOM/test.txt','r')
print
for l in outfile.readlines():
    print l,
outfile.close()