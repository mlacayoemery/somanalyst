import os, sys, subprocess

def text(string="Example SVG text 1",x=20,y=40):
    return "<text x=\""+str(x)+"\" y=\""+str(y)+"\" style=\"font-family: Courier; font-size: 34; stroke: #000000; fill : #000000;\">"+string+"</text>"

def rectangle(x=10,y=10,height=100,width=100,stroke="000000",fill="FFFFFF"):
    return "<rect x=\""+str(x)+"\" y=\""+str(y)+"\" height=\""+str(height)+"\" width=\""+str(width)+"\" style=\"stroke:#"+stroke+"; fill: #"+fill+"\"/>"

def polyline(points):
    return "<polyline points=\""+" ".join([str(x)+","+str(y) for x,y in points])+"\" style=\"stroke:#000000; fill: #FFFFFF\"/>"

def line(points):
    (x1,y1),(x2,y2)=points
    return "<line x1=\""+str(x1)+"\"  y1=\""+str(y1)+"\" x2=\""+str(x2)+"\"   y2=\""+str(y2)+"\" style=\"stroke:#000000;\"/>"

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
    
def table1(outfilename):
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

    outfile.write(text(".",15,85)+"\n")
    outfile.write(text(".",55,85)+"\n")
    outfile.write(text(".",95,85)+"\n")
    outfile.write(text(".",15,95)+"\n")
    outfile.write(text(".",55,95)+"\n")
    outfile.write(text(".",95,95)+"\n")
    outfile.write(text(".",15,105)+"\n")
    outfile.write(text(".",55,105)+"\n")
    outfile.write(text(".",95,105)+"\n")
    
    outfile.write("</svg>")
    outfile.close()

def table2(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    outfile.write(polyline([(10,45),(10,10),(125,10),(125,115),(10,115),(10,45),(125,45)])+"\n")
    outfile.write(polyline([(50,10),(50,115)])+"\n")
    outfile.write(polyline([(90,10),(90,115)])+"\n")

    outfile.write(text("A",15,35)+"\n")
    outfile.write(text("B",55,35)+"\n")
    outfile.write(text("C",95,35)+"\n")

    outfile.write(text("4",15,70)+"\n")
    outfile.write(text("5",55,70)+"\n")
    outfile.write(text("6",95,70)+"\n")

    outfile.write(text(".",15,85)+"\n")
    outfile.write(text(".",55,85)+"\n")
    outfile.write(text(".",95,85)+"\n")
    outfile.write(text(".",15,95)+"\n")
    outfile.write(text(".",55,95)+"\n")
    outfile.write(text(".",95,95)+"\n")
    outfile.write(text(".",15,105)+"\n")
    outfile.write(text(".",55,105)+"\n")
    outfile.write(text(".",95,105)+"\n")
    
    outfile.write("</svg>")
    outfile.close()

def table3(outfilename):
    outfile = open(outfilename,'w')
    outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    outfile.write(polyline([(10,45),(10,10),(125,10),(125,185),(10,185),(10,45),(125,45)])+"\n")
    outfile.write(polyline([(50,10),(50,185)])+"\n")
    outfile.write(polyline([(90,10),(90,185)])+"\n")

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
    svgname=svgpath+"table5.svg"
    pngname=pngpath+"table5.png"
    table5(svgname)
    pngrender(svgname,pngname)
 