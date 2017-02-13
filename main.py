from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 255 ]

colorRange = [ 10, 70, 150, 230 ]

x = 500
y = 0

for color1 in colorRange:
    for color2 in colorRange:
        for color3 in colorRange:
            color[RED] = color1
            color[BLUE] = color2
            color[GREEN] = color3
            
            draw_line(screen, 0, 0, x, y, color )
            y += 30


#draw_line(screen, 0, 500, 500, 250, color )

#draw_line(screen, 0, 250, 500, 250, color)
#draw_line(screen, 120, 250, 140, 170, color)
#draw_line(screen, 140, 170, 160, 340, color )

display(screen)
save_extension(screen, 'img.png')

