import os, sys, subprocess, math
import lib.shp.geometry
import random

def text(string="Example SVG text 1",x=20,y=40):
    return "<text x=\""+str(x)+"\" y=\""+str(y)+"\" style=\"font-family: Courier; font-size: 34; stroke: #000000; fill : #000000;\">"+string+"</text>"

def rectangle(x=10,y=10,height=100,width=100,stroke="000000",fill="FFFFFF"):
    return "<rect x=\""+str(x)+"\" y=\""+str(y)+"\" height=\""+str(height)+"\" width=\""+str(width)+"\" style=\"stroke:#"+stroke+"; fill: #"+fill+"\"/>"


def polyline(points,stroke="000000",fill="FFFFFF"):
    return "<polyline points=\""+" ".join([str(x)+","+str(y) for x,y in points])+"\" style=\"stroke:#"+stroke+"; fill: #"+fill+"\"/>"

def line(points):
    (x1,y1),(x2,y2)=points
    return "<line x1=\""+str(x1)+"\"  y1=\""+str(y1)+"\" x2=\""+str(x2)+"\"   y2=\""+str(y2)+"\" style=\"stroke:#000000;\"/>"

def downarrow(x,y,l,h,a):
    deltaX=h*math.cos(math.pi*(a/float(180)))
    deltaY=h*math.sin(math.pi*(a/float(180)))
    return line([(x,y),(x,y+l)])+"\n"+line([(x,y+l),(x-deltaX,y+l-deltaY)])+"\n"+line([(x,y+l),(x+deltaX,y+l-deltaY)])

def rightarrow(x,y,l,h,a):
    deltaX=h*math.cos(math.pi*(a/float(180)))
    deltaY=h*math.sin(math.pi*(a/float(180)))
    return line([(x,y),(x+l,y)])+"\n"+line([(x+l,y),(x+l-deltaX,y-deltaY)])+"\n"+line([(x+l,y),(x+l-deltaX,y+deltaY)])

def multiline(points):
    xml=""
    for i in range(len(points)-1):
        xml=xml+line([points[i],points[i+1]])+"\n"
    return xml

