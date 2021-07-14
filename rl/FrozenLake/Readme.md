# FrozenLake

- Non-slippery is solved by q-learning.
- Slippery case did not work with q-learning. Do some hyper-parameter search?
- Dynamic programming can solve the problem, but $P$ is required.
    - Policy Iteration 
    - P may be estimated: `01_frozenlake_v_iteration.py` and `02_frozenlake_q_iteration.py`