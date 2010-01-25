import sys
import lib.som.select

def select(inName,selectionType,outName,columns,start,step,stop,detectTypes):
    """
    Creates a DBF file with the rows from a DBF file that meet the selection criteria.

    :arguments:
      inName
       The input DBF filename.
      selectionType
       The select type (inclulsion or exclusion).
      outName
       The ouput DBF filename.
      columns
       The columns to keep. If no columns are specified, all columns are kept.
      start
       The start index for rows.
      step
       The step between idecies for rows.
      stop
       The stop index for rows.
      detectTypes
       An optional mode that detects and sets the data types for each column in the output file.
       
    """
    lib.som.select.select(inName,selectionType,outName,columns,start,step,stop,detectTypes)
    
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
    select(inName,selectionType,outName,columns,start,step,stop,detectTypes)