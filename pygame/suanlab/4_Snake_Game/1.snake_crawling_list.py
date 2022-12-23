"""
 Simple snake example with a list of segments
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import numpy as np  
 
# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3
 
# Set initial speed
x_change = segment_width + segment_margin
y_change = 0
 
 
# class Segment(pygame.sprite.Sprite):  # this may be a Sprite.

class Segment():  # this may be a Sprite.
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.color = tuple([np.random.randint(0,255) for _ in range(3)])  # used only once; doesn't have to be a self-variable.
        # print('color: ', self.color)
        self.image.fill(self.color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Snake Example with List of Segments')
 
# Create an initial snake
# allspriteslist = pygame.sprite.Group()
#
snake_segments = []
for i in range(15):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    # allspriteslist.add(segment)

 
clock = pygame.time.Clock()
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)
 
    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    # allspriteslist.remove(old_segment)

    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)
 
    # Insert new segment into the list
    snake_segments.insert(0, segment)
    # allspriteslist.add(segment)
 
    # -- Draw everything
    # Clear screen
    screen.fill((128, 128, 128))

    # print('old seg: ', old_segment.rect.x, old_segment.rect.y)
    pygame.draw.circle(screen, (255, 0, 0), (old_segment.rect.x, old_segment.rect.y), segment_height/2, 3)

    # allspriteslist.draw(screen)
    for seg in snake_segments:
        screen.blit(seg.image, seg.rect)
        
 
    # Flip screen
    pygame.display.flip()
 
    # Pause
    clock.tick(5)
 
pygame.quit()
