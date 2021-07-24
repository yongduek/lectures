import gym
import numpy as np
import time 
from Q_learner_MountainCar import Q_Learner

if __name__ == "__main__":
    env = gym.make('MountainCar-v0')
    agent = Q_Learner(env)

    # load the policy learned
    with open('learned_policy.npy', 'rb') as f:
        policy = np.load(f)

    done = False
    total_reward = 0.0
    action_seq = []
    env = gym.wrappers.Monitor(env, 'replay_recording', force=True)
    obs = env.reset()
    while not done:
        env.render()
        action = policy[agent.discretize(obs)]
        action_seq.append(action)
        next_obs, reward, done, info = env.step(action)
        total_reward += reward
        obs = next_obs
    #
    print('Finished. Total Reward: ', total_reward)
    time.sleep(30/1000.)
    env.close()
    
    import matplotlib.pyplot as plt 
    plt.plot(action_seq, '-o')
    plt.xlabel('time index')
    plt.ylabel(f'A(t)')
    plt.savefig('action_seq.png')