def som(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    colors=["ff","e6","cc","b3","99","80"]
    for x,y in lib.shp.geometry.hexagonGrid(0,3,0,4,60):
        color="ffffff"
        points=lib.shp.geometry.hexagon(x+20,y,30)
        outfile.write(polyline(points+[points[0]],"000000",color)+"\n")
    for x,y in lib.shp.geometry.hexagonGrid(0,3,0,4,60):
        color="ffffff"
        points=lib.shp.geometry.hexagon(x+10,y+10,30)
        outfile.write(polyline(points+[points[0]],"000000",color)+"\n")
    for x,y in lib.shp.geometry.hexagonGrid(0,3,0,4,60):
        color="ffffff"
        points=lib.shp.geometry.hexagon(x,y+20,30)
        outfile.write(polyline(points+[points[0]],"000000",color)+"\n")
    outfile.write("</svg>")
    outfile.close()        

def shape(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
##    colors=["ff","e6","cc","b3","99","80"]
    d=60
    r=30
    for x,y in lib.shp.geometry.hexagonGrid(0,3,0,4,d):
##        i=random.randint(0,2)
##        j=random.randint(1,9)
##        color=colors[((i*10)+j)/5]*3
        points=lib.shp.geometry.hexagon(x+30,y+5,r)
        outfile.write(polyline(points+[points[0]],"000000","ffffff")+"\n")
##        prob=random.random()
##        if prob < 0.15:
##            dots=3
##        elif prob < 0.4:
##            dots=2
##        elif prob < 0.75:
##            dots=1
##        else:
##            dots=0
##        for i in range(dots):
##            outfile.write(text(".",x+random.randint(0,20),y+random.randint(0,16))+"\n")
    outfile.write("</svg>")
    outfile.close()
    
def umat(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    colors=["ff","e6","cc","b3","99","80"]
    d=60
    r=30
    for x,y in lib.shp.geometry.hexagonGrid(0,3,0,4,d):
        i=random.randint(0,2)
        j=random.randint(1,9)
        color=colors[((i*10)+j)/5]*3
        points=lib.shp.geometry.hexagon(x+30,y+5,r)
        outfile.write(polyline(points+[points[0]],"000000",color)+"\n")
        outfile.write(text(str(i)+"."+str(j),x,y+15)+"\n")
    outfile.write("</svg>")
    outfile.close()        

def visual(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    colors=["ff","e6","cc","b3","99","80"]
    d=60
    r=30

    i=[]
    j=[]
    for lcv in range(12):
        i.append(random.randint(0,2))
        j.append(random.randint(1,9))
    bmu=zip(i,j).index(min(zip(i,j)))
    for id,(x,y) in enumerate(lib.shp.geometry.hexagonGrid(0,3,0,4,d)):
        color=colors[((i[id]*10)+j[id])/5]*3
        points=lib.shp.geometry.hexagon(x+30,y+5,r)
        outfile.write(polyline(points+[points[0]],"888888",color)+"\n")
        outfile.write(text(str(i[id])+"."+str(j[id]),x,y+15)+"\n")
        if id==bmu:
            outfile.write(multiline(points+[points[0]])+"\n")
    outfile.write("</svg>")
    outfile.close()        

def pngrender(infile,outfile):
    cmd = "E:/InkscapePortable/App/Inkscape/inkscape.exe --export-area-drawing --export-png="
    subprocess.Popen(cmd+outfile+" "+infile, shell=True)

def csv(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    outfile.write(rectangle(10,10,35,115)+"\n")
    outfile.write(rectangle(10,45,70,115)+"\n")
    outfile.write(text("*.csv",15,35)+"\n")
    outfile.write(text("A,B,C",15,70)+"\n")
    outfile.write(text("1,2,3",15,105)+"\n")
    outfile.write("</svg>")
    outfile.close()
    
def tsv(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    outfile.write(rectangle(10,10,35,115)+"\n")
    outfile.write(rectangle(10,45,70,115)+"\n")
    outfile.write(text("*.tsv",15,35)+"\n")
    outfile.write(text("A B C",15,70)+"\n")
    outfile.write(text("1 2 3",15,105)+"\n")
    outfile.write("</svg>")
    outfile.close()

def dbf(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    outfile.write(rectangle(10,10,30,175)+"\n")
    outfile.write(rectangle(10,40,65,175)+"\n")
    outfile.write(text("*.dbf",45,35)+"\n")
    outfile.write(text("01001100",15,65)+"\n")
    outfile.write(text("ABC123",15,95)+"\n")
    outfile.write("</svg>")
    outfile.close()
    
def dat(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    outfile.write(rectangle(10,10,30,175)+"\n")
    outfile.write(rectangle(10,40,95,175)+"\n")
    outfile.write(text("*.dat",45,35)+"\n")
    outfile.write(text("3",15,65)+"\n")
    outfile.write(text("#n A B C",15,95)+"\n")
    outfile.write(text("1 2 3",15,125)+"\n")
    outfile.write("</svg>")
    outfile.close()

def datH(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")

    #dbf file
    yoffset=15
    outfile.write(rectangle(10,10+yoffset,30,175)+"\n")
    outfile.write(rectangle(10,40+yoffset,65,175)+"\n")
    outfile.write(text("*.dbf",45,35+yoffset)+"\n")
    outfile.write(text("01001100",15,65+yoffset)+"\n")
    outfile.write(text("ABC123",15,95+yoffset)+"\n")

    #arrow
    outfile.write(rightarrow(200,55+yoffset,35,10,60)+"\n")

    #dat file
    xoffset=235
    outfile.write(rectangle(10+xoffset,10,30,175)+"\n")
    outfile.write(rectangle(10+xoffset,40,95,175)+"\n")
    outfile.write(text("*.dat",45+xoffset,35)+"\n")
    outfile.write(text("3",15+xoffset,65)+"\n")
    outfile.write(text("#n A B C",15+xoffset,95)+"\n")
    outfile.write(text("1 2 3",15+xoffset,125)+"\n")

    outfile.write("</svg>")
    outfile.close()

def datV(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")

    #dbf file
    xoffset=0
    yoffset=0
    outfile.write(rectangle(10,10+yoffset,30,175)+"\n")
    outfile.write(rectangle(10,40+yoffset,65,175)+"\n")
    outfile.write(text("*.dbf",45,35+yoffset)+"\n")
    outfile.write(text("01001100",15,65+yoffset)+"\n")
    outfile.write(text("ABC123",15,95+yoffset)+"\n")

    #arrow
    outfile.write(downarrow(95,125,35,10,60)+"\n")

    #dat file
    xoffset=0
    yoffset=160
    outfile.write(rectangle(10+xoffset,10+yoffset,30,175)+"\n")
    outfile.write(rectangle(10+xoffset,40+yoffset,95,175)+"\n")
    outfile.write(text("*.dat",45+xoffset,35+yoffset)+"\n")
    outfile.write(text("3",15+xoffset,65+yoffset)+"\n")
    outfile.write(text("#n A B C",15+xoffset,95+yoffset)+"\n")
    outfile.write(text("1 2 3",15+xoffset,125+yoffset)+"\n")

    outfile.write("</svg>")
    outfile.close()
    
def toXbaseV(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")

    #csv file
    xoffset=30
    outfile.write(rectangle(10+xoffset,10,35,115)+"\n")
    outfile.write(rectangle(10+xoffset,45,70,115)+"\n")
    outfile.write(text("*.csv",15+xoffset,35)+"\n")
    outfile.write(text("A,B,C",15+xoffset,70)+"\n")
    outfile.write(text("1,2,3",15+xoffset,105)+"\n")

    #or
    outfile.write(text("or",45+xoffset,140)+"\n")

    #tsv file
    yoffset=140
    outfile.write(rectangle(10+xoffset,10+yoffset,35,115)+"\n")
    outfile.write(rectangle(10+xoffset,45+yoffset,70,115)+"\n")
    outfile.write(text("*.tsv",15+xoffset,35+yoffset)+"\n")
    outfile.write(text("A B C",15+xoffset,70+yoffset)+"\n")
    outfile.write(text("1 2 3",15+xoffset,105+yoffset)+"\n")

    #arrow
    outfile.write(downarrow(65+xoffset,270,35,10,60)+"\n")

    #dbf file
    yoffset=305
    outfile.write(rectangle(10,10+yoffset,35,175)+"\n")
    outfile.write(rectangle(10,45+yoffset,70,175)+"\n")
    outfile.write(text("*.dbf",45,35+yoffset)+"\n")
    outfile.write(text("01001100",15,70+yoffset)+"\n")
    outfile.write(text("ABC123",15,105+yoffset)+"\n")

    outfile.write("</svg>")
    outfile.close()

def toXbaseH(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")

    #csv file
    xoffset=0
    outfile.write(rectangle(10+xoffset,10,35,115)+"\n")
    outfile.write(rectangle(10+xoffset,45,70,115)+"\n")
    outfile.write(text("*.csv",15+xoffset,35)+"\n")
    outfile.write(text("A,B,C",15+xoffset,70)+"\n")
    outfile.write(text("1,2,3",15+xoffset,105)+"\n")

    #or
    outfile.write(text("or",135,70)+"\n")

    #tsv file
    xoffset=175
    yoffset=0
    outfile.write(rectangle(10+xoffset,10+yoffset,35,115)+"\n")
    outfile.write(rectangle(10+xoffset,45+yoffset,70,115)+"\n")
    outfile.write(text("*.tsv",15+xoffset,35+yoffset)+"\n")
    outfile.write(text("A B C",15+xoffset,70+yoffset)+"\n")
    outfile.write(text("1 2 3",15+xoffset,105+yoffset)+"\n")

    #arrow
    outfile.write(rightarrow(320,60,35,10,60)+"\n")

    #dbf file
    yoffset=0
    xoffset=355
    outfile.write(rectangle(10+xoffset,10+yoffset,35,175)+"\n")
    outfile.write(rectangle(10+xoffset,45+yoffset,70,175)+"\n")
    outfile.write(text("*.dbf",45+xoffset,35+yoffset)+"\n")
    outfile.write(text("01001100",15+xoffset,70+yoffset)+"\n")
    outfile.write(text("ABC123",15+xoffset,105+yoffset)+"\n")

    outfile.write("</svg>")
    outfile.close()
    
def mergeV(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")

    #first table
    outfile.write(polyline([(10,45),(10,10),(125,10),(125,115),(10,115),(10,45),(125,45)])+"\n")
    outfile.write(polyline([(50,10),(50,115)])+"\n")
    outfile.write(polyline([(90,10),(90,115)])+"\n")

    outfile.write(text("A",15,35)+"\n")
    outfile.write(text("B",55,35)+"\n")
    outfile.write(text("C",95,35)+"\n")

    outfile.write(text("1",15,70)+"\n")
    outfile.write(text("2",55,70)+"\n")
    outfile.write(text("3",95,70)+"\n")

    outfile.write(text(".",15,85)+"\n")
    outfile.write(text(".",55,85)+"\n")
    outfile.write(text(".",95,85)+"\n")
    outfile.write(text(".",15,95)+"\n")
    outfile.write(text(".",55,95)+"\n")
    outfile.write(text(".",95,95)+"\n")
    outfile.write(text(".",15,105)+"\n")
    outfile.write(text(".",55,105)+"\n")
    outfile.write(text(".",95,105)+"\n")

    #plus sign    
    outfile.write(text("+",55,140)+"\n")
    
    #second table
    yoffset=140
    outfile.write(polyline([(10,45+yoffset),(10,10+yoffset),(125,10+yoffset),
                            (125,115+yoffset),(10,115+yoffset),(10,45+yoffset),
                            (125,45+yoffset)])+"\n")
    outfile.write(polyline([(50,10+yoffset),(50,115+yoffset)])+"\n")
    outfile.write(polyline([(90,10+yoffset),(90,115+yoffset)])+"\n")

    outfile.write(text("A",15,35+yoffset)+"\n")
    outfile.write(text("B",55,35+yoffset)+"\n")
    outfile.write(text("C",95,35+yoffset)+"\n")

    outfile.write(text("4",15,70+yoffset)+"\n")
    outfile.write(text("5",55,70+yoffset)+"\n")
    outfile.write(text("6",95,70+yoffset)+"\n")

    outfile.write(text(".",15,85+yoffset)+"\n")
    outfile.write(text(".",55,85+yoffset)+"\n")
    outfile.write(text(".",95,85+yoffset)+"\n")
    outfile.write(text(".",15,95+yoffset)+"\n")
    outfile.write(text(".",55,95+yoffset)+"\n")
    outfile.write(text(".",95,95+yoffset)+"\n")
    outfile.write(text(".",15,105+yoffset)+"\n")
    outfile.write(text(".",55,105+yoffset)+"\n")
    outfile.write(text(".",95,105+yoffset)+"\n")

    #arrow
    outfile.write(downarrow(70,270,35,10,60)+"\n")

    #final table
    yoffset=305
    outfile.write(polyline([(10,45+yoffset),(10,10+yoffset),(125,10+yoffset),
                            (125,185+yoffset),(10,185+yoffset),(10,45+yoffset),
                            (125,45+yoffset)])+"\n")
    outfile.write(polyline([(50,10+yoffset),(50,185+yoffset)])+"\n")
    outfile.write(polyline([(90,10+yoffset),(90,185+yoffset)])+"\n")

    outfile.write(text("A",15,35+yoffset)+"\n")
    outfile.write(text("B",55,35+yoffset)+"\n")
    outfile.write(text("C",95,35+yoffset)+"\n")

    outfile.write(text("1",15,70+yoffset)+"\n")
    outfile.write(text("2",55,70+yoffset)+"\n")
    outfile.write(text("3",95,70+yoffset)+"\n")

    outfile.write(text(".",15,85+yoffset)+"\n")
    outfile.write(text(".",55,85+yoffset)+"\n")
    outfile.write(text(".",95,85+yoffset)+"\n")
    outfile.write(text(".",15,95+yoffset)+"\n")
    outfile.write(text(".",55,95+yoffset)+"\n")
    outfile.write(text(".",95,95+yoffset)+"\n")
    outfile.write(text(".",15,105+yoffset)+"\n")
    outfile.write(text(".",55,105+yoffset)+"\n")
    outfile.write(text(".",95,105+yoffset)+"\n")

    outfile.write(text("4",15,140+yoffset)+"\n")
    outfile.write(text("5",55,140+yoffset)+"\n")
    outfile.write(text("6",95,140+yoffset)+"\n")

    outfile.write(text(".",15,155+yoffset)+"\n")
    outfile.write(text(".",55,155+yoffset)+"\n")
    outfile.write(text(".",95,155+yoffset)+"\n")
    outfile.write(text(".",15,165+yoffset)+"\n")
    outfile.write(text(".",55,165+yoffset)+"\n")
    outfile.write(text(".",95,165+yoffset)+"\n")
    outfile.write(text(".",15,175+yoffset)+"\n")
    outfile.write(text(".",55,175+yoffset)+"\n")
    outfile.write(text(".",95,175+yoffset)+"\n")

    
    outfile.write("</svg>")
    outfile.close()

def mergeH(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")

    #first table
    yoffset=35
    outfile.write(polyline([(10,45+yoffset),(10,10+yoffset),(125,10+yoffset),
                            (125,115+yoffset),(10,115+yoffset),(10,45+yoffset),
                            (125,45+yoffset)])+"\n")
    outfile.write(polyline([(50,10+yoffset),(50,115+yoffset)])+"\n")
    outfile.write(polyline([(90,10+yoffset),(90,115+yoffset)])+"\n")

    outfile.write(text("A",15,35+yoffset)+"\n")
    outfile.write(text("B",55,35+yoffset)+"\n")
    outfile.write(text("C",95,35+yoffset)+"\n")

    outfile.write(text("1",15,70+yoffset)+"\n")
    outfile.write(text("2",55,70+yoffset)+"\n")
    outfile.write(text("3",95,70+yoffset)+"\n")

    outfile.write(text(".",15,85+yoffset)+"\n")
    outfile.write(text(".",55,85+yoffset)+"\n")
    outfile.write(text(".",95,85+yoffset)+"\n")
    outfile.write(text(".",15,95+yoffset)+"\n")
    outfile.write(text(".",55,95+yoffset)+"\n")
    outfile.write(text(".",95,95+yoffset)+"\n")
    outfile.write(text(".",15,105+yoffset)+"\n")
    outfile.write(text(".",55,105+yoffset)+"\n")
    outfile.write(text(".",95,105+yoffset)+"\n")

    #plus sign    
    outfile.write(text("+",135,105)+"\n")
    
    #second table
    yoffset=35
    xoffset=155
    outfile.write(polyline([(10+xoffset,45+yoffset),(10+xoffset,10+yoffset),(125+xoffset,10+yoffset),
                            (125+xoffset,115+yoffset),(10+xoffset,115+yoffset),(10+xoffset,45+yoffset),
                            (125+xoffset,45+yoffset)])+"\n")
    outfile.write(polyline([(50+xoffset,10+yoffset),(50+xoffset,115+yoffset)])+"\n")
    outfile.write(polyline([(90+xoffset,10+yoffset),(90+xoffset,115+yoffset)])+"\n")

    outfile.write(text("A",15+xoffset,35+yoffset)+"\n")
    outfile.write(text("B",55+xoffset,35+yoffset)+"\n")
    outfile.write(text("C",95+xoffset,35+yoffset)+"\n")

    outfile.write(text("4",15+xoffset,70+yoffset)+"\n")
    outfile.write(text("5",55+xoffset,70+yoffset)+"\n")
    outfile.write(text("6",95+xoffset,70+yoffset)+"\n")

    outfile.write(text(".",15+xoffset,85+yoffset)+"\n")
    outfile.write(text(".",55+xoffset,85+yoffset)+"\n")
    outfile.write(text(".",95+xoffset,85+yoffset)+"\n")
    outfile.write(text(".",15+xoffset,95+yoffset)+"\n")
    outfile.write(text(".",55+xoffset,95+yoffset)+"\n")
    outfile.write(text(".",95+xoffset,95+yoffset)+"\n")
    outfile.write(text(".",15+xoffset,105+yoffset)+"\n")
    outfile.write(text(".",55+xoffset,105+yoffset)+"\n")
    outfile.write(text(".",95+xoffset,105+yoffset)+"\n")

    #arrow
    outfile.write(rightarrow(295,95,35,10,60)+"\n")

    #final table
    xoffset=335
    yoffset=0
    outfile.write(polyline([(10+xoffset,45+yoffset),(10+xoffset,10+yoffset),(125+xoffset,10+yoffset),
                            (125+xoffset,185+yoffset),(10+xoffset,185+yoffset),(10+xoffset,45+yoffset),
                            (125+xoffset,45+yoffset)])+"\n")
    outfile.write(polyline([(50+xoffset,10+yoffset),(50+xoffset,185+yoffset)])+"\n")
    outfile.write(polyline([(90+xoffset,10+yoffset),(90+xoffset,185+yoffset)])+"\n")

    outfile.write(text("A",15+xoffset,35+yoffset)+"\n")
    outfile.write(text("B",55+xoffset,35+yoffset)+"\n")
    outfile.write(text("C",95+xoffset,35+yoffset)+"\n")

    outfile.write(text("1",15+xoffset,70+yoffset)+"\n")
    outfile.write(text("2",55+xoffset,70+yoffset)+"\n")
    outfile.write(text("3",95+xoffset,70+yoffset)+"\n")

    outfile.write(text(".",15+xoffset,85+yoffset)+"\n")
    outfile.write(text(".",55+xoffset,85+yoffset)+"\n")
    outfile.write(text(".",95+xoffset,85+yoffset)+"\n")
    outfile.write(text(".",15+xoffset,95+yoffset)+"\n")
    outfile.write(text(".",55+xoffset,95+yoffset)+"\n")
    outfile.write(text(".",95+xoffset,95+yoffset)+"\n")
    outfile.write(text(".",15+xoffset,105+yoffset)+"\n")
    outfile.write(text(".",55+xoffset,105+yoffset)+"\n")
    outfile.write(text(".",95+xoffset,105+yoffset)+"\n")

    outfile.write(text("4",15+xoffset,140+yoffset)+"\n")
    outfile.write(text("5",55+xoffset,140+yoffset)+"\n")
    outfile.write(text("6",95+xoffset,140+yoffset)+"\n")

    outfile.write(text(".",15+xoffset,155+yoffset)+"\n")
    outfile.write(text(".",55+xoffset,155+yoffset)+"\n")
    outfile.write(text(".",95+xoffset,155+yoffset)+"\n")
    outfile.write(text(".",15+xoffset,165+yoffset)+"\n")
    outfile.write(text(".",55+xoffset,165+yoffset)+"\n")
    outfile.write(text(".",95+xoffset,165+yoffset)+"\n")
    outfile.write(text(".",15+xoffset,175+yoffset)+"\n")
    outfile.write(text(".",55+xoffset,175+yoffset)+"\n")
    outfile.write(text(".",95+xoffset,175+yoffset)+"\n")

    
    outfile.write("</svg>")
    outfile.close()

def selectV(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")

    #first table
    outfile.write(rectangle(10,80,35,115,"888888","888888")+"\n")
    outfile.write(rectangle(10,150,35,115,"888888","888888")+"\n")
    
    outfile.write(multiline([(10,45),(10,10),(125,10),(125,185),(10,185),(10,45),(125,45)])+"\n")
    outfile.write(line([(50,10),(50,185)])+"\n")
    outfile.write(line([(90,10),(90,185)])+"\n")

    
    outfile.write(text("A",15,35)+"\n")
    outfile.write(text("B",55,35)+"\n")
    outfile.write(text("C",95,35)+"\n")

    outfile.write(text("1",15,70)+"\n")
    outfile.write(text("2",55,70)+"\n")
    outfile.write(text("3",95,70)+"\n")

    outfile.write(text(".",15,85)+"\n")
    outfile.write(text(".",55,85)+"\n")
    outfile.write(text(".",95,85)+"\n")
    outfile.write(text(".",15,95)+"\n")
    outfile.write(text(".",55,95)+"\n")
    outfile.write(text(".",95,95)+"\n")
    outfile.write(text(".",15,105)+"\n")
    outfile.write(text(".",55,105)+"\n")
    outfile.write(text(".",95,105)+"\n")

    outfile.write(text("4",15,140)+"\n")
    outfile.write(text("5",55,140)+"\n")
    outfile.write(text("6",95,140)+"\n")

    outfile.write(text(".",15,155)+"\n")
    outfile.write(text(".",55,155)+"\n")
    outfile.write(text(".",95,155)+"\n")
    outfile.write(text(".",15,165)+"\n")
    outfile.write(text(".",55,165)+"\n")
    outfile.write(text(".",95,165)+"\n")
    outfile.write(text(".",15,175)+"\n")
    outfile.write(text(".",55,175)+"\n")
    outfile.write(text(".",95,175)+"\n")

    #arrow
    outfile.write(downarrow(70,205,35,10,60)+"\n")
    
    #second table
    yoffset=245
    outfile.write(polyline([(10,45+yoffset),(10,10+yoffset),(125,10+yoffset),
                            (125,115+yoffset),(10,115+yoffset),(10,45+yoffset),
                            (125,45+yoffset)])+"\n")
    outfile.write(polyline([(50,10+yoffset),(50,115+yoffset)])+"\n")
    outfile.write(polyline([(90,10+yoffset),(90,115+yoffset)])+"\n")

    outfile.write(text("A",15,35+yoffset)+"\n")
    outfile.write(text("B",55,35+yoffset)+"\n")
    outfile.write(text("C",95,35+yoffset)+"\n")

    outfile.write(text("1",15,70+yoffset)+"\n")
    outfile.write(text("2",55,70+yoffset)+"\n")
    outfile.write(text("3",95,70+yoffset)+"\n")
    outfile.write(text("4",15,105+yoffset)+"\n")
    outfile.write(text("5",55,105+yoffset)+"\n")
    outfile.write(text("6",95,105+yoffset)+"\n")
    
    outfile.write("</svg>")
    outfile.close()

def selectH(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")

    #first table
    outfile.write(rectangle(10,80,35,115,"888888","888888")+"\n")
    outfile.write(rectangle(10,150,35,115,"888888","888888")+"\n")
    
    outfile.write(multiline([(10,45),(10,10),(125,10),(125,185),(10,185),(10,45),(125,45)])+"\n")
    outfile.write(line([(50,10),(50,185)])+"\n")
    outfile.write(line([(90,10),(90,185)])+"\n")

    
    outfile.write(text("A",15,35)+"\n")
    outfile.write(text("B",55,35)+"\n")
    outfile.write(text("C",95,35)+"\n")

    outfile.write(text("1",15,70)+"\n")
    outfile.write(text("2",55,70)+"\n")
    outfile.write(text("3",95,70)+"\n")

    outfile.write(text(".",15,85)+"\n")
    outfile.write(text(".",55,85)+"\n")
    outfile.write(text(".",95,85)+"\n")
    outfile.write(text(".",15,95)+"\n")
    outfile.write(text(".",55,95)+"\n")
    outfile.write(text(".",95,95)+"\n")
    outfile.write(text(".",15,105)+"\n")
    outfile.write(text(".",55,105)+"\n")
    outfile.write(text(".",95,105)+"\n")

    outfile.write(text("4",15,140)+"\n")
    outfile.write(text("5",55,140)+"\n")
    outfile.write(text("6",95,140)+"\n")

    outfile.write(text(".",15,155)+"\n")
    outfile.write(text(".",55,155)+"\n")
    outfile.write(text(".",95,155)+"\n")
    outfile.write(text(".",15,165)+"\n")
    outfile.write(text(".",55,165)+"\n")
    outfile.write(text(".",95,165)+"\n")
    outfile.write(text(".",15,175)+"\n")
    outfile.write(text(".",55,175)+"\n")
    outfile.write(text(".",95,175)+"\n")

    #arrow
    outfile.write(rightarrow(145,95,35,10,60)+"\n")
    
    #second table
    xoffset=185
    yoffset=35
    outfile.write(polyline([(10+xoffset,45+yoffset),(10+xoffset,10+yoffset),(125+xoffset,10+yoffset),
                            (125+xoffset,115+yoffset),(10+xoffset,115+yoffset),(10+xoffset,45+yoffset),
                            (125+xoffset,45+yoffset)])+"\n")
    outfile.write(polyline([(50+xoffset,10+yoffset),(50+xoffset,115+yoffset)])+"\n")
    outfile.write(polyline([(90+xoffset,10+yoffset),(90+xoffset,115+yoffset)])+"\n")

    outfile.write(text("A",15+xoffset,35+yoffset)+"\n")
    outfile.write(text("B",55+xoffset,35+yoffset)+"\n")
    outfile.write(text("C",95+xoffset,35+yoffset)+"\n")

    outfile.write(text("1",15+xoffset,70+yoffset)+"\n")
    outfile.write(text("2",55+xoffset,70+yoffset)+"\n")
    outfile.write(text("3",95+xoffset,70+yoffset)+"\n")
    outfile.write(text("4",15+xoffset,105+yoffset)+"\n")
    outfile.write(text("5",55+xoffset,105+yoffset)+"\n")
    outfile.write(text("6",95+xoffset,105+yoffset)+"\n")
    
    outfile.write("</svg>")
    outfile.close()
    
if __name__=="__main__":
    svgpath = sys.argv[0][:sys.argv[0].rfind("\\")]+"\\doc\\xml\\svg\\"
    pngpath = sys.argv[0][:sys.argv[0].rfind("\\")]+"\\doc\\sphinx\\_images\\toolbox\\"

    svgname=svgpath+"vsom.svg"
    pngname=pngpath+"vsom.png"
    som(svgname)
    pngrender(svgname,pngname)