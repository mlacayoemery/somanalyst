#TXTvalid tests if a file is a valid data text file
#input: file name, check level
#output: None
#return: pass level
#
#the meaning of levels are as follows
#0: no check, failed check
#1: contains a valid header line
#2: included data conforms to header line
#3: included data is of type float

import sys

def validator(fName, level):
    iFile=open(fName)

    try:
        dim=int(iFile.readline())
        if level == 1:
            return 1
    except ValueError:
        return 0

    if level==2:
        while(line=iFile.readline()):
            if len(line.split()) != dim:
                return 
    
    

if __name__=="__main__":
    fName=sys.argv[1]
    level=int(sys.argv[2])

    try:
        validator(fName, level)
    except error:
        if error == ValueError:
            return 0