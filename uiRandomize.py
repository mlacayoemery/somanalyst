import sys
import lib.som.randomize

if __name__ == "__main__":
    inName = sys.argv[1]
    outName = sys.argv[2]
    lib.som.randomize.randomize(inName,outName)