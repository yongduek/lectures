# filename: lstm_pos_tagging.py
# ref: https://raw.githubusercontent.com/pytorch/tutorials/master/beginner_source/nlp/sequence_models_tutorial.py
# Author: Robert Guthrie

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

######################################################################
# Example: An LSTM for Part-of-Speech Tagging

training_data = [  # (sentence, tag_seq)
    ("The dog ate the apple".split(),    ["DET", "NN", "V", "DET", "NN"]),
    ("Everybody read that book".split(), ["NN", "V", "DET", "NN"])
]

print ('training_data: ', len(training_data))
for i in range(len(training_data)):
    print ('training_data[{}] = {}'.format(i, training_data[i]))


def prepare_sequence(seq, to_ix):
    idxs = [to_ix[w] for w in seq]
    return torch.tensor(idxs, dtype=torch.long)

word_to_ix = {}
for sent, tags in training_data:
    for word in sent:
        if word not in word_to_ix:
            word_to_ix[word] = len(word_to_ix)

print('word_to_ix = ', word_to_ix)

tag_to_ix = {"DET": 0, "NN": 1, "V": 2}  # hand-made , simple data

# These will usually be more like 32 or 64 dimensional.
# We will keep them small, so we can see how the weights change as we train.
EMBEDDING_DIM = 6 # word to Euclidean Embedding dimension
HIDDEN_DIM = 7    # LSTM hidden/output dimension

######################################################################
# Create the model:

class LSTMTagger(nn.Module):

    def __init__(self, embedding_dim, hidden_dim, vocab_size, tagset_size):
        super(LSTMTagger, self).__init__()
        self.hidden_dim = hidden_dim

        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)

        # The LSTM takes word embeddings as inputs, and outputs hidden states
        # with dimensionality hidden_dim.
        self.lstm = nn.LSTM(embedding_dim, hidden_dim)

        # The linear layer that maps from hidden state space to tag space
        self.hidden2tag = nn.Linear(hidden_dim, tagset_size)
        self.flag = True 
    def forward(self, sentence): # sentence is a LongTensor of indices
        embeds = self.word_embeddings(sentence)
        lstm_out, _ = self.lstm(embeds.view(len(sentence), 1, -1)) # [time, batch, infeat]
        tag_space = self.hidden2tag(lstm_out.view(len(sentence), -1)) # [b,f] = [time*batch, outfeat]
        #tag_scores = F.log_softmax(tag_space, dim=1)
        tag_scores = tag_space 

        if self.flag:
            self.flag = False
            print (
                'input:      ', sentence.shape, ' (only 1 batch)\n',
                'embeds:     ', embeds.shape, ' -> ', embeds.view(len(sentence),1,-1).shape, '\n',
                'lstm_out:   ', lstm_out.shape, ' -> ', lstm_out.view(len(sentence), -1).shape, '\n',
                'tag_space:  ', tag_space.shape, '\n',
                'tag_scores: ', tag_scores.shape
                )
        return tag_scores

######################################################################
# Train the model:

model = LSTMTagger(EMBEDDING_DIM, HIDDEN_DIM, len(word_to_ix), len(tag_to_ix))
print ('model:\n', model)

#loss_function = nn.NLLLoss()
loss_function = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

# See what the scores are before training
# Note that element i,j of the output is the score for tag j for word i.
# Here we don't need to train, so the code is wrapped in torch.no_grad()
print ('--- before training ---')
with torch.no_grad():
    inputs = prepare_sequence(training_data[0][0], word_to_ix)
    tag_scores = model(inputs)
    print('tag_scores:\n', tag_scores)
    print('target_est: ', torch.argmax(tag_scores, dim=1))
print ('----')

nepochs = 300
for epoch in range(nepochs):  # again, normally you would NOT do 300 epochs, it is toy data
    for sentence, tags in training_data:
        model.zero_grad()

        sentence_in = prepare_sequence(sentence, word_to_ix)
        targets = prepare_sequence(tags, tag_to_ix)

        tag_scores = model(sentence_in)

        # Step 4. Compute the loss, gradients, and update the parameters by
        #  calling optimizer.step()
        loss = loss_function(tag_scores, targets)
        loss.backward()
        optimizer.step()

        if epoch == nepochs//2:
            print (
                'epochs: ', epoch, '\n',
                'sentence: ', sentence, '\n',
                'sentence_in: ', sentence_in.data, '\n',
                'targets: ', targets, '\n',
                'tag_scores (model out):\n', tag_scores.data , '\n',
                ' --- '
            )
# end training loop

# See what the scores are after training
print ('--- after training ---')
with torch.no_grad():
    inputs = prepare_sequence(training_data[0][0], word_to_ix)
    tag_scores = model(inputs)
    print(tag_scores)
    print ('target_est: ', torch.argmax(tag_scores, dim=1))
# EOF
