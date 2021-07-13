import pygame
import gym 

pygame.init()
clock = pygame.time.Clock()
fps = 20  # frames per second

screen_size = (600, 400)
screen = pygame.display.set_mode(screen_size)

LEFT = 0
RIGHT = 1
key_action = {LEFT: 'left', RIGHT: 'right'}
action = LEFT # simple initialization

count = 0
done = False
while (done == False) and (count < 100):
    # main pygame event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            done = True

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            action = LEFT
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            action = RIGHT
    #

    print(count, 'key: ', key_action[action])
    clock.tick(fps) 
    count += 1