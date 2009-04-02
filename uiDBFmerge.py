import sys
import lib.som.dbfmerge

if __name__=="__main__":
    ifile1=open(sys.argv[1],'rb')
    ifile2=open(sys.argv[2],'rb')
    ofile=open(sys.argv[3],'wb')
    lib.som.dbfmerge.dbfmerge(ifile1,ifile2,ofile)