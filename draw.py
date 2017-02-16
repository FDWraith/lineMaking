from display import *

def draw_line( screen, x0, y0, x1, y1, color):
    
    A = y1 - y0
    B = x0 - x1

    if( x0 > x1 ):
        draw_line( screen, x1, y1, x0, y0, color)
        return 0
    
    x = x0
    y = y0

    if ( A >= 0 ):
        if ( -B >= A):
            #Octant 1
            d = 2*A + B
            A = 2*A
            B = 2*B
            #print("Octant 1")
            while x < x1:
                #print( "plotting at (%d, %d)"%(x,y))
                plot( screen, color, x, y)
                if ( d > 0 ):
                    y += 1
                    d += B
                x += 1
                d += A
        else:
            #Octant 2
            d = A + 2*B
            A = 2*A
            B = 2*B
            #print("Octant 2")
            while y < y1:
                #print( "plotting at (%d, %d)"%(x,y))
                plot( screen, color, x, y)
                if ( d < 0 ):
                    x += 1
                    d += A
                y += 1
                d += B
    else:
        if( B <= A):
            #Octant 8
            d = 2*A - B
            A = 2*A
            B = 2*B
            #print("Octant 8")
            while x < x1:
                #print( "plotting at (%d, %d)"%(x,y))
                plot( screen, color, x, y)
                if ( d < 0 ):
                    y -= 1
                    d -= B
                x += 1
                d += A
        else:
            #Octant 7
            d = A - 2*B
            A = 2*A
            B = 2*B
            #print("Octant 7")
            while y > y1:
                plot( screen, color, x, y)
                if( d > 0):
                    x += 1
                    d += A
                y -= 1
                d -= B
