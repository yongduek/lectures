# yndk@sogang.ac.kr
# Figure 13.1 is drawn from simulation of Exercise13.1.
# pytorch is used.
# Here, the policy is all the same regardless of the state
# policy is given by
#     score = t_1 [1, 0] + t_2 [0, 1] = [t1, t2]
#     pi = softmax(score)

# The environment and utility functions are from the following:
# https://github.com/ShangtongZhang/reinforcement-learning-an-introduction/blob/master/chapter13/short_corridor.py

import torch 
import numpy as np
import matplotlib.pyplot as plt 
from tqdm import tqdm, trange 


class ShortCorridor:
    """
    Short corridor environment, see Example 13.1
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = 0

    def step(self, go_right):
        """
        Args:
            go_right (bool): chosen action
        Returns:
            tuple of (reward, episode terminated?)
        """
        if self.state == 0 or self.state == 2:
            if go_right:
                self.state += 1
            else:
                self.state = max(0, self.state - 1)
        else:
            if go_right:
                self.state -= 1
            else:
                self.state += 1

        if self.state == 3:
            # terminal state
            return 0, True
        else:
            return -1, False
#

class ReinforceAgent:
    """
    REINFORCE Monte-Carlo Policy Gradient Sutton&Barto Ch. 13
    """

    def __init__(self, alpha, gamma):
        self.alpha = alpha
        self.gamma = gamma 

        self.theta = torch.tensor([-2., 2.], requires_grad=True)  # large value (skewed probability) causes very slow convergence
        self.rewards = []
        self.probs = []

    def get_pi(self, torch_softmax=True):
        if torch_softmax:
            pi = torch.nn.functional.softmax(self.theta, dim=-1)
        else:
            exp = torch.exp(self.theta)
            pi = exp / exp.sum() 
        return pi

    def choose_action(self,):
        pi = self.get_pi()
        # since only two actions exists,
        if np.random.uniform() < pi[0]:
            action = 0
        else:
            action = 1  # go_right

        self.probs.append(pi[action])
        return action
    #
    def append(self, reward):
        self.rewards.append(reward)
    #
    def learn(self,):
        Gs = []
        G = 0.
        for r in self.rewards[::-1]:
            G = r + G * self.gamma
            Gs.insert(0, G)  # in-order insertion

        Gs = torch.tensor(Gs)
        Gs = (Gs - Gs.mean()) / Gs.std()  # numerical
        loss = 0.  # total sum of loss
        for t, (G, p) in enumerate(zip(Gs, self.probs)):
            gt = self.gamma ** t
            loss += - gt * G * torch.log(p)
        if self.theta.grad is not None:
            self.theta.grad.zero_()  # clearn the buffer
        loss.backward()  # gradient computation

        with torch.no_grad():
            self.theta -= self.alpha * self.theta.grad  # gamma is assumed to be 1
        
        del self.rewards[:]
        del self.probs[:] 
        pass 

def trial(num_episodes, agent_generator):
    env = ShortCorridor()
    agent = agent_generator()

    rewards = np.zeros(num_episodes)
    for episode_idx in range(num_episodes):
        rewards_sum = 0
        reward = None
        env.reset()

        while True:
            go_right = agent.choose_action()
            reward, episode_end = env.step(go_right)
            rewards_sum += reward
            agent.append(reward)

            if episode_end:
                agent.learn()  # learning MC update
                break

        rewards[episode_idx] = rewards_sum

    return rewards
#

def figure_13_1():
    num_trials = 10
    num_episodes = 2000
    gamma = 1
    agent_generators = [lambda : ReinforceAgent(alpha=2e-4, gamma=gamma),
                        lambda : ReinforceAgent(alpha=2e-5, gamma=gamma),
                        lambda : ReinforceAgent(alpha=2e-3, gamma=gamma)]
    labels = ['alpha = 2e-4',
              'alpha = 2e-5',
              'alpha = 2e-3']

    rewards = np.zeros((len(agent_generators), num_trials, num_episodes))

    for agent_index, agent_generator in enumerate(agent_generators):
        for i in tqdm(range(num_trials)):
            reward = trial(num_episodes, agent_generator)
            rewards[agent_index, i, :] = reward

    plt.plot(np.arange(num_episodes) + 1, -11.6 * np.ones(num_episodes), ls='dashed', color='red', label='-11.6')
    for i, label in enumerate(labels):
        plt.plot(np.arange(num_episodes) + 1, rewards[i].mean(axis=0), label=label, alpha=.7)
    plt.ylabel('total reward on episode')
    plt.xlabel('episode')
    plt.legend(loc='lower right')

    plt.savefig('figure_13_1.png')
    plt.close()
#


figure_13_1()