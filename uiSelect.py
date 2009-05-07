import sys
import lib.som.select

if __name__=="__main__":
    inName=sys.argv[1]
    selectionType=sys.argv[2]
    outName=sys.argv[3]
    if sys.argv[4]=="#":
        columns=[]
    else:
        columns=sys.argv[4].split(";")
    start=int(sys.argv[5])
    step=int(sys.argv[6])
    stop=int(sys.argv[7])
    if sys.argv[8]=="true":
        detectTypes=True
    else:
        detectTypes=False
    lib.som.select.select(inName,selectionType,outName,columns,start,step,stop,detectTypes)