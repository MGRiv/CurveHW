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
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        else:
            c += 1
            if(l[c - 1] == "line"):
                add_edge(points,int(l[c][0]),int(l[c][1]),int(l[c][2]),int(l[c][3]),int(l[c][4]),int(l[c][5]))
            elif(l[c - 1] == "circle"):
                add_cirlce(points,int(l[c][0]),int(l[c][1]),0,,int(l[c][2]),0.02)
            elif(l[c - 1] == "hermite"):
                add_curve(points,int(l[c][0]),int(l[c][1]),int(l[c][2]),int(l[c][3]),int(l[c][4]),int(l[c][5]),int(l[c][6]),int(l[c][7]),0.02,0)
            elif(l[c - 1] == "bezier"):
                add_curve(points,int(l[c][0]),int(l[c][1]),int(l[c][2]),int(l[c][3]),int(l[c][4]),int(l[c][5]),int(l[c][6]),int(l[c][7]),0.02,1)
            elif(l[c - 1] == "scale"):
                t = make_scale(int(l[c][0]),int(l[c][1]),int(l[c][2]))
                matrix_mult(t,transform)
            elif(l[c - 1] == "translate"):
                t = make_translate(int(l[c][0]),int(l[c][1]),int(l[c][2]))
                matrix_mult(t,transform)
            elif(l[c - 1] == "xrotate"):
                t = make_rotX(int(l[c][0]))
                matrix_mult(t,transform)
            elif(l[c - 1] == "yrotate"):
                t = make_rotY(int(l[c][0]))
                matrix_mult(t,transform)
            elif(l[c - 1] == "zrotate"):
                t = make_rotZ(int(l[c][0]))
                matrix_mult(t,transform)
            elif(l[c - 1] == "save"):
                save_ppm(screen,l[c][0])
                
                

##draw_line(screen,int((int(l[c][0]) - int(l[c][2])) * math.sqrt(3)/2),int(int(l[c][1]) - .5 * (int(l[c][0]) + int(l[c][2]))),int((int(l[c][3]) - int(l[c][5])) * math.sqrt(3)/2),int(int(l[c][4]) - .5 * (int(l[c][3]) + int(l[c][5]))),color)
