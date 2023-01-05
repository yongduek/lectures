import pygame
import numpy as np 

def Rmat(deg):
    """ deg: angle in degree """
    radian = np.deg2rad(deg)
    c = np.cos(radian)
    s = np.sin(radian)
    m = np.eye(3)
    m[0,0] = m[1,1] = c 
    m[1,0] = s 
    m[0,1] = -s 
    return m 

def Tmat(tx, ty):
    m = np.eye(3)
    m[0,2] = tx 
    m[1,2] = ty
    return m 

def getHomogeneous(p_aff):
    """ p_aff: N x 2 affine coordinates, each row being a 2D coordinate vector """
    ones = np.ones( (p_aff.shape[0], 1) )
    p_homo = np.hstack( (p_aff, ones) )
    return p_homo
#

class Polygon:
    def __init__(self, vertices, color=(255,100,200)):
        """ vertices: N x 2 point coordinates for a proper polygon """
        self.vertices = getHomogeneous(vertices)  # must be 
        self.color = color            
        self.transform_ip(np.eye(3))
                
    def transform(self, H):  # or update()
        """ vertices = H @ vertices """
        vh = H @ self.vertices.T
        vh = vh.T 
        va = vh[:,:2]
        return Polygon(va) 
    
    def transform_ip(self, H):  # or update()
        """ vertices = H @ vertices """
        self.vh = H @ self.vertices.T
        self.vh = self.vh.T 
        self.va = self.vh[:,:2]
        
    def draw(self, screen, color=None):
        if color is not None:
            pygame.draw.polygon(screen, color, self.va, 4)
        else:
            pygame.draw.polygon(screen, self.color, self.va, 4)

    def print(self,):
        print(self.va)        
#


# our main object
pwidth = 100
pheight = 40
cx, cy = 30, pheight / 2  # rotation center of the cannon
p = np.array([ [0,0], [pwidth, 0], [pwidth, pheight], [0, pheight]])
poly = Polygon(p, color=(0,255, 255))
poly.print()
HTx = np.eye(3)
deg = 0


class Shoot:
    def __init__(self, pos=[0,0], vel=0, dir=0):
        self.pos = np.array(pos[:2])
        self.dir = dir # direction
        self.dirvec = np.array([np.cos(np.deg2rad(self.dir)), np.sin(np.deg2rad(self.dir))]) 
        self.vel = self.dirvec * vel
        self.acc = np.array([0, 600]) # accelaration
        # --- for drawing ---
        self.radius = 3
        self.tick = pygame.time.get_ticks()
        self.color = (100, 20, 80)
        self.flag = False
        
    def fire(self):
        self.flag = True 
        self.tick = pygame.time.get_ticks()
        
    def update(self):
        if self.flag:
            dt = 1 # ( pygame.time.get_ticks() - self.tick ) / 1000  # can be realistic by using pygame.time.get_ticks()
            current_tick = pygame.time.get_ticks()
            dt = ( current_tick - self.tick ) / 1000 
            self.tick = current_tick
            
            self.pos = self.pos + self.vel * dt + 0.5 * self.acc * dt * dt 
            self.vel = self.vel + self.acc * dt 
            # print(self.pos, self.vel, dt)
                        
            if self.pos[1] > WINDOW_HEIGHT + 100:
                self.flag = False  # stop simulation
                
    def draw(self, screen):
        if self.flag:
            pygame.draw.circle(screen, color=self.color, center=self.pos, radius=self.radius)
#
shooting_velocity = 1000
shoot = Shoot()
# --------------------------------------------------------------------
# 게임 윈도우 크기
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1200

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Drawing")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()
# pygame.time.get_ticks() returns elapsed time since its last call

# 게임 종료 전까지 반복
done = False

# 게임 반복 구간
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True 
        if 0: # following does not allow you continous check          
            if event.key == pygame.K_UP:
                deg -= 1
                if deg < -85: deg = -85
            elif event.key == pygame.K_DOWN:
                deg += 1
                if deg > 0: deg = 0
    #
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
        deg -= 2
        if deg < -85: deg = -85
    if keystate[pygame.K_DOWN]:
        deg += 2
        if deg > 0: deg = 0 
    if keystate[pygame.K_SPACE]:
        if shoot.flag == False:
            shoot = Shoot(pos=[center[0,0], center[1,0]], vel=shooting_velocity, dir=deg)
            shoot.fire()
    
    # update states
    shoot.update()
    #
    
    # screen.fill(WHITE)

    # initial location of the cannon object
    poly.draw(screen, color=(20, 0, 200))
  
    # put it at the bottom of the screen
    tx1, ty1 = 10, WINDOW_HEIGHT - 100
    H = Tmat(tx1, ty1)   
    poly_tx = poly.transform(H)
    poly_tx.draw(screen)
    
    # now the cannon rectangle is at (tx1, ty1) with (pwidth, pheight)
    # we rotate it with respect to (tx1+cx, ty1 + cy)
    tx2, ty2 = cx, cy
    # tx2, ty2 = 0, 0 # try this and see
    H = H @ Tmat(tx2, ty2) @ Rmat(deg) @ Tmat(-tx2, -ty2) 
    cannon = poly.transform(H)
    cannon.draw(screen, color=(200, 20, 20))
    center = H @ np.array([[cx, cy, 1]]).T # make a 3x1 matrix
    pygame.draw.circle(screen, (255, 0, 0), (center[0,0], center[1,0]), radius=3)
    
    shoot.draw(screen)    
    
    
    # 폰트 선택(폰트, 크기, 두껍게, 이탤릭)
    font = pygame.font.SysFont('FixedSys', 40, True, False)
    text = font.render("Hello Pygame", True, BLACK)

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()