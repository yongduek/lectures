import pygame as pg 
import numpy as np 
WIDTH, HEIGHT = 1000, 800

GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Block(pg.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        
        self.image.fill((250, 250, 100))
        
        self.dx = np.random.randint(-5, 5)
        self.dy = np.random.randint(-5, 5)
        
        # second image
        self.image2 = pg.Surface((width//2, height//2))
        self.rect2 = self.image2.get_rect()
        self.image2.fill(BLUE)
        self.dx2 = np.random.randint(-5, 5)
        self.dy2 = np.random.randint(-5, 5)
        
    def update(self):
        self.rect.x += self.dx 
        self.rect.y += self.dy 
        
        if self.rect.x < 0: 
            self.dx *= -1
        elif self.rect.x > WIDTH:
            self.dx *= -1
        if self.rect.y < 0 or self.rect.y > HEIGHT:
            self.dy *= -1 
        
        # second rectangle
        self.rect2.x += self.dx2
        # self.rect2.y += self.dy2 
        if self.rect2.left < 0:
            self.rect2.left = 0
            self.dx2 *= -1 
        if self.rect2.right > self.rect.width:
            self.rect2.right = self.rect.width
            self.dx2 *= -1 
        
        #
        self.image.fill(YELLOW)
        self.image.blit(self.image2, self.rect2)

def main():
    
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    
    allSprites = pg.sprite.Group()
    block = Block(200, 100)
    allSprites.add(block)
        
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                
        
        allSprites.update()
        
        screen.fill (GRAY)
        allSprites.draw(screen)
        
        pg.display.flip()
        clock.tick(60)
        
    pg.quit()
#

if __name__ == "__main__":
    main()