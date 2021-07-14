# RLBook Ch. 4.3 Policy Iteration (Page 80)

import numpy as np
import gym

rng = np.random.default_rng(202102)

env = gym.make('FrozenLake-v0')
# env = gym.make('FrozenLake8x8-v0')

states = np.arange(env.observation_space.n)
N = int(np.sqrt(env.observation_space.n))
actions = np.arange(env.action_space.n)

V = rng.normal(size=(env.observation_space.n))
terminal_state = [states[-1]]
V[terminal_state] = 0

policy = np.array([env.action_space.sample() for s in states]) ## initially randome action


gamma = 0.9

def policy_iteration(niter=1000, neval=10000):
    for it in range(1, niter):  # 
        # policy_evalation(env)
        for ev in range(1, neval):
            delta = 0
            for s in range(env.observation_space.n):  # for each state S,
                if s in terminal_state: continue 
                v = V[s]
                v_eval = 0
                action = policy[s]
                for prob, s2, reward, done in env.P[s][action]:
                    v_eval += prob * (reward + gamma * V[s2])
                V[s] = v_eval
                delta = max(delta, np.abs(v - V[s]))
            #
            if delta < 1E-7: 
                break
        print(f'>> {it:4}  evaluation done in {ev}, delta: {delta:.3e}')
        #
        # policy_improvement(env)
        stable = True 
        for s in range(env.observation_space.n):  # for each state S,
            if s in terminal_state: continue 
            old_action = policy[s]
            bo = []
            for a in actions: #
                vs = 0
                for prob, s2, reward, done in env.P[s][a]:
                    vs += prob * (reward + gamma * V[s2])
                bo.append(vs)
            policy[s] = np.argmax(bo)
            if old_action != policy[s]: 
                stable = False
        if stable :
            print(f'>> {it:4}  stable {stable} policy iteration finished.')
            return V, policy 
    # iteration
    return V, policy  # finished iteration. It can be run again for another iteration.
#

def run():
    s = env.reset()
    done = False 
    G = 0
    nsteps = 0
    while not done:
        action = policy[s]
        s, r, done, info = env.step(action)
        G += r
        nsteps += 1 
    # the reward is only at the trasition to terminal state
    # print(done, info)
    return G, nsteps

def test_run(nrepeat=1000):
    glist, nlist = [], []
    for i in range(nrepeat):
        g, n = run()
        glist.append(g)
        nlist.append(n)
    nTimeOut = sum(np.array(nlist) == env._max_episode_steps)
    print('$ test result: success cases: ', sum(glist), 'out of', nrepeat)
    print('$ nTimeOut: ', nTimeOut)
    print(f'$ Except for timeout, success rate = {sum(glist)/(nrepeat - nTimeOut):.2f}')

if __name__ == "__main__":
    # env = gym.make('FrozenLake-v0')
    print(env, 'maximum_epsode_steps', env._max_episode_steps)
    scene = env.render(mode='human')
    print(scene, type(scene))

    print('Initial: ', '\n', V.reshape(N,N), '\n', policy.reshape(N,N))

    policy_iteration()

    ActionMarker = ['<', '!', '>', '^']
    print(V.reshape(N,N), '\n', policy.reshape(N,N))
    for pr in policy.reshape(N,N):
        for c in pr:
            print(ActionMarker[c], end=' ')
        print()

    test_run()
