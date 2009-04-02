import sys
import lib.som.CODtoDBF

if __name__=="__main__":
    codfile=sys.argv[1]
    dfile=sys.argv[2]
    N=int(sys.argv[3])
    lib.som.CODtoDBF.CODtoDBF(codfile,dfile,N)
