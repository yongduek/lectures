# AIE6002 인공지능확률통계 중간시험 

이름, 학번:

* 반드시 설명을 적으세요.

1. A fair coin is tossed 4 times. What is the probability that you will have 4 heads?

1. Four-door Monty hall problem. You have four doors instead of three, this time. Given 4 options, you chose door #1, and the show host opened door #4, telling you that it was empty. Now find three probabilities $P_i = P[$ room $i$ has prize $]$, for each of $i=1,2,3$, the posterior probability that the room of the door $i$ has the winning prize.

1. Given $X$ ~ Bernoulli($\theta$), $\theta=0.4$, what is the probability of having 1, 0, 0, 1, 0 from three independent experiments?

1. Kim is a lab member in AI Lab, asked to write a paper accepted to CVPR, which is one of the most hilarious conferences in the world. The statistics is that a paper is accepted with probability 1/2 every year independent of past submission results. Because she is a pro-player in LOL, she can prepare only one submission a year. Unfortunately, she failed last year. Given this, let $Y$ be the additional number of submissions Kim prepares before her getting an acceptance letter from the conference. What is the expected number of additional submissions until success: $\mathbb{E}(Y)$?


1. Suppose $\theta\sim Beta(a,b)$, where $a>1$ and $b>1$. Show that
    $$
    \begin{align}
        \mathbb{E}(\theta) &= \frac{a}{a+b} \\
        mode[\theta]       &= \frac{a-1}{a+b-2}
    \end{align}
    $$
    
1. After your yearly checkup, the doctor has bad news and good news. The bad news is that you tested positive for a vampire disease, and that the test is 99% accurate (i.e., the probability of testing positive given that you have the disease is 0.99, as is the probability of testing negative given that you don't have the disease). The good news is that this is a rare disease, striking only one in 10,000 people. (1) What are the chances that you actually have the disease? (Show your calculations as well as giving the final result.) Since it was unbelievable, you went through an additional test and got positive. (2) Now what is the probability?  Well, you tried again and tested negative finally. (3) What is the final posterior probability?

1. Suppose $X$, $Y$ are two points sampled independently and uniformly at random from the interval $[0,3]$. What is the expected location of the leftmost point?


1. When $X\sim\mathcal{N}(0,4)$, what is $p(y)$ when $Y=2X+3$?

1. Provided a 2D random vector $X=[X_1, X_2]^T$ with a 2D Gaussian distribution of zero mean and covariance $\Sigma$, find $P[Y > 0]$ where $Y=X_1 + X_2$:

    $$\Sigma = \frac{1}{2}\begin{pmatrix} 25 & -7 \\ -7 & 25\end{pmatrix} $$

1. Let $X\sim U(-1,1)$ and $Y=X^2$. Clearly $Y$ is dependent on $X$. However, show that the correlation coefficient $\rho(X,Y)=0$. The general definition of $\rho$ is given as follows:

    $$ \rho(X,Y) = \frac{\mathrm{Cov}[X,Y]}{\sqrt{Var[X] Var[Y]}}$$

1. Given a Linear Gaussian System:
    $$
    \begin{align}
        p(z) & =  \mathcal{N}(z|\mu_z, \Sigma_z) \\
        p(y|z) & =  \mathcal{N}(y|Wz+b, \Sigma_y)
    \end{align}
    $$
    derive the mean $\mu$ and covariance $\Sigma$ of $p(z, y)$ to find the marginal distribution $p(y)$. During the class, we derived $\Sigma^{-1}$ and now its inverse $\Sigma$ is needed. You can use the matrix inversion formula, or you can use your own way of deriving it.

1. $Y\sim Bernoulli(\theta)$ and $\theta$ is a discrete random varaible with its PMF $P(\theta=0.6)=0.5$ and $P(\theta=0.3)= 0.5$. Through independent random experiments you obtained observations $1, 1, 0$ of $Y$. Compute the posterior PMF $P[\theta|Y=\{1,1,0\}]$.

