import pygame

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
ball_dx = 4
ball_dy = 4
ball_size = 40

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
    ball_x += ball_dx
    ball_y += ball_dy

    # 공이 윈도우를 벗어날 경우
    if (ball_x + ball_size) > WINDOW_WIDTH or (ball_x - ball_size) < 0:
        ball_dx = ball_dx * -1
    if (ball_y + ball_size) > WINDOW_HEIGHT or (ball_y - ball_size) < 0:
        ball_dy = ball_dy * -1

    # 윈도우 화면 채우기
    screen.fill(WHITE)

    # 화면 그리기 구간
    # 공 그리기
    pygame.draw.circle(screen, BLUE, [ball_x, ball_y], ball_size, 0)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()