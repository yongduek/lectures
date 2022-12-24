import os 
import pygame 
import numpy as np

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
PINK  = (255, 190, 200)

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1200

class ImageBlock:
    def __init__(self, image, x=100, y=100, sound=None):
        self.image = image 
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        self.vel = np.random.uniform(-7, 8, size=2)
        self.pos = np.array([x, y])
        self.pos = np.random.uniform(0, WINDOW_HEIGHT*2/3, size=2)
        self.angle = np.random.randint(-360, 360) # rotational motion
        self.avel = np.random.uniform(-5, 5)
        self.sound = sound
        
    def update(self):
        self.pos = self.pos + self.vel 
        
        bounce = False 
        if self.pos[0] < 0 or self.pos[0] + self.width > WINDOW_WIDTH:
            self.vel[0] *= -1
            bounce = True
        if self.pos[1] < 0 or self.pos[1] + self.height > WINDOW_HEIGHT:
            self.vel[1] *= -1
            bounce = True
        
        if bounce and self.sound:
            self.sound.play()
            
        self.angle = self.angle + self.avel
        if self.angle > 360:
            self.angle -= 360
        if self.angle < -360:
            self.angle += 360
            
    def draw(self, screen):            
        # print('draw: ', self.pos[0], self.pos[1])
        screen.blit(self.image, [self.pos[0], self.pos[1]]) #, self.width, self.height])
        # screen.blit(self.image, self.pos)
        rect = self.image.get_rect()
        rect.x = self.pos[0]
        rect.y = self.pos[1]
        pygame.draw.rect(screen, RED, rect, 5)

        im_rotated = pygame.transform.rotate(self.image, self.angle)
        if 0:  # draw without position correction
            rect2 = im_rotated.get_rect()
            rect2.x = self.pos[0]
            rect2.y = self.pos[1]
            pygame.draw.rect(screen, PINK, rect2, 5)
            screen.blit(im_rotated, rect2)

        if 1:  # with position correction
            old_center = np.array([self.width/2, self.height/2])
            new_center = [im_rotated.get_width()/2, im_rotated.get_height()/2]
            rot_pos = self.pos - (new_center - old_center)
            screen.blit(im_rotated, rot_pos)
            pygame.draw.rect(screen, BLACK, [rot_pos[0], rot_pos[1], im_rotated.get_width(), im_rotated.get_height()], 1)
#

def getLRTB(a: ImageBlock):
    l = a.pos[0]
    r = a.pos[0] + a.width
    t = a.pos[1]
    b = a.pos[1] + a.height
    return l,r,t,b
    
def collision2Blocks(a : ImageBlock, b: ImageBlock) -> bool :
    # AABB collision 
    al, ar, at, ab = getLRTB(a)
    bl, br, bt, bb = getLRTB(b)
    
    xoverlap = al < br and bl < ar 
    yoverlap = at < bb and bt < at 
    
    if xoverlap and yoverlap:
        return True 
    else: 
        return False

def loadImageFiles(dirname):
    print('cwd:', os.getcwd())
    print('full path:', os.path.abspath("."))
    imagelist = []
    for fn in os.listdir(dirname):
        if fn[-3:] not in ["png", "bmp", "gif"]: continue
        ifname = os.path.join(dirname, fn)
        print(fn, ifname)
        im = pygame.image.load(ifname)
        imagelist.append(im)
    return imagelist

def loadSoundFiles(dirname):
    print('cwd:', os.getcwd())
    print('full path:', os.path.abspath("."))
    sndlist = []
    for fn in os.listdir(dirname):
        if fn[-3:] not in ["mp3", "wav", "ogg"]: continue
        fname = os.path.join(dirname, fn)
        print(fn, fname)
        snd = pygame.mixer.Sound(fname)
        sndlist.append(snd)
    return sndlist
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    
    imageList = loadImageFiles ("./assets")
    print('imageList:', imageList)
    
    soundList = loadSoundFiles("./assets")
    
    imageBlockList = []
    for i in range(12):
        img = np.random.choice(imageList)
        snd = np.random.choice(soundList)
        imblk = ImageBlock(img, sound=snd)
        imageBlockList.append(imblk)
    #
    
    # keyboard control
    keyboard_dx, keyboard_dy = 0, 0
    
    done = False
    while not done:
        # 1. event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keyboard_dx = -3
                elif event.key == pygame.K_RIGHT:
                    keyboard_dx = 3
                elif event.key == pygame.K_UP:
                    keyboard_dy = -3
                elif event.key == pygame.K_DOWN:
                    keyboard_dy = 3
                elif event.key == pygame.K_ESCAPE:
                    done = True 
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    keyboard_dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    keyboard_dy = 0
        
        # 2. state update
        for imblk in imageBlockList:
            imblk.update()
                            
        # 3. draw
        screen.fill(WHITE)

        screen.blit(img, [200, 100])

        for imblk in imageBlockList:
            imblk.draw(screen)
            
        # 4. flip / tick
        pygame.display.flip()
        clock.tick(60)
# main()

if __name__ == "__main__":
    
    main()