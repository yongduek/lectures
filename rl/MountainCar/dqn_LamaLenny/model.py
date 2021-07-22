import torch.nn as nn

class Model(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        lin1 = nn.Linear(state_dim,64)
        nn.init.xavier_normal_(lin1.weight)

        lin2 = nn.Linear(64, 64)
        nn.init.xavier_normal_(lin2.weight)

        lin3 = nn.Linear(64, action_dim)
        nn.init.xavier_normal_(lin3.weight)

        self.layers = nn.Sequential(lin1, nn.ReLU(), lin2, nn.ReLU(), lin3)

    def forward(self, x):
        return self.layers(x)
