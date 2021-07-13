import time 
import gym  # OpenAI Gym을 사용하기 위해 라이브러리 import
from gym.envs.registration import register
# import sys, tty, termios # 키 입력을 위한 라이브러리 for Linux/Unix
import sys, msvcrt  ## windows

# 키입력을 받기 위한 클래스
class _Getch:
  # 키값 리턴
  def __call__(self):
      fd = sys.stdin.fileno()
      old_setting = termios.tcgetattr(fd)
      try:
          tty.setraw(sys.stdin.fileno())
          ch = sys.stdin.read(1)
      finally:
          termios.tcsetattr(fd, termios.TCSADRAIN, old_setting)
      print(ch)
      return ch
#
# choose one for keyboard input
# inkey = _Getch()       # linux
inkey = msvcrt.getwch  # https://docs.python.org/3.7/library/msvcrt.html#console-i-o

# OpenAI Gym에서 미리 정의되어 있는 action 매핑
RIGHT = 1
LEFT = 0

# 키보드 키와 상하좌우 동작을 매핑
arrow_keys = {
    'l' : RIGHT,
    'a' : LEFT,
}

game_speed = 1./10. # seconds

# Gym 환경설정
# https://gym.openai.com/envs/ 에 들어가면 다양한 환경을 살펴볼 수 있다.

env = gym.make("CartPole-v0")

state = env.reset()
env.render()
print(f'> reset returned: {state}')

G = 0  # total return
while True:  # repeat forever
    # 키 값을 기다린다
    key = inkey()

    # 만약에 우리가 정의한 키 값이 아닌 경우, 
    if key not in arrow_keys.keys():
        print('actions: ', arrow_keys.keys())
        continue
    
    # 키값과 액션 매핑을 사용해서 상하좌우 중 어떤 행동을 취할지 리턴
    action = arrow_keys[key]

    # env.step(action) 은 결정한 행동을 실행한다는 의미이고,
    # 행동의 결과로 이동한 자리가 어딘지(state), 행동의 reward는 얼마인지(reward), 
    # 게임이 끝났는지: 구멍에 빠지거나 결승점에 도착하거나 (done), 그 밖의 정보 (info)가 리턴된다.
    state, reward, done, info = env.step(action)
    G += reward 

    # 화면에 그림
    env.render()
    time.sleep(game_speed) # wait for a while for user interface

    # 게임이 끝났으면 Reward를 출력
    if done :
        print(f"Finished with total return {G}")
        # break