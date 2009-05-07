from ..shp import shapefile

def extent(ifile,ofile):
    i=shapefile.Shapefile(5)
    i.readFile(ifile)
    o=shapefile.Shapefile(5)
    o.add([(i.Xmin,i.Ymin),(i.Xmin,i.Ymax),
           (i.Xmax,i.Ymax),(i.Xmax,i.Ymin),
           (i.Xmin,i.Ymin)])
    o.writeFile(ofile)