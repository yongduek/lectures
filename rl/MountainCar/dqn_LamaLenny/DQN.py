import numpy as np
import torch
import torch.optim as optim
import torch.nn.functional as F
import copy
from model import Model


class DQN:
    def __init__(self, state_dim, action_dim, device, GAMMA):
        self.device = device
        self.GAMMA = GAMMA
        self.network = Model(state_dim, action_dim).to(self.device)
        self.target_network = copy.deepcopy(self.network).to(self.device)
        self.optimizer = optim.Adam(self.network.parameters(), lr=5e-4)

    def update(self, batch):
        states, actions, rewards, next_states, dones = zip(*batch)
        states = torch.from_numpy(np.array(states)).float().to(self.device)
        actions = torch.from_numpy(np.array(actions)).to(self.device).unsqueeze(1)
        rewards = torch.from_numpy(np.array(rewards)).float().to(self.device).unsqueeze(1)
        next_states = torch.from_numpy(np.array(next_states)).float().to(self.device)
        dones = torch.from_numpy(np.array(dones)).to(self.device).unsqueeze(1)

        with torch.no_grad(): # Double DQN  
            argmax = self.network(next_states).detach().max(1)[1].unsqueeze(1)
            target = rewards + (GAMMA * self.target_network(next_states).detach().gather(1, argmax))*(~dones)

        Q_current = self.network(states).gather(1, actions)
        self.optimizer.zero_grad()
        loss = F.mse_loss(target, Q_current)
        loss.backward()
        self.optimizer.step()

    def act(self, state):
        state = torch.tensor(state).to(self.device).float()
        with torch.no_grad():
            Q_values = self.network(state.unsqueeze(0))
        return np.argmax(Q_values.cpu().data.numpy())

    def update_target(self):
        self.target_network = copy.deepcopy(self.network)
