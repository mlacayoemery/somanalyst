import sys
import lib.som.normZ

if __name__ == "__main__":
    inName = sys.argv[1]
    direction = sys.argv[2]
    outName = sys.argv[3]
    if sys.argv[4]=="#":
        zeroDivision=0
    else:
        zeroDivision=float(sys.argv[4])
    if sys.argv[5]=="#":
        decimalPlaces=0
    else:
        decimalPlaces = int(sys.argv[5])
    if sys.argv[6] == "#":
        fieldNames=[]
    else:
        fieldNames = sys.argv[6].split(";")
    lib.som.normZ.normalize(inName,outName,direction,zeroDivision,decimalPlaces,fieldNames)