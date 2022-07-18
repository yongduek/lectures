# AIE6002 인공지능확률통계 기말시험 

이름, 학번:

* 반드시 설명을 적으세요.
* 10 points each.
* (For problems 1 & 2) Given a Linear Gaussian System:
$$
\begin{align}
    p(z) & =  \mathcal{N}(z|\mu_z, \Sigma_z) \\
    p(y|z) & =  \mathcal{N}(y|Wz+b, \Sigma_y)
\end{align}
$$

1. Derive the mean $\mu$ and covariance $\Sigma$ of $p(z, y)$.
   
6. Find the marginal distribution $p(y)$ based on the result of Problem 2. 
   
7. $Y\sim Bernoulli(\theta)$ and $\theta$ is a discrete random varaible with its PMF $P(\theta=0.6)=0.5$ and $P(\theta=0.3)= 0.5$. Through independent random experiments you obtained observations $1, 1, 0$ of $Y$. 
   - Compute the posterior PMF $P[\theta|Y=\{1,1,0\}]$.

8. You are given the observation $N_0=3$ and $N_1=7$ from 10 times independent experiments of Bernoulli distribution $Bernoulli(\theta)$ where $\theta$ denotes $P[Y=1|\theta]$ and the prior distribution is $Beta(a=11, b=9)$. 
   1. Find the MAP estimate of the posterior 
   2. and Laplace approximation of the posterior distribution $p(\theta | N_0=3, N_1=7)$.
   
9.  You have an observation $y=3$ from a Gaussian distribution $\mathcal{N}(\mu, \sigma^2)$; you know $\sigma^2=4$ but you do not know the value of $\mu$. From our bureau of information, you are told that the prior for $\mu$ is $\mathcal{N}(0, 4)$.
    -  What is the posterior distribution $p_9(\mu|y)$ of $\mu$ given the data $y$? 
  
10. You are going to apply ELBO maximization to obtain an approximation $q(\mu | \phi, \lambda^{-1})$ of the exact posterior $p_9(\mu|y)$; here $\phi$ is the mean of $q()$ and $\lambda$ is the precision of $q()$.
    - Find ELBO which is a function of $\phi$ and $\lambda$.

11. Find the optimal values for $\phi$ and $\lambda$ in Problem 10.

1. When $X\sim\mathcal{N}(0,4)$, what is $p(y)$ when $Y=2X+3$?

1. Provided a 2D random vector $X=[X_1, X_2]^T$ with a 2D Gaussian distribution of mean $\mu$ and covariance $\Sigma$, find $P[Y > 2]$ where $Y=X_1 + X_2$:

    $$ \mu = [2, 0]^T $$
    $$\Sigma = \begin{pmatrix} 25 & 0 \\ 0 & 25\end{pmatrix} $$

1. Let $X\sim U(-1,1)$ and $Y=X^2$. Clearly $Y$ is dependent on $X$. However, show that the correlation coefficient $\rho(X,Y)=0$. The general definition of $\rho$ is given as follows:
    $$ \rho(X,Y) = \frac{\mathrm{Cov}[X,Y]}{\sqrt{Var[X] Var[Y]}}$$

* Good luck!