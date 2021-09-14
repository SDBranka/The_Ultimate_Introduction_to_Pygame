import pygame
from sys import exit

# initialize pygame
pygame.init()

# setup display surface
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
# rename screen title
pygame.display.set_caption('Runner')

# controlling the framerate
clock = pygame.time.Clock()

# creating a font
# font_type = None
font_type = "font/Pixeltype.ttf"
font_size = 50
test_font = pygame.font.Font(font_type, font_size)

# create a surface with a plain color
# ts_width = 100
# ts_height = 200
# test_surface = pygame.Surface((ts_width, ts_height))
# test_surface.fill('Red')

# create a surface with an image
sky_surface = pygame.image.load('img/Sky.png').convert()

# create a ground surface with an image
ground_surface = pygame.image.load('img/ground.png').convert()

# create text surface
text_surface_text = "My Game"
text_surface_anti_aliasing = False
text_surface_color = "Black"
text_surface = test_font.render(text_surface_text, text_surface_anti_aliasing, text_surface_color)

# create snail character(surface)
snail_surface = pygame.image.load("img/snail/snail1.png").convert_alpha()
snail_pos_x = 600
snail_pos_y = 250


# game loop
while True:
    for event in pygame.event.get():
        # if user clicks the window close button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # display test_surface
    # ts_pos_x = 200
    # ts_pos_y = 100
    # screen.blit(test_surface, (ts_pos_x, ts_pos_y))

    # display sky_surface
    sky_pos_x = 0
    sky_pos_y = 0
    screen.blit(sky_surface, (sky_pos_x, sky_pos_y))

    # display ground_surface
    ground_pos_x = 0
    ground_pos_y = 300
    screen.blit(ground_surface, (ground_pos_x, ground_pos_y))

    # display text_surface
    text_pos_x = 300
    text_pos_y = 50
    screen.blit(text_surface, (text_pos_x, text_pos_y))

    # display snail/move position
    snail_pos_x -= 3
    if snail_pos_x < -90:
        snail_pos_x = 800
    screen.blit(snail_surface, (snail_pos_x, snail_pos_y))


    pygame.display.update()
    # sets so that while True loop should not run faster than framerate_ceiling times per second
    framerate_ceiling = 60
    clock.tick(framerate_ceiling)












