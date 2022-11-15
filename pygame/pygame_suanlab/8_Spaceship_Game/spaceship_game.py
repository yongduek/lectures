import pygame
import os
import sys
import random
import math
from time import sleep

# 게임 스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색 정의
BLACK = (0, 0, 0)
WHITE= (200, 200, 200)
YELLOW = (250, 250, 20)
BLUE = (20, 20, 250)

# 전역 변수
FPS = 60

# 우주선 객체
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__()
        spaceship_image_path = resource_path('assets/spaceship.png')
        explosion_image_path = resource_path('assets/explosion.png')
        explosion_sound_path = resource_path('assets/explosion.wav')
        self.image = pygame.image.load(spaceship_image_path)
        self.explosion_image = pygame.image.load(explosion_image_path)
        self.explosion_sound = pygame.mixer.Sound(explosion_sound_path)
        self.rect = self.image.get_rect()
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

    # 우주선 위치 지정
    def set_pos(self, x, y):
        self.rect.x = x - self.centerx
        self.rect.y = y - self.centery

    # 우주선 충돌 체크
    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite

    # 충돌 이벤트 발생
    def occur_explosion(self, screen):
        explosion_rect = self.explosion_image.get_rect()
        explosion_rect.x = self.rect.x
        explosion_rect.y = self.rect.y
        screen.blit(self.explosion_image, explosion_rect)
        pygame.display.update()
        self.explosion_sound.play()

# 암석 객체
class Rock(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, hspeed, vspeed):
        super(Rock, self).__init__()
        rock_images_path = resource_path('assets/rock')
        image_file_list = os.listdir(rock_images_path)
        self.image_path_list = [os.path.join(rock_images_path, file)
                                for file in image_file_list if file.endswith(".png")]
        choice_rock_path = random.choice(self.image_path_list)
        self.image = pygame.image.load(choice_rock_path)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed
        self.set_direction()

    # 방향 지정
    def set_direction(self):
        if self.hspeed > 0:
            self.image = pygame.transform.rotate(self.image, 270)
        elif self.hspeed < 0:
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.vspeed > 0:
            self.image = pygame.transform.rotate(self.image, 180)

    # 업데이트
    def update(self):
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed

# 워프 객체
class Warp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Warp, self).__init__()
        self.image = pygame.image.load(resource_path('assets/warp.png'))
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.centerx
        self.rect.y = y - self.rect.centery

