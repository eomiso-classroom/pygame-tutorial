import pygame as pg
### TODO: Add random module


pg.init()
screen = pg.display.set_mode((600, 600))

# Creating image object
background_img = pg.image.load("background.png")

rock = pg.image.load("rock.png")
rock = pg.transform.scale(rock, (150, 150))

scissors = pg.image.load("scissors.png")
scissors = pg.transform.scale(scissors, (150, 150))

paper = pg.image.load("paper.png")
paper = pg.transform.scale(paper, (150, 150))

click = pg.image.load("click_here.png")
click = pg.transform.scale(click, (150,100))

# Drawing the images on the screen
screen.blit(background_img, background_img.get_rect())
scissors_pos = screen.blit(scissors, (50, 100))
rock_pos = screen.blit(rock, (200, 100))
paper_pos = screen.blit(paper, (350, 100))
click_pos = screen.blit(click, (400, 0))

RSP = [rok ,scissors, paper]

# TODO: Use the RSP list to get a random entry
random_computer = None

running = True
while running:
    
    # Receiving event
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if click_pos.collidepoint(pg.mouse.get_pos()):
                
                # TODO: Print out the the hand of the computer
                
                
    pg.display.update()
