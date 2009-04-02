import dbftool

def dbfmerge(ifile1,ifile2,ofile):
    t1=dbftool.dbfreader(ifile1)
    t2=dbftool.dbfreader(ifile2)

    fn1=t1.next()
    fn2=t2.next()
    fn1.extend(fn2)

    fs1=t1.next()
    fs2=t2.next()
    fs1.extend(fs2)


    fnames=fn1
    fspecs=fs1

    recs1=[]
    recs=[]
    for i in t1:
        recs1.append(i)
    for i,j in enumerate(t2):
        recs.append(recs1[i]+j)

    dbftool.dbfwriter(ofile,fnames,fspecs,recs)
    ofile.close()
        
