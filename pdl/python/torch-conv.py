# filename: torch-conv.py

# See the actions of spatial filters: Sobel, Blur

import torch
import imageio
import matplotlib 
import matplotlib.pyplot as plt
plt.switch_backend ('TkAgg')
import numpy as np

# The weight is set manually to examine its output
class SobelY (torch.nn.Module):
    def __init__(self):
        super(SobelY, self).__init__()
        self.conv = torch.nn.Conv2d (in_channels=1, out_channels=1, kernel_size=3, bias=False)
        print ('self.conv.weight.data.shape = ', self.conv.weight.data.shape)
        self.conv.weight.data = torch.FloatTensor([[-1,-1,-1],[0, 0, 0], [1,1,1]]).reshape(self.conv.weight.data.shape)
        
    def forward(self, x):
        x = self.conv(x)
        return x
#

img = imageio.imread ('imgs/sunflowers.png')
# get red channel
gray = img[:,:,0]
plt.imshow (gray, cmap='gray')
plt.title ('input gray image')
plt.pause(1); plt.close()

# Declare an instance of SobelY network
soby = SobelY()

print (soby)
print ('soby.weight.data: ', soby.conv.weight.data)

# add batch dimension for SobelY()
print (gray.shape)
inp = torch.tensor(gray.astype(np.float32))
inp = inp.reshape(1,1,*inp.shape)
print (inp.shape)

# apply the filter
out = soby(inp)

# we cannot display torch.tensor directly
outnp = out.detach().numpy()
print ('outnp.shape = ', outnp.shape)

# examine the distribution of the outnp
hist, bin_edges = np.histogram (outnp.flatten(), bins=50, density=True)
plt.plot (bin_edges[:-1], hist)
plt.title ('histogram of the SobelY operation')
plt.pause(1); plt.close()

# apply abs() to convert negative values to positive
outnpABS = np.abs(outnp[0,0])

plt.imshow (outnpABS, cmap='gray')
plt.title ('Magnitude image of Y-Gradient (Sobel-Y)')
plt.pause(1); plt.close()


# The weight is set manually to examine its output
class Smoothing (torch.nn.Module):
    '''
    This kernel calculates the average of 9 pixels in the kernel window
    '''
    def __init__(self):
        super(Smoothing, self).__init__()
        self.conv = torch.nn.Conv2d (in_channels=1, out_channels=1, kernel_size=3, bias=False)
        self.conv.weight.data = 1./9. * torch.FloatTensor([[1,1,1],[1,1,1],[1,1,1]]).reshape(self.conv.weight.data.shape)
        
    def forward(self, x):
        x = self.conv(x)
        return x
#

smooth_filter = Smoothing()

outsm = smooth_filter (inp)

# repeat smoothing so that the result shows smoothing effect clearly.
outsm2 = smooth_filter (outsm)
for k in range (20):
    outsm10 = smooth_filter(outsm)

outsm10np = outsm10.detach().numpy()[0,0]
plt.imshow (outsm10np, cmap='gray')
plt.pause(1); plt.close()

print ('input shape: ', inp.shape)
print ('output shape: ', outsm10.shape)
# EOF
