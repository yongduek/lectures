# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # TicTacToe Game & Tabular Q Learning

# %%
import numpy as np
import matplotlib.pyplot as plt 
from collections import defaultdict  
from tqdm import trange

rng = np.random.default_rng(2021)  # random number generator


# %%
class EnvTTT():
    def __init__(self,):
        self.reset()
        
    def reset(self,):
        self.board = '---------'
        self.state = self.board
        self.winner = None  # { 'O', 'X', 'D' }

        return self.state 
        
    def step(self, action, ox):
        """ put X/O at the location specified by action
            action: a number 0 ~ 9 
            return: state, reward, done, info """
        done = False 
        reward = 0
        info = {}
        if self.state[action] != '-':
            done = True 
            info = {'state' : self.state, 'code': 'bad action: occupied' }
        else:
            self.state = self.state[:action] + ox + self.state[action+1:]

        if self.game_over() == True:
            if self.winner == 'D':
                reward = 0
            else:
                reward = 1
            done = True

        return self.state, reward, done, info 

    def game_over(self,):            
        # Each list corresponds to the values to check to see if a winner is there
        checks = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7] , [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for check in checks:
            # Check to see if the strings have a winner
            test = self.state[check[0]] + self.state[check[1]] + self.state[check[2]]
            if test == 'XXX':
                self.winner = 'X'
                # print('>>>', test, self.winner)
                return True
            elif test == 'OOO':
                self.winner = 'O'
                # print('>>>', test, self.winner)
                return True

        if '-' not in self.state:
            """ draw """
            self.winner = 'D'  # draw
            return True 
        return False

    def render(self,):
        for i in range(0, 9, 3):
            print(self.state[i:i+3])
    


# %%
class QAgent():
    def __init__(self):
        # { state: [q1, q2, ..., q9] } where q_n = -inf if action n is impossible.
        # use self.get_Qvalues(state) interface. Do not try to access self.Q directly, because of initialization
        self.Q = {}   ## defaultdict(lambda : np.ones(9)*self.qval_init)   # auto key generation
        self.qval_init = .5
        #
        self.eps = 0.1  # eps-greedy policy
        self.alpha = 0.9
        self.gamma = 1.  # discount factor 
        #
        self.history = []
        pass

    def get_random_action(self, state):
        possible = [i for i, s in enumerate(state) if s == '-']
        chosen = np.random.choice(possible)
        return chosen 

    def get_action(self, state, verbose=False, greedy=False):
        if (greedy == False) and (rng.random() < self.eps):  # eps-greedy policy
            if verbose: 
                print('QAgent(): eps-greedy action')
            action_candidates = [i for i in range(9) if state[i] == '-']
            return rng.choice(action_candidates)
        #

        # Get the q-values for the state
        q_vals = np.round(self.get_Qvalues(state), 5)
        # Get location of all max values and select a random one
        max_q = max(q_vals)
        action_candidates = [i for i, qsa in enumerate(q_vals) if qsa == max_q]
        action = np.random.choice(action_candidates)
        if verbose: print(action, 'action_cand: ', action_candidates, q_vals, max_q)
        return action  # the  place to put 'O' or 'X"

    def get_Qvalues(self, state):
        if state not in self.Q.keys():
            values = np.array([self.qval_init if bar == '-' else float('-inf') for bar in state])
            self.Q[state] = values  # register a new action-values
        return self.Q[state]

    def qlearn(self, state, action, reward, new_state, done):
        qsa = self.get_Qvalues(state)[action]  ## self.Q[state][action]  # Q(S,A)
        pred = reward
        if not done:
            max_a = max(self.get_Qvalues(new_state))
            pred += self.gamma * max_a
        #
        self.Q[state][action] += self.alpha * (pred - qsa)   # Q-learning or TD(0)
#


class Player:
    def __init__(self, xo, agent):
        self.xo = xo  # 'X' or 'O'
        self.agent = agent
        self.started = False 
        pass

    def get_action(self, state, greedy=False):
        self.state = state 
        self.action =  self.agent.get_action(state, greedy=greedy)
        self.update()
        return self.action

    def update(self,):
        self.started = True 

    def qlearn(self, new_state, reward, done):
        self.agent.qlearn(self.state, self.action, reward, new_state, done)
        # self.state = new_state

#
class Game:
    def __init__(self, p1, p2, env):
        self.env = env
        self.p1 = p1  # player 1
        self.p2 = p2  

        self.cp = self.p1  # current player
        self.np = self.p2  # next player

    def reset(self,):
        self.cp = self.p1  # current player; X goes first always
        self.np = self.p2  # next player
        self.state = env.reset()
        pass 

    def run(self, greedy=False, learn=True, verbose=False):
        done = False 
        while not done:
            action = self.cp.get_action(self.state, greedy=greedy)
            new_state, reward, done, info = self.env.step(action, self.cp.xo)

            if verbose:
                print(self.cp.xo, self.state, action, reward, new_state, done)

            if done:
                self.cp.qlearn(new_state, reward, done)
                self.np.qlearn(new_state, -reward, done)  # lost, reward = -1
                break 

            if self.np.started:  # this is not the first move
                self.np.qlearn(new_state, reward, done)
            else: 
                self.np.update()  # record current state

            self.state = new_state   # transition

            # swap cp & np
            imsi = self.cp 
            self.cp = self.np 
            self.np = imsi 
        return self.env.winner
#

import pickle
nepisodes = 100000
filename = f'qagent_{nepisodes}.pkl' 

def train():
    # we need two players to play the game
    env = EnvTTT()

    qagent = QAgent()
    player1 = Player('X', qagent)
    player2 = Player('O', qagent)

    game = Game(player1, player2, env)

    winner = []
    for _ in trange(1, nepisodes+1):
        game.reset()
        w = game.run() 
        winner.append(w)
    #

    winner = np.array(winner)
    print('@stats: {X O D}', sum(winner == 'X')/nepisodes, sum(winner == 'O')/nepisodes, sum(winner == 'D')/nepisodes)

    for _ in range(3):
        game.reset()
        w = game.run(greedy=True, verbose=True)
        print('@ Winner: ', w)

    # save Q-Agent
    with open(filename, 'wb') as f:
        pickle.dump(qagent, f)

    print('plotting stats')
    niter = np.arange(1, nepisodes+1)
    x = winner == 'X'
    o = winner == 'O'
    d = winner == 'D'

    x = np.cumsum(x) / niter 
    o = np.cumsum(o) / niter 
    d = np.cumsum(d) / niter 

    # print('plotting')
    plt.plot(x, label='X')
    plt.plot(o, label='O')
    plt.plot(d, label='D')
    plt.legend()
    plt.grid()
    plt.xlabel('nepisodes')
    plt.ylabel('percentage of game result (accumulated)')
    plt.savefig('xod.png')
    print('finished.')

def test():
    # we need two players to play the game
    env = EnvTTT()
    qagent = QAgent()
    with open(filename, 'rb') as f:
        qagent = pickle.load(f)
    # print(qagent.Q)

    done = False 
    state = env.reset()
    while not done:
        env.render()

        s = input('enter row col: ')
        if s == 'q': break 
        r, c = [int(i) for i in s.split()]
        print(r, c)
        action = r * 3 + c 
        state, reward, done, info = env.step(action, 'X')  # human action for 'X'
        env.render()
        print('@+++++++++++++')
        # computer's turn
        action = qagent.get_action(state, verbose=True)
        state, reward, done, info = env.step(action, 'O')
        if done: env.render()

    if env.winner == 'D':
        print('The result is Draw')
    else:
        print('The winner is ', env.winner)
#


if __name__ == "__main__":
    test()