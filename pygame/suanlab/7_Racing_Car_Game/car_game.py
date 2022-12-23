import pygame
import os
import sys
import random
from time import sleep

# 게임 스크린 전역변수
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# 색상 전역변수
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (200, 0, 0)

# 게임 전역 변수
CAR_COUNT = 3
LANE_COUNT = 5
SPEED = 10
FPS = 60

# 자동차 객체
class Car():
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        car_images_path = resource_path('assets/car')
        image_file_list = os.listdir(car_images_path)
        self.image_path_list = [os.path.join(car_images_path, file)
                                for file in image_file_list if file.endswith(".png")]

        crash_image_path = resource_path('assets/crash.png')
        crash_sound_path = resource_path('assets/crash.wav')
        collision_sound_path = resource_path('assets/collision.wav')
        engine_sound_path = resource_path('assets/engine.wav')
        self.crash_image = pygame.image.load(crash_image_path)
        self.crash_sound = pygame.mixer.Sound(crash_sound_path)
        self.collision_sound = pygame.mixer.Sound(collision_sound_path)
        self.engine_sound = pygame.mixer.Sound(engine_sound_path)

    # 자동차 이미지 로드
    def load_image(self):
        choice_car_path = random.choice(self.image_path_list)
        self.image = pygame.image.load(choice_car_path)
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    # 자동차 로드
    def load(self):
        self.load_image()
        self.x = int(SCREEN_WIDTH / 2)
        self.y = SCREEN_HEIGHT - self.height
        self.dx = 0
        self.dy = 0
        self.engine_sound.play()

    # 자동차 랜덤 로드
    def load_random(self):
        self.load_image()
        self.x = random.randrange(0, SCREEN_WIDTH - self.width)
        self.y = -self.height
        self.dx = 0
        self.dy = random.randint(4, 9)

    # 자동차 이동
    def move(self):
        self.x += self.dx
        self.y += self.dy

    # 스크린 범위 체크
    def out_of_screen(self):
        if self.x + self.width > SCREEN_WIDTH or self.x < 0:
            self.x -= self.dx
        if self.y + self.height > SCREEN_HEIGHT or self.y < 0:
            self.y -= self.dy

    # 자동차 충돌 체크
    def check_crash(self, car):
        if (self.x + self.width > car.x) and (self.x < car.x + car.width) \
           and (self.y < car.y + car.height) and (self.y + self.height > car.y):
            return True
        else:
            return False

    # 자동차 그리기
    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

    # 자동차 충돌 그리기
    def draw_crash(self, screen):
        width = self.crash_image.get_rect().width
        height = self.crash_image.get_rect().height
        draw_x = self.x + int(self.width / 2) - int(width / 2)
        draw_y = self.y + int(self.height / 2) - int(height / 2)
        screen.blit(self.crash_image, [draw_x, draw_y])
        pygame.display.update()

# 차선 객체
class Lane():
    def __init__(self):
        self.color = WHITE
        self.width = 10
        self.height = 80
        self.gap = 20
        self.space = (SCREEN_WIDTH - (self.width * LANE_COUNT)) / (LANE_COUNT - 1)
        self.count = 10
        self.x = 0
        self.y = -self.height

    # 차선 이동
    def move(self, speed, screen):
        self.y += speed
        if self.y > 0:
            self.y = -self.height
        self.draw(screen)

    # 차선 그리기
    def draw(self, screen):
        next_lane = self.y
        for i in range(self.count):
            pygame.draw.rect(screen, self.color, \
                             [self.x, next_lane, self.width, self.height])
            next_lane += self.height + self.gap

