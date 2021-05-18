# install atari-py in windows 10
# if atari-py is installed and doesn't work, then delete it first.
#
# https://stackoverflow.com/questions/42605769/openai-gym-atari-on-windows/46739299
#   $ pip install -f https://github.com/Kojoley/atari-py/releases atari_py
#
# basically gym atari is not supported in windows 10

import gym
print(gym.__version__)

env = gym.make('SpaceInvaders-v0')
env.reset()
reward = 0
for i in range(3000):
    s, r, done, info = env.step(env.action_space.sample())
    reward += r
    env.render('human')
    if done:
        print('done: ', r, info, reward, i)
        break
env.close()  # https://github.com/openai/gym/issues/893