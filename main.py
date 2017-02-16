from display import *
from draw import *

screen = new_screen()
color = [ 0, 0, 0 ]

'''
draw_line(screen, 0, 0, 250, 500, color )
draw_line(screen, 250, 500, 500, 0, color)
draw_line(screen, 500, 0, 0, 250, color)
draw_line(screen, 0, 250, 500, 500, color)
draw_line(screen, 500, 500, 250, 0, color)
draw_line(screen, 250, 0, 0, 500, color)
draw_line(screen, 0, 500, 500, 250, color)
draw_line(screen, 500, 250, 0, 0, color)

draw_line(screen, 0, 0, 500, 500, color)
draw_line(screen, 0, 500, 500, 0, color)
draw_line(screen, 250, 0, 250, 500, color)
draw_line(screen, 0, 250, 500, 250, color)

'''

color[RED] = 255
for y0 in range(250) :
    if y0 % 10 == 0:
        color[BLUE] = y0 / 2
        draw_line(screen, 0, y0 * 2, 500, 500 - y0 * 2, color)

color[BLUE] = 0
for x0 in range(500):
    if x0 % 20 == 0:
        color[GREEN] = x0 / 2
        draw_line( screen, x0, 0, 500-x0, 500, color)

#draw_line(screen, 0, 250, 500, 250, color)
#draw_line(screen, 120, 250, 140, 170, color)
#draw_line(screen, 140, 170, 160, 340, color )

display(screen)
save_extension(screen, 'img.png')

