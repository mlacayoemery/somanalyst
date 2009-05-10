import sys
import lib.som.normVar

if __name__=="__main__":
    inName=sys.argv[1]
    normBy=sys.argv[2]
    outName=sys.argv[3]
    zeroDivision=float(sys.argv[4])
    if sys.argv[5]=="#":
        decimalPlaces=0
    else:
        decimalPlaces=int(sys.argv[5])
    if sys.argv[6]=="#":
        fieldNames=[]
    else:
        fieldNames=sys.argv[6].split(";")
    
    lib.som.normVar.normalize(inName,outName,fieldNames,normBy,zeroDivision,decimalPlaces)