# 게임 객체
class Game():
    def __init__(self):
        # 게임 리소스 로드
        menu_image_path = resource_path('assets/menu_car.png')
        self.image_intro = pygame.image.load(menu_image_path)
        pygame.mixer.music.load(resource_path('assets/race.wav'))
        font_path = resource_path('assets/NanumGothicCoding-Bold.ttf')
        self.font_40 = pygame.font.Font(font_path, 40)
        self.font_30 = pygame.font.Font(font_path, 30)

        # 도로 차선 생성
        self.lanes = []
        for i in range(LANE_COUNT):
            lane = Lane()
            lane.x = i * int(lane.space + lane.width)
            self.lanes.append(lane)

        # 컴퓨터 자동차 생성
        self.cars = []
        for i in range(CAR_COUNT):
            car = Car()
            self.cars.append(car)

        # 사용자 자동차 생성
        self.player = Car()

        # 게임 점수
        self.score = 0

        # 게임 메뉴 On/Off
        self.menu_on = True

    # 게임 이벤트 처리 및 조작
    def process_events(self):
        # 게임 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            # 메뉴 화면 이벤트 처리
            if self.menu_on:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.play(-1)
                        pygame.mouse.set_visible(False)
                        self.score = 0
                        self.menu_on = False
                        # 사용자 자동차 초기화
                        self.player.load()
                        # 컴퓨터 자동차 초기화
                        for car in self.cars:
                            car.load_random()
                        sleep(4)
            # 게임 화면 이벤트 처리
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.dy -= 5
                    elif event.key == pygame.K_DOWN:
                        self.player.dy += 5
                    elif event.key == pygame.K_LEFT:
                        self.player.dx -= 5
                    elif event.key == pygame.K_RIGHT:
                        self.player.dx += 5
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.player.dx = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.player.dy = 0

        return False

    # 게임 로직 수행
    def run_logic(self, screen):
        # 컴퓨터 자동차 체크
        for car in self.cars:
            # 컴퓨터 자동차 게임 화면 넘어감
            if car.y > SCREEN_HEIGHT:
                self.score += 10
                car.load_random()

            # 사용자 자동차 충돌 체크
            if self.player.check_crash(car):
                self.menu_on = True
                pygame.mixer.music.stop()
                self.player.crash_sound.play()
                self.player.draw_crash(screen)
                car.draw_crash(screen)
                sleep(1)
                pygame.mouse.set_visible(True)

            # 컴퓨터 자동차 충돌 체크
            for com in self.cars:
                if car == com:
                    None
                elif car.check_crash(com):
                    self.score += 10
                    car.collision_sound.play()
                    car.draw_crash(screen)
                    car.load_random()
                    com.draw_crash(screen)
                    com.load_random()

    # 텍스트 그리기
    def draw_text(self, screen, text, font, x, y, main_color):
        text_obj = font.render(text, True, main_color)
        text_rect = text_obj.get_rect()
        text_rect.center = x, y
        screen.blit(text_obj, text_rect)

    # 게임 메뉴 출력
    def display_menu(self, screen):
        screen.fill(GRAY)   # 게임 배경
        screen.blit(self.image_intro, [40, 150])
        draw_x = int(SCREEN_WIDTH / 2)
        draw_y = int(SCREEN_HEIGHT / 2)
        self.draw_text(screen, "PyCar: Racing Car Game",
                       self.font_40, draw_x, draw_y + 50, BLACK)
        self.draw_text(screen, "Score: " + str(self.score),
                       self.font_40, draw_x, draw_y + 150, WHITE)
        self.draw_text(screen, "Press Space Key to Start!",
                       self.font_30, draw_x, draw_y + 200, RED)

    # 게임 프레임 출력
    def display_frame(self, screen):
        screen.fill(GRAY)   # 게임 배경

        # 도로 차선 이동
        for lane in self.lanes:
            lane.move(SPEED, screen)

        # 사용자 자동차
        self.player.draw(screen)
        self.player.move()
        self.player.out_of_screen()

        # 컴퓨터 자동차
        for car in self.cars:
            car.draw(screen)
            car.move()

        # 점수 표시
        self.draw_text(screen, "Score: " + str(self.score),
                       self.font_30, 80, 20, BLACK)


# 게임 리소스 경로
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    # 게임 초기화 및 환경 설정
    pygame.init()
    pygame.display.set_caption("Racing Car Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_events()
        if game.menu_on:
            game.display_menu(screen)
        else:
            game.run_logic(screen)
            game.display_frame(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()