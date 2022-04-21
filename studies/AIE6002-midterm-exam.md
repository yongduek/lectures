# AIE6002 인공지능확률통계 중간시험 

이름, 학번:

* 반드시 설명 있어야함. 답만 적으면 점수 없음.

1. A fair coin is tossed 10 times. What is the probability that you will have 4 heads?

1. Four-door Monty hall problem. You have four doors instead of three, this time. Given 4 options, you chose door #1, and the show host opened door #4, telling you that it was empty. Now find three probabilities $p_i$ for $i=1,2,3$, where $p_i$ is the posterior probability that the room of the door $i$ has the winning prize.

1. Given $X$ ~ Bernoulli($\theta$), $\theta=0.4$, what is the probability of having 1, 0, 0 from three independent experiments?

1. The prior distribution for $\theta$ is given by $P(\theta) = Beta(\theta | 3,3)$, and the likelihood density for outcome $Y$ is $P(Y|\theta) = Bernoulli(y|\theta)$. What is the joint probability function $P(Y, \theta)$?

1. Given $P(\theta) = Beta(\theta | 3,3)$, $P(Y|\theta) = Bernoulli(y|\theta)$, you did four independent experiments of tossing the coin and obtained $1,0,1,1$. What is the posterior distribution $P(\theta|Y=\{1,0,1,1\})$?

1. For a Gaussian density $p(x) = \mathcal{N}(0, 3^2)$, what is the probability $P[ X \leq 3]$?

1. When $X\sim\mathcal{N}(0,1)$, what is $p(y)$ when $Y=2X+3$?

1. Provided a 2D random vector $X=[X_1, X_2]^T$ with a 2D Gaussian distribution of zero mean and covariance $\Sigma$, find $P[Y > 0]$ where $Y=X_1 + X_2$:

    $$\Sigma = \frac{1}{2}\begin{pmatrix} 25 & -7 \\ -7 & 25\end{pmatrix} $$

1. Let $X\sim U(-1,1)$ and $Y=X^2$. Clearly $Y$ is dependent on $X$. However, show that the correlation coefficient $\rho(X,Y)=0$. The general definition of $\rho$ is given as follows:

    $$ \rho(X,Y) = \frac{Cov[X,Y]}{\sqrt{Var[X] Var[Y]}}$$

1. Given a Linear Gaussian System:
    $$
    \begin{align}
        p(z) & =  \mathcal{N}(z|\mu_z, \Sigma_z) \\
        p(y|z) & =  \mathcal{N}(y|Wz+b, \Sigma_y)
    \end{align}
    $$
    derive the mean $\mu$ and covariance $\Sigma$ of $p(z, y)$ to find the marginal distribution $p(y)$. During the class, we derived $\Sigma^{-1}$ and now its inverse $\Sigma$ is needed. You can use the matrix inversion formula, or you can use your own way of deriving it.

1. (Extra) Suppose $X$, $Y$ are two points sampled independently and uniformly at random from the interval $[0,1]$. What is the expected location of the leftmost point?