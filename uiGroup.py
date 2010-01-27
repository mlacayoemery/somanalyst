import sys
import lib.som.group

def group(inName,groupBy,groupType,valueType,outName,sortBy,decimalPlaces):
    """
    Groups shapes in a shapefile using the specified parameters.

    :arguments:
      inName
       The input shapefile name.
      groupBy
       The data column to group on.
      groupType
       The type of grouping to create.
      valueType
       The type of value to place in the final ouput.
      outName
       The output shapefile name.
      sortBy (*optional*)
       A column to sort the data by before grouping.
    """
    lib.som.group.group(inName,groupBy,groupType,valueType,outName,sortBy,decimalPlaces)

if __name__=="__main__":
    inName=sys.argv[1]
    groupBy=sys.argv[2]
    groupType=lib.som.group.groupTypes[sys.argv[3]]
    valueType=lib.som.group.valueTypes[sys.argv[4]]
    outName=sys.argv[5]
    if sys.argv[6]=="#":
        sortBy=None
    else:
        sortBy=sys.argv[6]
    decimalPlaces=int(sys.argv[7])
    group(inName,groupBy,groupType,valueType,outName,sortBy,decimalPlaces)