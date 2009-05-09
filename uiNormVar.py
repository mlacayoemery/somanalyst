import sys
import lib.som.normVar

if __name__=="__main__":
    inName=sys.argv[1]
    if sys.argv[2]=="#":
        fieldNames=[]
    else:
        fieldNames=sys.argv[2].split(";")
    normBy=sys.argv[3]
    outName=sys.argv[4]
    zeroDivision=float(sys.argv[5])
    
    lib.som.normVar.normalize(inName,outName,fieldNames,normBy,zeroDivision)