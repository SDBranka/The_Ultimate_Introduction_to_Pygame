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

# create a surface with a plain color
ts_width = 100
ts_height = 200
test_surface = pygame.Surface((ts_width, ts_height))
test_surface.fill('Red')


# game loop
while True:
    for event in pygame.event.get():
        # if user clicks the window close button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # display test_surface
    ts_pos_x = 0
    ts_pos_y = 0
    screen.blit(test_surface, (ts_pos_x, ts_pos_y))

    pygame.display.update()
    # sets so that while True loop should not run faster than framerate_ceiling times per second
    framerate_ceiling = 60
    clock.tick(framerate_ceiling)












