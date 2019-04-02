# filename: torch-conv-learn.py

# See the actions of spatial filters: Sobel, Blur

import torch
import imageio
import matplotlib 
import matplotlib.pyplot as plt
plt.switch_backend ('TkAgg')
import numpy as np

# The weight is set manually to examine its output
class SobelYFilter (torch.nn.Module):
    def __init__(self):
        super(SobelYFilter, self).__init__()
        self.conv = torch.nn.Conv2d (in_channels=1, out_channels=1, kernel_size=3, bias=False)
        print ('self.conv.weight.data.shape = ', self.conv.weight.data.shape)
        self.conv.weight.data = torch.FloatTensor([[-1,-1,-1],[0, 0, 0], [1,1,1]]).reshape(self.conv.weight.data.shape)
        
    def forward(self, x):
        x = self.conv(x)
        return x
#

# input image
img = imageio.imread ('imgs/sunflowers.png')
# get red channel for experiments
gray = img[:,:,0]
plt.imshow (gray, cmap='gray')
plt.title ('input gray image')
plt.pause(1); plt.close()

# Declare an instance of SobelY network
soby = SobelYFilter()
print (soby)
print ('soby.weight.data: ', soby.conv.weight.data)

# add batch dimension to image data for SobelYFilter()
print (gray.shape)
inp = torch.tensor(gray.astype(np.float32))
inp = inp.reshape(1,1,*inp.shape)
print (inp.shape)
print (inp[:2,:5])
# apply the filter
out = soby(inp)

# we cannot display torch.tensor directly
outp = out.detach()
outnp = outp.numpy()
print ('outnp.shape = ', outnp.shape)

print('outp: ', type(outp), outp[0][0][300:310, 300:320]) # just examine

# For display, apply abs() to convert negative values to positive
outnpABS = np.abs(outnp[0,0])
plt.imshow (outnpABS, cmap='gray')
plt.title ('Magnitude image of Y-Gradient (Sobel-Y)')
plt.pause(1); plt.close()

# Now we train a NN that performs like SobleYFilter
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

target = outp.clone().to(device)
source = inp.clone().to(device)

# NN Model
class SobelYNN (torch.nn.Module):
    def __init__(self):
        super(SobelYNN, self).__init__()
        self.conv = torch.nn.Conv2d (in_channels=1, out_channels=1, kernel_size=3, bias=False)
        
    def forward(self, x):
        x = self.conv(x)
        return x
#

# define NN model
model = SobelYNN().to(device)  # cuda if possible

# define Loss function
criterion = torch.nn.MSELoss()

# define optimizer
optim = torch.optim.Adadelta(model.parameters(), lr=0.01)

# weights before training
print ('model weight before training.\n',
    model.conv.weight.detach())

# training iteration
def train(epochs, losslist):
    for epoch in range(epochs):
        optim.zero_grad()
        output = model (source)
        loss = criterion(target, output); losslist.append (loss.item())
        loss.backward()
        optim.step()
    #
    print ('{} loss = {:.2f}'.format(epochs, loss.item()))
#

loss = []
for i in range (10):
    train(2000, loss)

print ('model weight after training (overfitting!)\n', 
    model.conv.weight.detach())

plt.plot (loss)
plt.title ('loss evolution through epochs')
plt.pause (1)
plt.close()
# EOF
