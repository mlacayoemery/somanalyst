import os, sys, subprocess

def text(string="Example SVG text 1",x=20,y=40):
    return "<text x=\""+str(x)+"\" y=\""+str(y)+"\" style=\"font-family: Courier; font-size: 34; stroke: #000000; fill : #000000;\">"+string+"</text>"

def rectangle(x=10,y=10,height=100,width=100,stroke="000000",fill="FFFFFF"):
    return "<rect x=\""+str(x)+"\" y=\""+str(y)+"\" height=\""+str(height)+"\" width=\""+str(width)+"\" style=\"stroke:#"+stroke+"; fill: #"+fill+"\"/>"


path = sys.argv[0][:sys.argv[0].rfind("\\")]+"\\_images\\"
cmd = "E:/InkscapePortable/App/Inkscape/inkscape.exe --export-area-drawing --export-png="

fname="csv.svg"
outfile = open(path+fname,'w')
outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
outfile.write(rectangle(10,10,35,115)+"\n")
outfile.write(rectangle(10,45,70,115)+"\n")
outfile.write(text("*.csv",15,35)+"\n")
outfile.write(text("A,B,C",15,70)+"\n")
outfile.write(text("1,2,3",15,105)+"\n")
outfile.write("</svg>")
outfile.close()
subprocess.Popen(cmd+path+"toolbox/"+fname.split(".")[0]+".png "+path+fname, shell=True)

fname="tsv.svg"
outfile = open(path+fname,'w')
outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
outfile.write(rectangle(10,10,35,115)+"\n")
outfile.write(rectangle(10,45,70,115)+"\n")
outfile.write(text("*.tsv",15,35)+"\n")
outfile.write(text("A B C",15,70)+"\n")
outfile.write(text("1 2 3",15,105)+"\n")
outfile.write("</svg>")
outfile.close()
subprocess.Popen(cmd+path+"toolbox/"+fname.split(".")[0]+".png "+path+fname, shell=True)

fname="dbf.svg"
outfile = open(path+fname,'w')
outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
outfile.write(rectangle(10,10,30,175)+"\n")
outfile.write(rectangle(10,40,65,175)+"\n")
outfile.write(text("*.dbf",45,35)+"\n")
outfile.write(text("01001100",15,65)+"\n")
outfile.write(text("ABC123",15,95)+"\n")
outfile.write("</svg>")
outfile.close()
subprocess.Popen(cmd+path+"toolbox/"+fname.split(".")[0]+".png "+path+fname, shell=True)

fname="dat.svg"
outfile = open(path+fname,'w')
outfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
outfile.write(rectangle(10,10,30,175)+"\n")
outfile.write(rectangle(10,40,95,175)+"\n")
outfile.write(text("*.dat",45,35)+"\n")
outfile.write(text("3",15,65)+"\n")
outfile.write(text("#n A B C",15,95)+"\n")
outfile.write(text("1 2 3",15,125)+"\n")
outfile.write("</svg>")
outfile.close()
subprocess.Popen(cmd+path+"toolbox/"+fname.split(".")[0]+".png "+path+fname, shell=True)