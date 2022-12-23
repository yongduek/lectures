# -*- coding: utf-8 -*- 
import pygame
import numpy as np 

# 게임 윈도우 크기
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 색 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Ball")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 공 초기 위치, 크기, 속도
ball_x = int(WINDOW_WIDTH / 2)
ball_y = int(WINDOW_HEIGHT / 2)
ball_dx = 4 # velocity x
ball_dy = 4 # velocity y 
ball_size = 40 # radius

class Ball:
    def __init__(self,):
        self.x = np.random.randint(low=100, high=200)
        self.y = np.random.randint(low=100, high=200)
        self.radius = np.random.randint(low=1, high=30)
        self.dx = np.random.randint(-9, 10)
        self.dy = np.random.randint(-10, 11)
        self.color = (np.random.randint(low=0, high=256), 
                        np.random.randint(low=0, high=256),
                        np.random.randint(low=0, high=256))

        self.time = pygame.time.get_ticks()
        self.period = np.random.uniform(1000, 6000)

    def update(self,):
        if 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.time > self.period: # milisecond
                self.dx = np.random.randint(-19, 20)
                self.dy = np.random.randint(-20, 21)
                self.time = current_time
                pass

        self.x += self.dx 
        self.y += self.dy 

        if self.x + self.radius > WINDOW_WIDTH:  # right side bounce
            self.dx *= -1

        if self.x - self.radius < 0: # left side bounce
            self.dx *= -1

        if self.y + self.radius > WINDOW_HEIGHT: # bootom side bounce
            self.dy *= -1

        if self.y - self.radius < 0: # top side bounce
            self.dy *= -1


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# 게임 종료 전까지 반복
done = False

ball = Ball()
print(ball)
listOfBalls = []
for i in range(20):
    ball = Ball()
    listOfBalls.append(ball)

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 게임 로직 구간
    # 속도에 따라 원형 위치 변경: state update / logic update / parameter update
    # ------------------------
    ball_x += ball_dx
    ball_y += ball_dy

    # 공이 윈도우를 벗어날 경우
    if (ball_x + ball_size) > WINDOW_WIDTH or (ball_x - ball_size) < 0:
        ball_dx = ball_dx * -1
    if (ball_y + ball_size) > WINDOW_HEIGHT or (ball_y - ball_size) < 0:
        ball_dy = ball_dy * -1
    # -----------------------------------
    # update ball 2
    # your update code here
    for i in range(len(listOfBalls)):
        ball = listOfBalls[i]
        ball.update()
    # -----------------------------------
    # 윈도우 화면 채우기
    screen.fill(WHITE)

    # 화면 그리기 구간
    # 공 그리기
    pygame.draw.circle(screen, BLUE, [ball_x, ball_y], ball_size, 0)

    for i in range(len(listOfBalls)):
        ball = listOfBalls[i]
        ball.draw(screen)

    # 화면 업데이트
    pygame.display.flip()
    # 초당 60 프레임으로 업데이트
    clock.tick(60) # 60 frames per second
                   # ball_dx = 4
                   # ball_velocity_x = 4 pixels / 1 frame * 60 (frames / second)
                    #                = 240 pixels / second
# 게임 종료
pygame.quit()