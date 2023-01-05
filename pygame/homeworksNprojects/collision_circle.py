# -*- coding: utf-8 -*- 
import pygame
import numpy as np 

# 게임 윈도우 크기
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# 색 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class Circle:
    def __init__(self, radius, x, y, dx, dy, color):
        self.radius = radius
        self.color = color
        self.x = x 
        self.y = y 
        self.dx = dx 
        self.dy = dy 
    
    def update(self):
        self.x += self.dx
        self.y += self.dy

        if (self.x + self.radius) > WINDOW_WIDTH or (self.x - self.radius) < 0:
            self.dx = self.dx * -1
            self.x += self.dx
        if (self.y + self.radius) > WINDOW_HEIGHT or (self.y - self.radius) < 0:
            self.dy = self.dy * -1
            self.y += self.dy
        pass 
    
    def draw(self, screen):
        pygame.draw.circle(screen, color=self.color, center=(self.x, self.y), radius=self.radius)
        pass 
#

def collideCircle(c1, c2):
    dist = np.sqrt( (c1.x - c2.x)**2 + (c1.y - c2.y)**2 )
    if dist <= c1.radius + c2.radius:
        return True 
    return False 

def main():
    # Pygame 초기화
    pygame.init()

    # 윈도우 제목
    pygame.display.set_caption("Ball")

    # 윈도우 생성
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # 게임 화면 업데이트 속도
    clock = pygame.time.Clock()

    # 공 초기 위치, 크기, 속도
    ball = Circle(20, x = int(WINDOW_WIDTH / 2), y = int(WINDOW_HEIGHT / 2), dx = 4, dy = 4, color=(255, 0, 0))

    nBalls = 5
    listball = []
    for i in range(nBalls):
        b = Circle(radius = np.random.randint(26, 35), \
                        x = np.random.uniform(100, WINDOW_WIDTH-100), \
                        y = np.random.uniform(100, WINDOW_HEIGHT-100), \
                        dx = np.random.uniform(1,7),
                        dy = np.random.uniform(1,7),
                        color=(np.random.randint(0,256), np.random.randint(0,256), np.random.randint(0,256)))
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
                if collideCircle(listball[i], listball[j]):
                    # collided; let's just relocate one of them; but after collision detection
                    if np.random.uniform(0,1) < .5:
                        collided.append(listball[i])
                    else: 
                        collided.append(listball[j])
        # --------------------------------------------------------------------------------------                
        # 윈도우 화면 채우기
        screen.fill(WHITE)

        # 화면 그리기 구간
        # 공 그리기
        for b in listball:
            b.draw(screen)
            
        # 화면 업데이트
        pygame.display.flip()
        clock.tick(60)

        # collision resolution
        for e in collided:
            e.x = np.random.uniform(100, WINDOW_WIDTH-100)
            e.y = np.random.uniform(100, WINDOW_HEIGHT-100)
            e.dx *= -1
            e.dy *= -1

if __name__ == "__main__":
    main()
    # 게임 종료
    pygame.quit()