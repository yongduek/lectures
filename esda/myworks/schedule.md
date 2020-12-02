# Schedule

## 1. Bayesian Thinking
- Getting Acquainted with Software Environment
- Interesting Prolblem Solving [TB]
- Thinking with Outcome Table  or Contingency Table [RD]
- Random Simulations
    * How many girls in 400 births? [ROS]
        - $p=0.48$, but what will be the actual sample numbers?
    * Polling rate. How much supported? Simulate the number give a rate and examine the distribution.
- Grid-based Approach for Bayesian Analysis
    * Coming to Earth for Water.
    * [Prior and Posterior Predictive Checks](https://docs.pymc.io/notebooks/posterior_predictive.html)
- Probability Models
    * `scipy.stats.*`

## 2. Linear Models
- Linear Regression with One Predictor Variable
    * Gaussian Model of Height- [SR2]
    * Height and Earnings [ROS, p84]
    * Elections and Economy [ROS, p93]
    * Data Nomalization
- Point Estimation vs Density Estimation
    * MLE / MAP estimation for data analysis
    * Parametric vs non-parametric Bayesian Estimation
- LR with Multiple Predictor Variables
    * Kid IQ and Mom [ROS p131]
- Robust Linear Regression [BAP]
- Control vs Treatment
    * [Drug IQ: One treatment vs. one control](https://ericmjl.github.io/bayesian-stats-talk/)
    * [A or B?, Rasmusab](https://www.youtube.com/watch?v=mAUwjSo5TJE)
    * [Smart Drug for IQ](https://docs.pymc.io/notebooks/BEST.html) Bayesian Extimation Supersedes the T-Test.
- Hierarchical (Multilevel) Model Example
    * [The Best of Both Worlds](https://docs.pymc.io/notebooks/GLM-hierarchical.html)
    * [Rat Tumor Example](https://docs.pymc.io/notebooks/GLM-hierarchical-binominal-model.html)

## 3. Generalized Linear Models
- Am I going to earn more than $50,000?
    * [GLM: Logistic Regression, pymc3](https://docs.pymc.io/notebooks/GLM-logistic.html)
- Fancy Mathematics for logistic regression [ROS]
    - Bernoulli, MLE, MAP
- Which species is the iris? [BAP] 
    * Logistic and Softmax for 4 kinds of iris flowers.
- How many fish? [BAP]
    * Poisson Regression
    * Zero-Inflated Poisson Regression
- How often do you sneeze?
    * [GLM:Poisson Regression,pymc3](https://docs.pymc.io/notebooks/GLM-poisson-regression.html)


## References
1. BAP: Bayesian Analysis with Python, 2nnd
1. BCM: Bayesian Cognitive Modeling
1. BDA: Bayesian Data Analysis
1. RD: Reasoning with Data: An Introduction to Traditional and Bayesin Statistics Using R, Jeffrey M. Stanton.
1. ROS: Regression and Other Stories
1. SR2: Statistical Rethinking, (1st or 2nd)
1. TB: Think Bayes
1. [Computational Statistics in Python, Using PyMC3, Duke Univ.](http://people.duke.edu/~ccc14/sta-663-2016/16C_PyMC3.html#Robust-linear-regression)