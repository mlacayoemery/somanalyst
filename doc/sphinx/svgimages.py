import os, sys, subprocess, math

def text(string="Example SVG text 1",x=20,y=40):
    return "<text x=\""+str(x)+"\" y=\""+str(y)+"\" style=\"font-family: Courier; font-size: 34; stroke: #000000; fill : #000000;\">"+string+"</text>"

def rectangle(x=10,y=10,height=100,width=100,stroke="000000",fill="FFFFFF"):
    return "<rect x=\""+str(x)+"\" y=\""+str(y)+"\" height=\""+str(height)+"\" width=\""+str(width)+"\" style=\"stroke:#"+stroke+"; fill: #"+fill+"\"/>"


def polyline(points):
    return "<polyline points=\""+" ".join([str(x)+","+str(y) for x,y in points])+"\" style=\"stroke:#000000; fill: #FFFFFF\"/>"

def line(points):
    (x1,y1),(x2,y2)=points
    return "<line x1=\""+str(x1)+"\"  y1=\""+str(y1)+"\" x2=\""+str(x2)+"\"   y2=\""+str(y2)+"\" style=\"stroke:#000000;\"/>"

def downarrow(x,y,l,h,a):
    deltaX=h*math.cos(math.pi*(a/float(180)))
    deltaY=h*math.sin(math.pi*(a/float(180)))
    return line([(x,y),(x,y+l)])+"\n"+line([(x,y+l),(x-deltaX,y+l-deltaY)])+"\n"+line([(x,y+l),(x+deltaX,y+l-deltaY)])

def multiline(points):
    xml=""
    for i in range(len(points)-1):
        xml=xml+line([points[i],points[i+1]])+"\n"
    return xml

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
    
def merge(outfilename):
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

def table4(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
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
    
    outfile.write("</svg>")
    outfile.close()

def table5(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    outfile.write(polyline([(10,45),(10,10),(125,10),(125,115),(10,115),(10,45),(125,45)])+"\n")
    outfile.write(polyline([(50,10),(50,115)])+"\n")
    outfile.write(polyline([(90,10),(90,115)])+"\n")

    outfile.write(text("A",15,35)+"\n")
    outfile.write(text("B",55,35)+"\n")
    outfile.write(text("C",95,35)+"\n")

    outfile.write(text("1",15,70)+"\n")
    outfile.write(text("2",55,70)+"\n")
    outfile.write(text("3",95,70)+"\n")
    outfile.write(text("4",15,105)+"\n")
    outfile.write(text("5",55,105)+"\n")
    outfile.write(text("6",95,105)+"\n")
    
    outfile.write("</svg>")
    outfile.close()
    
if __name__=="__main__":
    svgpath = sys.argv[0][:sys.argv[0].rfind("\\")]+"\\_images\\"
    pngpath = sys.argv[0][:sys.argv[0].rfind("\\")]+"\\_images\\toolbox\\"

##    svgname=svgpath+"csv.svg"
##    pngname=pngpath+"csv.png"
##    csv(svgname)
##    pngrender(svgname,pngname)
##
##    svgname=svgpath+"tsv.svg"
##    pngname=pngpath+"tsv.png"
##    tsv(svgname)
##    pngrender(svgname,pngname)
##
##    svgname=svgpath+"dbf.svg"
##    pngname=pngpath+"dbf.png"
##    dbf(svgname)
##    pngrender(svgname,pngname)
##
##    svgname=svgpath+"dat.svg"
##    pngname=pngpath+"dat.png"
##    dat(svgname)
##    pngrender(svgname,pngname)
##
##    svgname=svgpath+"table1.svg"
##    pngname=pngpath+"table1.png"
##    table1(svgname)
##    pngrender(svgname,pngname)
##
##    svgname=svgpath+"table2.svg"
##    pngname=pngpath+"table2.png"
##    table2(svgname)
##    pngrender(svgname,pngname)
##
##    svgname=svgpath+"table3.svg"
##    pngname=pngpath+"table3.png"
##    table3(svgname)
##    pngrender(svgname,pngname)
##
##    svgname=svgpath+"table4.svg"
##    pngname=pngpath+"table4.png"
##    table4(svgname)
##    pngrender(svgname,pngname)
##
    svgname=svgpath+"merge.svg"
    pngname=pngpath+"merge.png"
    merge(svgname)
    pngrender(svgname,pngname)
 