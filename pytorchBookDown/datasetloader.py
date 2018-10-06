
import numpy as np
import torch
from matplotlib import pyplot as plt
from torch.utils.data import Dataset


class myDataSet (Dataset):
    def __init__ (self, x, y, transform=None):
        self.x = x
        self.y = y
        self.transform = transform
        self.size = x.shape[0]
    def __len__ (self):
        return self.size
    def __getitem__ (self, idx):
        xi = x[idx]
        yi = y[idx]
        if self.transform:
            yi = self.transform (yi)
        return xi, yi
#

class add_num(object):
    """ add a constant number to the input data """

    def __init__(self, num):
        self.num = num

    def __call__(self, sample):
        return sample + self.num
#
class add_2(object):
    """ simply add 2 to the object """
    def __call__(self, sample):
        res = sample + 2.

        #print ('add_2: sample={}  output={}'.format(sample), res)
        return res
#
class ToTensor(object):
    def __call__(self, sample):
        return torch.from_numpy(sample)
#

ndata = 100
x = np.random.rand(ndata,1).astype(np.float32)
y = 3 * x + 5 + np.random.randn(ndata,1).astype(np.float32)*0.5
print ('data generated: ', x.shape, y.shape)

import torchvision
composed = torchvision.transforms.Compose([add_num(3), add_2(), ToTensor()])
dataset = myDataSet (x, y, composed)

for i, (xi, yi) in enumerate(dataset):
    print ('{}: y[{}] = {},  yi={}'.format(i, i, y[i][0], yi.item()))
    print ()
#    print (y[i] - yi.item())
