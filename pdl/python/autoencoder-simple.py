# autoencoder-simple.py
# ref: https://github.com/L1aoXingyu/pytorch-beginner/blob/master/08-AutoEncoder/simple_autoencoder.py

import os
import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
from torchvision.utils import save_image

# cuda ?
device = torch.device ('cuda' if torch.cuda.is_available() else 'cpu')

sample_dir = './data/samples' # AE output will be saved here
if not os.path.exists(sample_dir):
    os.mkdir(sample_dir)

def to_img(x):
    x = 0.5 * (x + 1)
    x = x.clamp(0, 1)
    x = x.view(x.size(0), 1, 28, 28)
    return x

num_epochs = 10 # You should increase this probably.
batch_size = 128
learning_rate = 1e-3

# MNIST data set: 
# image size = [28x28] PIL Image
# It is converted to a [1,28,28] tensor by ToTensor()
img_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5]) # mean, std
])

# MNIST data size = 28x28
# len = 60000
dataset = MNIST('./data', transform=img_transform, download=True)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

class autoencoder(nn.Module):
    def __init__(self, input_dim, rep_dim=4):
        super(autoencoder, self).__init__()
        self.rep_dim = rep_dim
        self.nhidden = 128
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, self.nhidden), nn.ReLU(True),
            nn.Linear(self.nhidden, self.rep_dim))
        self.decoder = nn.Sequential(
            nn.Linear(self.rep_dim, self.nhidden), nn.ReLU(True),
            nn.Linear(self.nhidden, input_dim), 
            nn.Tanh()) # The input values are transfomred into the range [-1,1]

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

    def encode (self, x):
        feat = self.encoder(x)
        return feat
#

input_dim = 28*28
rep_dim   = 4

model = autoencoder(input_dim, rep_dim=rep_dim).to(device)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(
    model.parameters(), lr=learning_rate, weight_decay=1e-5)

for epoch in range(num_epochs):
    for data in dataloader:
        img, _ = data # We don't need labels
        img = img.to(device).view(img.size(0), -1) # [batch, 28*28]
#        img = img.view(img.size(0), -1)
#        img = Variable(img).cuda()
        # ===================forward=====================
        output = model(img)
        loss = criterion(output, img)
        # ===================backward====================
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    # ===================log========================
    print('epoch [{}/{}], loss:{:.4f}'
          .format(epoch + 1, num_epochs, loss.item()))
    if epoch % 10 == 0: # every time
        pic = to_img(output.cpu().data)
        save_image(pic, sample_dir + '/image_{}.png'.format(epoch))
#
torch.save(model.state_dict(), './data/autoencoder-simple.pth')


# EOF