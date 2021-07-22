import gym
import numpy as np
import torch
import random
from collections import deque
from buffer import Buffer
from DQN import DQN

BUF_SIZE = 10000
BATCH_SIZE = 128
UPDATE_TARGET = 500 # Обновляем target сетку раз в UPDATE_TARGET обновлений основной сетки
GAMMA = 0.98

seed = 17
np.random.seed(seed)
random.seed(seed)
env = gym.make('MountainCar-v0')
env.seed(seed)
torch.manual_seed(seed)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def transform_state(state):
    state = (np.array(state) + np.array((1.2, 0.0))) / np.array((1.8, 0.07))
    result = []
    result.extend(state)
    return np.array(state)


def eps_greedy(env, dqn, state, eps):
    if random.random() < eps:
        return env.action_space.sample()
    return dqn.act(state)


def current_results(i, rews, eps, output_period=100):
    mean_r = np.mean(rews)
    max_r = np.max(rews)
    min_r = np.min(rews)
    print(f'\repisode {i}, eps = {eps}, mean = {mean_r}, min = {min_r}, max = {max_r}', end="")
    if not i % output_period:
        print(f'\repisode {i}, eps = {eps}, mean = {mean_r}, min = {min_r}, max = {max_r}')
    return mean_r


dqn = DQN(state_dim=2, action_dim=3, GAMMA=GAMMA, device=device)
buf = Buffer(BUF_SIZE)

episodes = 1500
eps = 1
eps_coeff = 0.995
dqn_updates = 0
output_period = 100
rews = deque(maxlen=output_period)  # сюда буду писать данные за output_period эпизодов

for i in range(1, episodes + 1):
    state = transform_state(env.reset())
    done = False
    total_reward = 0
    while not done:
        action = eps_greedy(env, dqn, state, eps)
        next_state, reward, done, _ = env.step(action)
        next_state = transform_state(next_state)
        total_reward += reward
        reward += 350 * (GAMMA * abs(next_state[1]) - abs(state[1]))
        buf.add((state, action, reward, next_state, done))
        if len(buf) >= BATCH_SIZE:
            dqn.update(buf.sample(BATCH_SIZE))
            dqn_updates += 1
        if not dqn_updates % UPDATE_TARGET:
            dqn.update_target()
        state = next_state
    eps *= eps_coeff
    rews.append(total_reward)
    mean_r = current_results(i, rews, eps, output_period)
