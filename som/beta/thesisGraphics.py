#This programs generates the graphics used in the thesis

import Image, ImageDraw
from math import sqrt
import sys

#parameters
ifilename="D:/thesis.png"
isize=(800,600)

#helper functions
def round6(x):
    return round(x,6)

def imageround(x):
    return int(x*dialation)

def pointround(x):
    return [imageround(x[0])+border,imageround(x[1])+ypad]


#main program

def hexagonPoint(box):
    (x1,y1),(x2,y2)=box
    return [(x1,.75*(y1+y2)),(x1,.25*(y1+y2)),(.5*(x1+x2),y1),(x2,.25*(y1+y2)),
            (x2,.75*(y1+y2)),(.5*(x1+x2),y2),
            ]    
    

im = Image.new("RGB",isize)
draw = ImageDraw.Draw(im)

#fill the background white
draw.rectangle([(0,0),im.size],fill=(255,255,255))

#origin upper left

draw.line(hexagonPoint([(10,10),(400,400)]),fill=(0,0,0),width=2)#,outline=(0,0,0))
#draw.ellipse([(50,50),(100,100)],fill=(128,128,128),outline=(0,0,0))

imagefile=open(ifilename,'wb')
im.save(imagefile,'PNG')
imagefile.close()

del draw
