import sys
import lib.som.normMinMax

if __name__ == "__main__":
    inName = sys.argv[1]
    direction = sys.argv[2]
    outName = sys.argv[3]
    start = float(sys.argv[5])
    end = float(sys.argv[6])
    minEqMax = float(sys.argv[4])
    if sys.argv[8]=="#":
        fieldNames = []
    else:
        fieldNames=sys.argv[8].split(";")
    if sys.argv[7]=="#":
        decimalPlaces=0
    else:
        decimalPlaces=int(sys.argv[7])

    lib.som.normMinMax.normalize(inName,outName,start,end,direction,minEqMax,fieldNames,decimalPlaces)    