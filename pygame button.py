# This is a simple Pygame button program.

# Import and initialize the pygame library
import pygame
pygame.init()

# Set colour variables
light_grey=(200,200,200)
lightish_grey=(180,180,180)
dark_grey=(100,100,100)
darker_grey=(70,70,70)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)


# Set up the display window
screen = pygame.display.set_mode([500, 550])

# Intialise button 1 variables
x1_pos=100
y1_pos=150
rec1_colour=light_grey
button1=pygame.Rect(x1_pos,y1_pos,80,80)

# Intialise button 2 variables
x2_pos=300
y2_pos=150
rec2_colour=light_grey
button2=pygame.Rect(x2_pos,y2_pos,80,80)


running = True
click=0


while running:
    screen.fill((darker_grey))

    # When the user clicks x in the game window
    for event in pygame.event.get():
        mouse_x,mouse_y=pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running=False

        # When the user clicks on a button, animate the button and change its colour
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                rec1_colour=white
                x1_pos=x1_pos+3
                y1_pos=y1_pos+3
                button1=pygame.Rect(x1_pos,y1_pos,80,80)
            elif button2.collidepoint(event.pos):
                rec2_colour=white
                x2_pos=x2_pos+3
                y2_pos=y2_pos+3
                button2=pygame.Rect(x2_pos,y2_pos,80,80)
            

        # When the user releases the button, reset button to original colour and position
        elif event.type==pygame.MOUSEBUTTONUP:
            if button1.collidepoint(event.pos):
                rec1_colour=light_grey
                x1_pos=x1_pos-3
                y1_pos=y1_pos-3
                button1=pygame.Rect(x1_pos,y1_pos,80,80)

            if button2.collidepoint(event.pos):
                rec2_colour=light_grey
                x2_pos=x2_pos-3
                y2_pos=y2_pos-3
                button2=pygame.Rect(x2_pos,y2_pos,80,80)       

        # When the user hovers over the button, change colour
        elif button1.x<=mouse_x<=(button1.x+80) and button1.y<=mouse_y<=(button1.y+80):
            rec1_colour=lightish_grey
        elif button2.x<=mouse_x<=(button2.x+80) and button2.y<=mouse_y<=(button2.y+80):
            rec2_colour=lightish_grey        
        else:
            rec1_colour=light_grey
            rec2_colour=light_grey

        pygame.draw.rect(screen,rec1_colour,button1)
        pygame.draw.rect(screen,rec2_colour,button2)        

        pygame.display.update()



pygame.quit()
