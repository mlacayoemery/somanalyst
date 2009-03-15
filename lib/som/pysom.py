#Maritn Lacayo-Emery

#returns a list of immediate neighbors in a hex grid
#list in clockwise order
#bottom left corner always non-offset
def hexNeighbors(x,y,xmin=0,xmax=0,ymin=0,ymax=0,spacing=1)
    spacingX=spacing
    spacingY=spacing
    halfspacingX=spacing/2
    #in range
    if ((xmin <= x) and (x <= xmax)) and ((ymin <= y) and (y <= ymax)):
        if x==xmin:
            if y==ymin:
                #left bottom cornner
                return [(x+halfspacing,y+spacing),(x+spacing,y)]
            elif y==ymax:
                #left top cornner
                if y%2:
                    #offset row
                    return [(),()]
            elif y%2:
                #left offset edge
            else:
                #left non-ofset edge
        elif x==xmax:
            if y==ymin:
                #right bottom cornner
            elif y==ymax:
                #right top cornner
            elif y%2:
                #right offset edge
            else:
                #right non-offset edge
        elif y==ymin:
            #bottom edge
        elif y==ymax:
            #top edge
        else:
            return [(x+halfspacingX,y+spacingY),
                    (x+spacingX,y),
                    (x+halfspacingX,y-spacingY),
                    (x-halfspacingX,y-spacingY),
                    (x-spacingX,y),
                    (x-halfspacingX,y+spaingY)]