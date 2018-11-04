

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import numpy as np
import matplotlib.pyplot as plt


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

batch_size = 64
test_batch_size = 1000
epochs = 10
lr = 0.01
momentum = 0.5
seed = 1
use_cuda = False
log_interval = 10

torch.manual_seed(seed)

device = torch.device("cuda" if use_cuda else "cpu")
print ('device = ', device)

train_dataset_org = datasets.MNIST('./data', train=True)
train_dataset_ToTensor = datasets.MNIST('./data', train=True,
                                       transform=transforms.Compose([transforms.ToTensor()]))

mean = 0.1307
std  = 0.3081
train_dataset = datasets.MNIST('./data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ]))

train_loader = torch.utils.data.DataLoader(train_dataset,
                  batch_size=batch_size, shuffle=True)
#

test_dataset = datasets.MNIST('../data', train=False, transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ]))

test_loader = torch.utils.data.DataLoader(test_dataset,
                  batch_size=test_batch_size, shuffle=True)
#

model = Net().to(device)
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)


print ('len(train_dataset) = ', len(train_dataset), 'len(test_dataset)= ', len(test_dataset))

# orignal data info.
img0, _ = train_dataset_org[0]
print ('origninal image shape: ', np.array(img0).shape)
npimg0 = np.array(img0)
rows, cols = npimg0.shape
#print ('org: ', npimg0[10:15,10:12]) # [0,255] gray scale image

# data after ToTensor: shape=(C,W,H), values in [0,1]
img, label = train_dataset_ToTensor[0]
npimg = np.array(img)
print ('image shape with ToTensor(): ', npimg.shape, label)
npimg = npimg.reshape((npimg.shape[1],npimg.shape[2]))
print ('image shape for gray scale display: ', npimg.shape)
#print ('scaled: ', npimg, npimg[10:15,10:12]) # [0,1] scaled by ToTensor()
plt.imshow (npimg, cmap='gray')
plt.show()


# using dataloader
dataiter = iter(train_loader)
images, labels = dataiter.next()
print ('> output of dataiter.next():\n',
'images: ', type(images), images.shape, '\n', 'labels: ', type(labels), 'labels={}'.format(labels))
#print (images[0][0])

fig, axes = plt.subplots(2,5)
for i, ax in enumerate(axes.ravel()):
    npimg = images[i].numpy().reshape(rows,cols) * std + mean
    ax.imshow(npimg, cmap='gray')
    ax.set_title (str(labels[i].item()))
print ('type(img) = ', type(images[i]), images[i].shape, '-->', npimg.shape)
#print ('scaled to original [0,1]', npimg)
plt.show()


def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item() # sum up batch loss
            pred = output.max(1, keepdim=True)[1] # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))
#

def learn(epochs):
    #
    for epoch in range(1, epochs + 1):
        train(model, device, train_loader, optimizer, epoch)
        test(model, device, test_loader)
#

learn (1)

