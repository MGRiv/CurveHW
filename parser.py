from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r')
    r = f.read()
    l = r.split('\n')
    c = 0
    while(c < len(l)):
        print str(c + 1) +"\n"
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
            t = l[c].split(' ')
            if(l[c - 1] == "line"):
                add_edge(points,int(t[0]),int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]))
            elif(l[c - 1] == "circle"):
                add_circle(points,int(t[0]),int(t[1]),0,int(t[2]),0.02)
            elif(l[c - 1] == "hermite"):
                add_curve(points,int(t[0]),int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]),int(t[6]),int(t[7]),0.02,0)
            elif(l[c - 1] == "bezier"):
                add_curve(points,int(t[0]),int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]),int(t[6]),int(t[7]),0.02,1)
            elif(l[c - 1] == "scale"):
                q = make_scale(float(t[0]),float(t[1]),float(t[2]))
                matrix_mult(q,transform)
            elif(l[c - 1] == "translate"):
                q = make_translate(int(t[0]),int(t[1]),int(t[2]))
                matrix_mult(q,transform)
            elif(l[c - 1] == "xrotate"):
                q = make_rotX(float(t[0]))
                matrix_mult(q,transform)
            elif(l[c - 1] == "yrotate"):
                q = make_rotY(float(t[0]))
                matrix_mult(q,transform)
            elif(l[c - 1] == "zrotate"):
                q = make_rotZ(float(t[0]))
                matrix_mult(q,transform)
            elif(l[c - 1] == "save"):
                save_ppm(screen,t[0])
        c+=1
    f.close()    
                



