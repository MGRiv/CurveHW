from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    x0 = cx + r
    y0 = cy
    t = 0
    while(t <= 1):
        x1 = cx + r * math.cos(2 * math.pi * t)
        y1 = cy + r * math.sin(2 * math.pi * t)
        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        t += step
    add_edge(points,cx + r, cy,cz, x0, y0,cz)
    

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    m = []
    dx = 0
    dy = 0
    if curve_type == 0:
        m = [[x0, x2, x1 - x0, x3 - x2], [y0, y2, y1 - y0, y3 - y2]]
        matrix_mult([[2, -3, 0, 1], [-2, 3, 0, 0], [1, -2, 1, 0], [1, -1, 0, 0]], m)
        dx = x2
        dy = y2
    else:
        m = [[x0, x1, x2, x3], [y0, y1, y2, y3]]
        matrix_mult([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]], m)
        dx = x3
        dy = y3
    xp = x0
    yp = y0
    t = 0
    while(t <= 1):
        add_point(points,xp,yp,0)
        xp = t * ( t * ( (m[0][0] * t) + m[0][1]) + m[0][2]) + m[0][3]
        yp = t * ( t * ( (m[1][0] * t) + m[1][1]) + m[1][2]) + m[1][3]
        add_point(points,xp,yp,0)
        t += step
    add_edge(points,xp,yp,0,dx,dy,0)
        
        

def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
    l = len(matrix)
    c = 0
    while(l - c > 1):
        p = matrix[c]
        e = matrix[c + 1]
        draw_line(screen,int(p[0]),int(p[1]),int(e[0]),int(e[1]),color)
        c += 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

