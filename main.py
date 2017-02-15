from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 255 ]

draw_line(screen, 0, 0, 250, 500, color )
draw_line(screen, 250, 500, 500, 0, color)
draw_line(screen, 500, 0, 0, 250, color)
draw_line(screen, 0, 250, 500, 500, color)
draw_line(screen, 500, 500, 250, 0, color)
draw_line(screen, 250, 0, 0, 500, color)
draw_line(screen, 0, 500, 500, 250, color)
draw_line(screen, 500, 250, 0, 0, color)


#draw_line(screen, 0, 250, 500, 250, color)
#draw_line(screen, 120, 250, 140, 170, color)
#draw_line(screen, 140, 170, 160, 340, color )

display(screen)
save_extension(screen, 'img.png')

