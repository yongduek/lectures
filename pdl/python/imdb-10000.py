# imdb-10000.py
# 

import os
import torch 
import numpy as np 
# download the http://mng.bz/0tIo 

imdb_dir = '/home/yndk/.data/imdb/aclImdb'
train_dir =  os.path.join(imdb_dir, 'train')
print ('train data is in ', train_dir, '\n', os.listdir(train_dir))

labels = []
texts = []
fnames = []
for labeltype in ['neg', 'pos']:
    dirname = os.path.join(train_dir, labeltype)
    # print ('dirname: ', dirname, os.listdir(dirname))
    for fname in os.listdir (dirname):
        filepath = os.path.join(dirname, fname)
        fnames.append (filepath)
        if fname[-4:] == '.txt':
            with open (filepath) as f:
                texts.append (f.read())
            labels.append( 0 if labeltype == 'neg' else 1 )
#

print(len(labels), len(texts), labels[0], '\n', texts[0], '\n', fnames[0])

textlenths = np.array([len(text) for text in texts])
print ('max/min text length = ', textlenths.max(), textlenths.min())

# tokenizer: string -> set of words
# we use the simplest tokenizer
special = ['<pad>', '<sos>', '<eos>', '<unknown>']
vocab = set()
for text in texts:
    vocab.update (text.split())
print ('length of vocab: ', len(vocab))

word_index = { w: i for i, w in enumerate(special) }
word_index.update([ (w, i+len(special)) for i, w in enumerate(vocab) ])
print ('len(word_index) = ', len(word_index))
print ('word_index[\'<pad>\'] = ', word_index['<pad>'])
#print (word_index, type(word_index))

i2w = { i : w for w, i in word_index.items() }
print ('i2w = ', i2w[0], i2w[1], i2w[2], i2w[3])

# One of the simplest way of text feature vector is one-hot encoding, 
# where the position of a word has 1, otherwise 0.

# x = onehot_features (texts, word_index) # 2D [ndata, nfeature]
ndata = len(texts)
nfeatures = len(word_index)
# data = np.zeros ( (ndata, nfeatures), dtype=np.float32)
# well, this caused a memory error. We have to reduce the size of feature dimension
# We will use 10000 words, which we have to choose them among the vocab.

nfeatures = 10000

import collections

counter = collections.Counter()
for text in texts:
    counter.update (text.split())
most_common = counter.most_common (nfeatures - len(special))
print (most_common[:10])

# rebuild word_index & i2w
word_index = { w: i for i, w in enumerate(special) }
for w, cnt in most_common:
    word_index[w] = len(word_index)
#
i2w = { i : w for w, i in word_index.items() }
#print ('i2w = ', i2w[0], i2w[1], i2w[2], i2w[3])
#print ('new word_index: ', word_index, len(word_index))

data = np.zeros ( (ndata, nfeatures), dtype=np.float32)

# build one-hot encoding
for i, text in enumerate(texts):
    for w in text.split(): # tokenize
        w_index = word_index[w] if w in word_index else word_index['<unknown>']
        data[i, w_index] = 1
#       
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = np.asarray(labels)[indices]

# separate training data and validation data
ntrains = int(0.75 * data.shape[0])
x_train = data[:ntrains]
y_train = labels[:ntrains]
x_val = data[ntrains:]
y_val = data[ntrains:]

# NN model

model = torch.nn.Sequential(
    torch.nn.Linear(nfeatures, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 1),
    torch.nn.Sigmoid()
)

# sanity check
yhat = model (torch.tensor(data[:2]))
print (yhat)

# dataset & dataloader

# training
def train(nepochs, model, dl):
    # do training
    return