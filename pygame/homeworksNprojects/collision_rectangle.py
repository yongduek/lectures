# -*- coding: utf-8 -*- 
import pygame
import numpy as np 

# 게임 윈도우 크기
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# 색 정의
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED  = (255, 0, 0)

class Rectangle:
    def __init__(self, w, h, x, y, dx, dy, color):
        self.w = w 
        self.h = h 
        self.color = color
        self.x = x 
        self.y = y 
        self.dx = dx 
        self.dy = dy 
        self.collided = False 
        
    def update(self):
        self.x += self.dx
        self.y += self.dy

        if (self.x + self.w) >= WINDOW_WIDTH:
            self.dx = self.dx * -1
            self.x = WINDOW_WIDTH - self.w 
        
        if  self.x < 0:
            self.dx *= -1.
            self.x = 0
        
        if (self.y + self.h) > WINDOW_HEIGHT:
            self.dy = self.dy * -1
            self.y = WINDOW_HEIGHT - self.h
        
        if self.y  < 0:
            self.dy *= -1
            self.y = 0
        pass
    
    def draw(self, screen):
        rect = [self.x, self.y, self.w, self.h]
        # print(rect)
        pygame.draw.rect(screen, color=self.color, rect=rect)
        # if not self.collided:
        #     pygame.draw.rect(screen, color=self.color, rect=[self.x, self.y, self.w, self.h])
        # else:
        #     pygame.draw.rect(screen, color=RED, rect=[self.x, self.y, self.w, self.h])
        pass 
#

def collideAABB(r1, r2):
    xflag = r1.x  < r2.x + r2.w  and  r2.x < r1.x + r1.w 
    yflag = r1.y  < r2.y + r2.h  and  r2.y < r1.y + r1.y
    if xflag and yflag:
        return True 
    else:
        return False 
#
 
def main():
    # Pygame 초기화
    pygame.init()

    # 윈도우 제목
    pygame.display.set_caption("Rectangle")

    # 윈도우 생성
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # 게임 화면 업데이트 속도
    clock = pygame.time.Clock()

    # 공 초기 위치, 크기, 속도
    nBalls = 3
    listball = []
    for i in range(nBalls):
        b = Rectangle(w=np.random.randint(152, 160), \
                      h=np.random.randint(152, 160), \
                        x = np.random.uniform(20, WINDOW_WIDTH-300), \
                        y = np.random.uniform(20, WINDOW_HEIGHT-300), \
                        dx = np.random.uniform(3,7),
                        dy = np.random.uniform(3,7),
                        color=(np.random.randint(0,20), np.random.randint(0,256), np.random.randint(0,256)))
        listball.append(b)
        
    # 게임 종료 전까지 반복
    done = False

    # 게임 반복 구간
    while not done:
        # 이벤트 반복 구간
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # 게임 로직 구간
        # 속도에 따라 원형 위치 변경
        for b in listball:
            b.update()


        # ------------------------------------------------------------------------------------
        collided = []
        for i in range(nBalls):
            for j in range(i+1, nBalls):
                if collideAABB(listball[i], listball[j]):
                    # collided; let's just relocate one of them; but after collision detection
                    listball[i].collided = True
                    listball[j].collided = True
                    collided.append(i)
                    collided.append(j)
        # --------------------------------------------------------------------------------------   
        # 윈도우 화면 채우기
        screen.fill(GRAY)

        # 화면 그리기 구간
        for b in listball:
            b.draw(screen)
            
        # 화면 업데이트
        pygame.display.flip()
        clock.tick(30)

        # # collision resolution
        for i in range(nBalls):
            if listball[i].collided == True:
                listball[i].x = np.random.uniform(10, WINDOW_WIDTH - 300)
                listball[i].y = np.random.uniform(10, WINDOW_HEIGHT - 300)
                listball[i].collided = False 
        # ---------------------------------------------------------------------------------------        

    return 
#

if __name__ == "__main__":
    main()
    # 게임 종료
    pygame.quit()