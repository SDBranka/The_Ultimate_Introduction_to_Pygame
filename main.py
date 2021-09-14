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

# Setting up game states
game_active = True




# create a surface with a plain color
# ts_width = 100
# ts_height = 200
# test_surface = pygame.Surface((ts_width, ts_height))
# test_surface.fill('Red')

# create a surface with an image
sky_surface = pygame.image.load('img/Sky.png').convert()

# create a ground surface with an image
ground_surface = pygame.image.load('img/ground.png').convert()

# create score surface
score_surface_text = "My Game"
score_surface_anti_aliasing = False
# score_surface_color = "Black"
score_surface_color = (64, 64, 64)
score_surface = test_font.render(score_surface_text, score_surface_anti_aliasing, score_surface_color)
score_pos_x = 400
score_pos_y = 27
score_rect = score_surface.get_rect(midtop = (score_pos_x, score_pos_y))

# create snail character(surface)
snail_surface = pygame.image.load("img/snail/snail1.png").convert_alpha()
snail_pos_x = 600
snail_pos_y = 300
# create snail rectangle that is same size as snail_surface
snail_rect = snail_surface.get_rect(midbottom = (snail_pos_x, snail_pos_y))

# create player character(surface)
player_surface = pygame.image.load("img/player/player_walk_1.png").convert_alpha()
player_pos_x = 80
player_pos_y = 300
# create player rectangle that is same size as player_surface
player_rect = player_surface.get_rect(midbottom = (player_pos_x, player_pos_y))
# create gravity physics for player
player_gravity = 0











# game loop
while True:
    for event in pygame.event.get():
        if game_active:
            # if user clicks the window close button
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # if the mouse moves the terminal will output the mouse position 
            # if event.type == pygame.MOUSEMOTION:
            #     print(event.pos)
            # if mouse button is depressed print "mouse down"
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     print("mouse down")
            # if mouse button is not depressed print "mouse up"
            # if event.type == pygame.MOUSEBUTTONUP:
            #     print("mouse up")
            # check to see if mouse is over player_rect
            # if event.type == pygame.MOUSEMOTION:
                # print(event.pos)
                # if player_rect.collidepoint(event.pos):
                #     print("collision")
            # learning KEYUP and KEYDOWN
            # if event.type == pygame.KEYDOWN:
            #     print("Key down")
            # if event.type == pygame.KEYUP:
            #     print("Key up")
            # check for a specific key press
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         print("jump")
            
            # make player jump using space bar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

            # make player jump if player is clicked (1:43:15)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800


    if game_active:
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

        # adding a background to the score_surface
        surface_to_draw_score_on = screen
        # score_bg_color = "Pink"
        score_bg_color = "#c0e8ec"
        rect_to_draw = score_rect
        pygame.draw.rect(surface_to_draw_score_on, score_bg_color, rect_to_draw)
        pygame.draw.rect(surface_to_draw_score_on, score_bg_color, rect_to_draw, 10)

        # display score_surface
        screen.blit(score_surface, score_rect)

        # display snail/move position
        snail_rect.left -= 3
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        # apply player gravity physics
        player_gravity +=1 
        player_rect.y += player_gravity
        # create floor as barrier
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        # display player
        screen.blit(player_surface, player_rect)

        # stores pressed keys into variable like a dictionary, if space bar is pushed print jump
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("jump")


        # check if player_rect() has collided with snail_rect
        # player_rect.colliderect(snail_rect) generates a number value either 1 or 0 which may be used as a Boolean check
        # print(player_rect.colliderect(snail_rect))
        # if player_rect.colliderect(snail_rect):
            # print("collision")

        # determines mouse position, if mouse collides with player_rect the terminal will output which buttons on the mouse are being pressed
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
            # print(pygame.mouse.get_pressed())

        # draw a line from the top left corner to the bottom right corner
        # surface_to_draw_line_on = screen
        # line_color = "Gold"
        # line_start_point = (0,0)
        # line_end_point = (800, 400)
        # line_width = 10
        # pygame.draw.line(surface_to_draw_line_on, line_color, line_start_point, line_end_point, line_width)

        # draw a line from top left corner to the mouse position
        # surface_to_draw_line_on = screen
        # line_color = "Gold"
        # line_start_point = (0,0)
        # line_end_point = pygame.mouse.get_pos()
        # line_width = 10
        # pygame.draw.line(surface_to_draw_line_on, line_color, line_start_point, line_end_point, line_width)

        # draw ellipse while designing our own rect
        # surface_to_ellipse_line_on = screen
        # ellipse_color = "Brown"
        # ellipse_x = 50
        # ellipse_y = 200
        # ellipse_width = 100
        # ellipse_height = 100
        # pygame.draw.ellipse(surface_to_ellipse_line_on, ellipse_color, pygame.Rect(ellipse_x, ellipse_y, ellipse_width, ellipse_height))

        # player vs snail collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("Yellow")


    pygame.display.update()
    # sets so that while True loop should not run faster than framerate_ceiling times per second
    framerate_ceiling = 60
    clock.tick(framerate_ceiling)












