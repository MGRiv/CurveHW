from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r')
    r = f.read()
    l = r.split('\n')
    c = 0
    while(c < len(l)):
        if(l[c] == "ident"):
            ident(transform)
        elif(l[c] == "apply"):
            matrix_mult(transform,points)
        elif(l[c] == "display"):
            display(screen)
        else:
            c += 1
            if(l[c - 1] == "line"):
                add_edge(points,int(l[c][0]),int(l[c][1]),int(l[c][2]),int(l[c][3]),int(l[c][4]),int(l[c][5]))
            elif(l[c - 1] == "circle"):
                add_cirlce(points,int(l[c][0]),int(l[c][1]),0,,int(l[c][2]),0.02)
            elif(l[c - 1] == "hermite"):
                add_curve(points,


##draw_line(screen,int((int(l[c][0]) - int(l[c][2])) * math.sqrt(3)/2),int(int(l[c][1]) - .5 * (int(l[c][0]) + int(l[c][2]))),int((int(l[c][3]) - int(l[c][5])) * math.sqrt(3)/2),int(int(l[c][4]) - .5 * (int(l[c][3]) + int(l[c][5]))),color)
