# TTT with Tabular Q learning

```
python q_learning2.py
```

The command will start a TTT game for you against q-learning agent.

- If you want to train, then set the varaible `nepisodes` and chante `test()` to `train()` in the python file.

## Discussion

1. On-policy Q learning is data inefficient. The propagation of the final reward back to the action-value at the early stage states takes long time. This can be seen by looking at the action values at the last action just before the game. For example,
```
enter row col: 0 1
0 1
OX-
OXX
---
@+++++++++++++
6 action_cand:  [6] [   -inf    -inf 0.15767    -inf    -inf    -inf 0.28145 0.19567 0.16274] 0.28145
OX-
OXX
O--
The winner is  O
```
The Q value at action=6 is only .28, which must be 1 since it finishes the game right away.

2. Game history may be reserved and q-learning backward after an episode will improve the performance and learning speed.
    - See the code in https://github.com/sunbri/tictactoe, where an episode history is saved and learned backwards so that the update of the q table may be the most effective. But note that this is only possible for an episodic case like ttt game.