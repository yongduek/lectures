# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # TicTacToe Game & Tabular Q Learning

# %%
import numpy as np
import matplotlib.pyplot as plt 
from collections import defaultdict  

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
    def __init__(self, ox):
        self.ox = ox 
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

    def get_action(self, state, verbose=False):
        if rng.random() < self.eps:  # eps-greedy policy
            action_candidates = [i for i in range(9) if state[i] == '-']
            return rng.choice(action_candidates)
        #

        # Get the q-values for the state
        q_vals = np.round(self.get_Qvalues(state), 7)

        # Get location of all max values and select a random one
        max_q = max(q_vals)
        action_candidates = [i for i, qsa in enumerate(q_vals) if qsa == max_q]
        action = np.random.choice(action_candidates)
        if verbose: print(action, 'action_cand: ', action_candidates, q_vals, max_q)
        return action  # the  place to put 'O' or 'X"

    def get_Qvalues(self, state):
        if state not in self.Q.keys():
            values = np.array([self.qval_init if ox == '-' else float('-inf') for ox in state])
            self.Q[state] = values  # register a new action-values
        return self.Q[state]

    def q_update(self, state, action, reward, new_state, done):
        qsa = self.get_Qvalues(state)[action]  ## self.Q[state][action]  # Q(S,A)
        pred = reward
        if not done:
            max_a = max(self.get_Qvalues(new_state))
            pred += self.gamma * max_a
        #
        self.Q[state][action] += self.alpha * (pred - qsa)   # Q-learning or TD(0)


# %%
env = EnvTTT()

# %% [markdown]
# ## Test running of the environment

# %%
def run(agents, update=False):
    done = False
    state = env.reset()
    print('initial state: ', state)
    while not done:
        action = agents[0].get_random_action(state)
        state, reward, done, info = env.step(action, agents[0].ox)
        print(f'Turn: {agents[0].ox}, A: {action}, S: {state}, R: {reward}')
        # env.render()

        if done: 
            break 

        action = agents[1].get_random_action(state)
        state, reward, done, info = env.step(action, agents[1].ox)
        print(f'Turn: {agents[1].ox}, A: {action}, S: {state}, R: {reward}')
        # env.render()
        
    print(f'Winner: {env.winner}')
    env.render()


# %%
# we need two agents to play the game
agents = [QAgent('X'), QAgent('O')]

run(agents)


# %%
# without learning, Q table is empty
agents[0].Q


# %%
def run_X(agents, verbose=True):
    done = False
    state = env.reset()
    init = True 
    if verbose:
        print('initial state: ', state)
    while not done:
        # X-turn
        action = agents[0].get_action(state, verbose)
        new_state0, reward, done, info = env.step(action, agents[0].ox)
        if verbose: print(f'Turn: {agents[0].ox}, A: {action}, S: {new_state0}, R: {reward}')
        # env.render()

        if init  == False:
            agents[1].q_update(new_state0p, action1, reward, new_state0, done)
        else:
            init = False 

        if done: 
            agents[0].q_update(state, action, reward, new_state0, done)  # if game is over (X won), then update
            break 

        # O-turn
        new_state0p = new_state0  # copy for update later
        action1 = agents[1].get_action(new_state0p)
        new_state1, reward, done, info = env.step(action1, agents[1].ox)
        if verbose: print(f'Turn: {agents[1].ox}, A: {action1}, S: {new_state1}, R: {reward}')
        # env.render()

        # Now, the opponant finished its move. Update.
        agents[0].q_update(state, action, reward, new_state1, done)

        state = new_state1 

        if done:
            agents[1].q_update(new_state0p, action1, reward, new_state1, done) 
            break 

    if verbose: print(f'Winner: {env.winner}')

    if verbose: env.render()

    return env.winner  
#

def get_winstats(wins, nview=1000):
    wins = np.array(wins[-nview:])
    return {oxd: np.round(sum(wins == oxd)/nview,3) for oxd in ['X', 'O', 'D']}

# %%
run_X(agents)

wins = []
niters = 1000000
for n in range(1, niters):
    wins.append(run_X(agents, verbose=False))
    if n % 1000 == 0:
        print(f'@ wins @ n:{n} = {get_winstats(wins)}')
        # run_X(agents)


run_X(agents)