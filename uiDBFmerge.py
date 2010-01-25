import sys
import lib.som.dbfmerge

def dbfmerge(ifile1,ifile2,ofile):
    """
    Creates a single DBF file that contains both input DBF files.

    :arguments:
      ifile1
       The first input DBF file.
      ifile2
       The second input DBF file.
      ofile
       The output DBF file.
       
    """
    lib.som.dbfmerge.dbfmerge(ifile1,ifile2,ofile)
    
if __name__=="__main__":
    ifile1=open(sys.argv[1],'rb')
    ifile2=open(sys.argv[2],'rb')
    ofile=open(sys.argv[3],'wb')
    dbfmerge(ifile1,ifile2,ofile)