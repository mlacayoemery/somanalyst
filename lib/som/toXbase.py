import sys, os
from ..shp import databasefile

def toXbaseFile(inName,inType,outName,detectTypes):
    """
    Conversion to Xbase file using paths
    """
    try:
        fileConversion[inType](inName,detectTypes).writeFile(outName)
    except KeyError:
        raise KeyError, "No file conversion key was specified for "+inType

def SVtoDBF(inName,separator,detectTypes):
    d=databasefile.DatabaseFile([],[],[])
    d.readSV(inName,separator)
    if detectTypes:
        d.dynamicSpecs()
    return d

def CSVtoDBF(inName,detectTypes):
    return SVtoDBF(inName,",",detectTypes)

def TSVtoDBF(inName,detectTypes):
    return SVtoDBF(inName,"\t",detectTypes)

fileConversion={"Comma Separated Values (CSV)":CSVtoDBF,
                "Tab Separated Values(TSV)":TSVtoDBF}