import sys
import lib.som.normMinMax

if __name__ == "__main__":
    inName = sys.argv[1]
    direction = sys.argv[2]
    outName = sys.argv[3]
    start = float(sys.argv[4])
    end = float(sys.argv[5])
    minEqMax = float(sys.argv[6])
    if sys.argv[7]=="#":
        fieldNames = []
    else:
        fieldNames=sys.argv[7].split(";")

    lib.som.normMinMax.normalize(inName,outName,start,end,direction,minEqMax,fieldNames)    