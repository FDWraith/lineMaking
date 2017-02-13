from display import *

'''
##Octant 1 
def draw_line( screen, x0, y0, x1, y1, color ):

    A = y1 - y0
    B = x0 - x1

    x = x0
    y = y0

    d = 2*A + B
    A = 2*A
    B = 2*B

    while x < x1:
        #print( "plotting at (%d, %d)"%(x,y))
        plot( screen, color, x, y)
        if ( d > 0 ):
            y+=1
            d+=B
        x+=1
        d+=A
'''

'''
##Octant 2
def draw_line( screen, x0, y0, x1, y1, color ):

    A = y1 - y0
    B = x0 - x1

    x = x0
    y = y0

    d = 2*A + B
    A = 2*A
    B = 2*B

    while y < y1:
        #print( "plotting at (%d, %d)"%(x,y))
        plot( screen, color, x, y)
        if ( d < 0 ):
            x+=1
            d+=A
        y+=1
        d+=B 

'''

'''
##Octant 8
def draw_line( screen, x0, y0, x1, y1, color ):

    A = y1 - y0
    B = x0 - x1

    x = x0
    y = y0

    d = 2*A + B
    A = 2*A
    B = 2*B

    while x < x1:
        #print( "plotting at (%d, %d)"%(x,y))
        plot( screen, color, x, y)
        if ( d > 0 ):
            y-=1
            d+=B
        x+=1
        d-=A 
'''

def draw_line( screen, x0, y0, x1, y1, color):
    
    A = y1 - y0
    B = x0 - x1

    x = x0
    y = y0

    d = 2*A + B
    A = 2*A
    B = 2*B

    m = ( A / -B)
    if ( m >= 0 ):
        if ( m <= 1):
            while x < x1:
                #print( "plotting at (%d, %d)"%(x,y))
                plot( screen, color, x, y)
                if ( d > 0 ):
                    y += 1
                    d += B
                x += 1
                d += A
        else:
            while y < y1:
                #print( "plotting at (%d, %d)"%(x,y))
                plot( screen, color, x, y)
                if ( d < 0 ):
                    x+=1
                    d+=A
                y+=1
                d+=B
    else:
        if( m >= -1):
            while x < x1:
                #print( "plotting at (%d, %d)"%(x,y))
                plot( screen, color, x, y)
                if ( d > 0 ):
                    y-=1
                    d+=B
                x+=1
                d-=A
        else:
            while y < y1:
                plot( screen, color, x, y)
                if( d < 0):
                    x += 1
                    d -= A
                y -= 1
                d += B