# 게임 객체
class Game():
    def __init__(self):
        self.menu_image = pygame.image.load(resource_path('assets/game_screen.png'))
        self.background_img = pygame.image.load(resource_path('assets/background.jpg'))
        self.font_70 = pygame.font.Font(resource_path('assets/NanumGothic.ttf'), 70)
        self.font_30 = pygame.font.Font(resource_path('assets/NanumGothic.ttf'), 30)
        self.warp_sound = pygame.mixer.Sound(resource_path('assets/warp.wav'))
        pygame.mixer.music.load(resource_path('assets/Inner_Sanctum.mp3'))

        self.spaceship = Spaceship()
        self.rocks = pygame.sprite.Group()
        self.warps = pygame.sprite.Group()

        self.occur_prob = 15
        self.score = 0
        self.warp_count = 1

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                    self.score = 0
                    self.warp_count = 1
                    # 게임 메뉴 On/Off
                    self.menu_on = False
            # 게임 화면 이벤트 처리
            else:
                if event.type == pygame.MOUSEMOTION:
                    self.spaceship.set_pos(*pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.warp_count > 0:
                        self.warp_count -= 1
                        self.warp_sound.play()
                        sleep(1)
                        self.rocks.empty()

        return False

    # 게임 로직 수행
    def run_logic(self, screen):
        # 운석 수와 속도 조절
        occur_of_rocks = 1 + int(self.score / 500)
        min_rock_speed = 1 + int(self.score / 400)
        max_rock_speed = 1 + int(self.score / 300)

        # 랜덤 확률의 빈도로 수행
        if random.randint(1, self.occur_prob) == 1:
            # 운석 생성 및 생성된 운석만큼 점수 증가
            for i in range(occur_of_rocks):
                self.rocks.add(self.create_random_rock(min_rock_speed, max_rock_speed))
                self.score += 1

            # 랜덤 확률로 워프 아이템 생성
            if random.randint(1, self.occur_prob * 10) == 1:
                warp = Warp(random.randint(30, SCREEN_WIDTH - 30),
                            random.randint(30, SCREEN_HEIGHT - 30))
                self.warps.add(warp)

        # 우주선이 암석과 충돌
        if self.spaceship.collide(self.rocks):
            pygame.mixer.music.stop()
            self.spaceship.occur_explosion(screen)
            self.rocks.empty()
            self.menu_on = True
            sleep(1)

        # 워프 아이템을 먹은 경우
        warp = self.spaceship.collide(self.warps)
        if warp:
            self.warp_count += 1
            warp.kill()

    # 랜덤한 암석 생성
    def create_random_rock(self, min_rock_speed, max_rock_speed):
        direction = random.randint(1, 4)
        speed = random.randint(min_rock_speed, max_rock_speed)
        if direction == 1:  # Up -> Down
            return Rock(random.randint(0, SCREEN_WIDTH), 0, 0, speed)
        elif direction == 2:  # Right -> Left
            return Rock(SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT), -speed, 0)
        elif direction == 3:  # Down -> Up
            return Rock(random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT, 0, -speed)
        elif direction == 4:  # Left -> Right
            return Rock(0, random.randint(0, SCREEN_HEIGHT), speed, 0)

    # 배경 그리기
    def draw_background(self, screen):
        background_rect = self.background_img.get_rect()
        for i in range(int(math.ceil(SCREEN_WIDTH / background_rect.width))):
            for j in range(int(math.ceil(SCREEN_HEIGHT / background_rect.height))):
                rect = pygame.Rect(i * background_rect.width,
                                   j * background_rect.height,
                                   background_rect.width,
                                   background_rect.height)
                screen.blit(self.background_img, rect)

    # 텍스트 그리기
    def draw_text(self, screen, text, font, x, y, main_color):
        text_obj = font.render(text, True, main_color)
        text_rect = text_obj.get_rect()
        text_rect.center = x, y
        screen.blit(text_obj, text_rect)

    # 게임 메뉴 출력
    def display_menu(self, screen):
        pygame.mouse.set_visible(True)

        screen.blit(self.menu_image, [0, 0])
        draw_x = int(SCREEN_WIDTH / 2)
        draw_y = int(SCREEN_HEIGHT / 4)
        self.draw_text(screen, '우주 암석 피하기',
                       self.font_70, draw_x, draw_y, WHITE)
        self.draw_text(screen, '점수: {}'.format(self.score),
                       self.font_30, draw_x, draw_y + 100, YELLOW)
        self.draw_text(screen, "마우스 버튼을 누르면 게임이 시작됩니다.",
                       self.font_30, draw_x, draw_y + 180, WHITE)

    # 게임 프레임 출력
    def display_frame(self, screen):
        self.draw_background(screen)
        screen.blit(self.spaceship.image, self.spaceship.rect)
        self.draw_text(screen, '점수: {}'.format(self.score),
                       self.font_30, 80, 20, YELLOW)
        self.draw_text(screen, '워프: {}'.format(self.warp_count),
                       self.font_30, 700, 20, BLUE)
        self.rocks.update()
        self.warps.update()
        self.rocks.draw(screen)
        self.warps.draw(screen)


# 게임 리소스 경로
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    # 게임 설정
    pygame.init()
    pygame.display.set_caption('Spaceship Game')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_events()
        if game.menu_on:  # 게임 메뉴 처리
            game.display_menu(screen)
        else:  # 게임 화면 처리
            game.run_logic(screen)
            game.display_frame(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
