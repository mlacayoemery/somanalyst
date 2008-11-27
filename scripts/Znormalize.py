#Martin Lacayo-Emery
#10/18/2008
#computes z-score using population statistics


import sys

def normalize(inName,outName,direction,denorm):
    stdDevZero=0
    
    infile=open(inName,'r')
    outfile=open(outName,'w')

    outfile.write(infile.readline())

    if (direction=="column") or (direction=="global"):
        #readd in table and convert it to numbers
        table=[]
        for l in infile.readlines():
            line=l.split(",")
            try:
                table.append(line[:2]+map(eval,line[2:]))
            #don't crash on empty lines
            except TypeError:
                pass
        if (direction=="column"):
            N=float(len(table))

            averages=[0]*len(table[0][2:])
            stdDevs=[0]*len(table[0][2:])
            
            for l in table:
                for id,x in enumerate(l[2:]):
                    averages[id]+=x/N
            for l in table:
                for id,x in enumerate(l[2:]):
                    stdDevs[id]+=((x-averages[id])**2)/N
            for id,s in enumerate(stdDevs):
                stdDevs[id]=s**0.5
                
            for l in table:
                row=l[:2]
                for id,x in enumerate(l[2:]):
                    try:
                        row.append(str((x-averages[id])/stdDevs[id]))
                    except ZeroDivisionError:
                        row.append(str(stdDevZero))
                        
                outfile.write(','.join(row)+"\n")
            #if denormalization file wanted
            if denorm:
                o=open(denorm,'w')
                o.write("#Martin Lacayo-Emery\n#This script was produced using SOM Analyst.\ndef denorm(table):\n"+
                        "\taverages="+str(averages)+"\n\tstdDevs="+str(stdDevs)+"\n\tdenormTable=[]"+
                        "\n\tfor row in table:\n\t\tdenormRow=[]\n\t\tfor id,value in enumerate(row):"+
                        "\n\t\t\tdenormRow.append((value*stdDevs[id])+averages[id])"+
                        "\n\t\tdenormTable.append(denormRow)"+
                        "\n\treturn denormTable")
                o.close()
                
        else:
            N=float(len(table)*(len(table[0])-2))
            average=0
            stdDev=0
            for l in table:
                for x in l[2:]:
                    average+=x/N
            for l in table:
                for x in l[2:]:
                    stdDev+=((x-average)**2)/N
            stdDev=stdDev**0.5
            
            for l in table:
                row=l[:2]
                for x in l[2:]:
                    try:
                        row.append(str((x-average)/stdDev))
                    except ZeroDivisionError:
                        row.append(str(stdDevZero))
                outfile.write(','.join(row)+"\n")

    elif (direction=="row"):
        line=infile.readline()
        while(line):
            line=line.split(",")
            row=line[:2]+map(eval,line[2:])

            N=float(len(row[2:]))
            average=sum(row[2:])/N
            stdDev=0
            for x in row[2:]:
                stdDev+=((x-average)**2)/N
            stdDev=stdDev**0.5
            
            for id,x in enumerate(row[2:]):
                try:
                    row[id+2]=(x-average)/stdDev
                except ZeroDivisionError:
                    row[id+2]=stdDevZero
                    
            outfile.write(','.join(map(str,row))+"\n")
            line=infile.readline()
    else:
        pass

    infile.close()
    outfile.close()

        
if __name__ == "__main__":
    inName = sys.argv[1]
    outName = sys.argv[2]
    direction = sys.argv[3]
    denorm = sys.argv[4]
    if denorm=='#':
        denorm=None

    normalize(inName,outName,direction,denorm)    
    