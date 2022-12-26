import numpy as np 
import pygame
import os 
from pathlib import Path

WINDOW_WIDTH, WINDOW_HEIGHT = 1300, 800
WHITE = (255, 255, 255)


def keyboard_handling():
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True 
    return done 

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
        snd.play()
    return sndlist
    
def loadImageFiles(dirname = "./assets"):
    """ this function does ... """
    filelist = os.listdir(dirname)
    imagelist = []
    # dirname = Path(dirname)
    for f in filelist:
        ext = f[-3:]
        if ext in ["png", "bmp", "jpg"]:  # jpeg
            # load
            ff = dirname + "/" + f # directory / filename 
            ff = os.path.join(dirname, f)
            # ff = dirname / f 
            print("image load: ", f, ff)
            im = pygame.image.load(ff)
            imagelist.append(im)
    #
    return imagelist 

class ImageBlock:
    def __init__(self, image, sound=None):
        self.image = image 
        self.width = image.get_width()
        self.height = image.get_height()
        
        self.rect = image.get_rect()

        self.x, self.y = np.random.randint(0, WINDOW_WIDTH-100), np.random.randint(0, WINDOW_HEIGHT-100)
        self.dx, self.dy = np.random.randint(-10, 11), np.random.randint(-10,11)

        self.sound = sound 
        
    def update(self):
        self.x += self.dx 
        self.y += self.dy 

        flag = False 
        if self.x < 0 or self.x + self.width > WINDOW_WIDTH:
            self.dx *= -1 
            flag = True 

        if self.y < 0 or self.y + self.height > WINDOW_HEIGHT:
            self.dy *= -1
            flag = True 

        if flag:
            self.sound.play()

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

class Player:
    def __init__(self, image, sound=None):
        self.image = image 
        self.width = image.get_width()
        self.height = image.get_height()
        
        self.rect = image.get_rect()

        self.x, self.y = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
        
        self.sound = sound 
        
    def update(self):
        dx, dy = 0, 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -3
                elif event.key == pygame.K_RIGHT:
                    dx = 3
                elif event.key == pygame.K_UP:
                    dy = -3
                elif event.key == pygame.K_DOWN:
                    dy = 3
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    dy = 0
        #

        self.x += dx 
        self.y += dy 

        flag = False 
        if self.x < 0:
            self.x = 0
            flag = True 
        if self.x + self.width > WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - self.width
            flag = True 

        if self.y < 0:
            self.y  = 0
            flag = True 
        if self.y + self.height > WINDOW_HEIGHT:
            self.y = WINDOW_HEIGHT - self.height 
            flag = True 

        if flag:
            self.sound.play()

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    imageList = loadImageFiles ("./assets")
    print('imageList:', imageList)
    
    soundList = loadSoundFiles("./assets")
    

    imageBlockList = []
    for i in range(2):
        img = np.random.choice(imageList)
        indx = np.random.randint(0, len(soundList))
        snd = soundList[indx]
        imblk = ImageBlock(img, sound=snd)
        # imblk = ImageBlock(img)
        imageBlockList.append(imblk)
    #
    player = Player(img, sound=snd)
    imageBlockList.append(player)

    done = False
    while not done:
        # 1. event handling
        done = keyboard_handling()
        
        # 2. state update 
        # for i in range(len(imageBlockList)):
        #     imageBlockList[i].update()

        for ib in imageBlockList:
            ib.update()

        # 3. drawing
        screen.fill(WHITE) # clear the whole screen

        for ib in imageBlockList:
            ib.draw(screen)

        # 4. finalize
        pygame.display.flip()
        clock.tick(60)
    return 


if __name__ == "__main__":
    main()