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
        
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.va, 4)

    def print(self,):
        print(self.va)        
#



p = np.array([ [2, 2], [5, 2], [5, 5], [3, 5], [2, 3]]) * 200
poly = Polygon(p + np.array([100, -150]), color=(0,255, 255))
poly.print()

poly2 = Polygon(p + np.array([-100, -150]), color=(255, 0, 0))

HTx = np.eye(3)
deg = 0 


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
    #
    
    screen.fill(WHITE)

    # A triangle
    pygame.draw.polygon(screen, GREEN, [[350, 200], [250, 350], [450, 350]], 4)

    # A polygon
    pygame.draw.polygon(screen, BLUE, p, 5)
    
    
    # translational motion
    HTx[0,2] += 1
    if HTx[0,2] > WINDOW_WIDTH: HTx[0,2] = 0
    
    poly_tx = poly.transform(HTx)
    poly_tx.draw(screen)
    
    # rotation w.r.t (0,0)
    deg += 1
    poly2.transform_ip(Rmat(deg))
    poly2.draw(screen)
    
    # rotation w.r.t to (x0, y0)
    if 1:
        # 1. let's choose any rotation center
        x0, y0 = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
        x0, y0 = 1100, 850 # one of the vertices of poly
        # 2. compute transformation matrix
        H = Tmat(x0, y0) @ Rmat(deg) @ Tmat(-x0, -y0)
        # 3. apply transformation
        poly_rot = poly.transform(H)
        # 4. draw
        poly_rot.draw(screen)
        #
        pygame.draw.circle(screen, RED, (x0, y0), 5) # center of rotation
    
    # 폰트 선택(폰트, 크기, 두껍게, 이탤릭)
    font = pygame.font.SysFont('FixedSys', 40, True, False)

    # 안티얼리어스를 적용하고 검은색 문자열 렌더링
    text = font.render("Hello Pygame", True, BLACK)

    # 화면 업데이트
    pygame.display.flip()
    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()