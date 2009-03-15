import math

def vrmlWrite(points,polygons):
    world=open("G:/arcSOM/world.wrl",'w')

    world.write("#VRML V2.0 utf8\n")
    world.write("\n")
    world.write("Shape {\n")
    world.write("geometry IndexedFaceSet {\n")
    world.write("solid TRUE\n")
    world.write("coord Coordinate {\n")

    #write points X Y Z,
    world.write("point [\n")
    for p in points:
        world.write(p[0]+" "+p[1]+" "+p[2]+",\n")
    world.write("]\n")
    world.write("}\n")

    #write faces A, B, C, -1,
    world.write("coordIndex [\n")
    for p in map(str,polygons):
        world.write(p+", ")
    world.write("\n")
    world.write("]\n")
    world.write("colorPerVertex FALSE\n")

    #define colors R G B
    world.write("color Color {\n")
    world.write("color [\n")
    world.write("1 1 0\n")
    world.write("1 0 0\n")
    world.write("0 1 0\n")
    world.write("0 0 1\n")
    world.write("]\n")
    world.write("}\n")

    #index of color for each face N N N
    world.write("colorIndex [\n")
    world.write("0 1 2 3")
    world.write("]\n")
    world.write("}\n")
    world.write("}\n")
    
    world.close()

def radXtoDeg(x):
    if x<1:
        return 180*x
    else:
        return -180*(2-x)

def radYtoDeg(y):
    if y<float(1)/2:
        print "here"
        return -180*y
    elif y<1:
        return -180*(1-y)
    elif y<float(3)/2:
        return 180*(y-1)
    else:
        return 180*(2-y)

def radsToDeg(xy):
    return [radXtoDeg(xy[0]),radYtoDeg(xy[0])]

def polarToRect(xy):
    return map(str,[math.cos(math.radians(xy[0]))*math.cos(math.radians(xy[1])),
            math.cos(math.radians(xy[0]))*math.sin(math.radians(xy[1])),
            math.sin(math.radians(xy[0]))])

#north pole
A=[0,float(3)/2]
#south of A along prime meridian
B=[0,float(1)/6]
#east of B
C=[float(2)/3,float(1)/6]
#east of C
D=[float(4)/3,float(1)/6]

points=map(polarToRect,map(radsToDeg,[A,B,C,D]))
polygons=[0,1,2,-1,0,2,3,-1,0,3,1,-1,1,2,3,-1]

vrmlWrite(points,polygons)


print math.cos(math.radians(0))*math.cos(math.radians(90)),
print math.cos(math.radians(0))*math.sin(math.radians(90)),
print math.sin(math.radians(0))