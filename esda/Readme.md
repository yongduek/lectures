# Introduction to Exploratory & Statistical Data Analysis

- This course introduces fundamental concepts and methods of modern computational statistical data analysis.
- The focus is on computational and exploratory data analysis
- Mainly with python codes with minimal mathematics and equations
- Example oriented or based on synthetic data

- Targeted for people who just learned first steps of python 
- developed for students in Global Korean Studies

Course Target:
- Learn basic approach of statistical thinking
- Sampling based approach (Computational random sampling)
- Basic probability distributions
- Basic Concept of Bayesian data analysis
- Regression analysis
- Null Hypothesis Testing for $z$-test and $t$-test, when time allows.


## Related computational support
- python 3.6 or higher
- Data exploration with `matplotlib`, `seaborne`
- Data manipulation with `numpy`, `torch`, `pandas`
- Probability and Statistics, Computational Approach with `pymc3`
- Machine Learning `scikit learn`, `scipy`


## References
1. [OpenIntro Statistics](https://docs.pymc.io/notebooks/posterior_predictive.html)
1. Regression and Other Stories, Gelman
1. Statistical Rethinking 2ed. McElreath
1. Bayesian Analysis with Python
1. Think Bayes
1. [Think Stats 2ed](https://greenteapress.com/wp/think-stats-2e/)
1. [Khan Acamdemy AP College Statistics](https://www.khanacademy.org/math/ap-statistics/)


## Schedule
1. Introduction to `scipy.stats`
  - uniform distribution & random sampling from U[0,1]
  - Z=X1 + X2 + ... + X100  for Xi ~ U[0,1]
  - Bernoulli, Binomial, Beta
  
2. PMF, CDF, PDF
  - mathematical concepts and definitions of PMF, Expectation, Variance, Standard deviation
  - statistics from computation (OpenIntro Stats)
    - sample mean, std, var, median, quartile, IQR, box plots
  - mass or density?
  - utility functions and random sampling using `scipy.stats`
  
3. Joint probability P(X,Y)
  - contingency table
  - conditional probability  
  - Sum Rule and Product Rule
  
4. Simple survey analysis
  - 12 out of 30, Binomial
  - dependency on p of Binomial
    - is p = 0.5?
  - given multiple assumptions on p, find the probabilty of the outcome.
  
5. Some more problems with Bayesian thinking
  - Think Bayes
  
6. Linear Regression
  - Least-squares estimation
  - Maximum likelihood estimation

7. Topics in LR
  - types of outliers in LR
  - various data manipulation for LR modeling

8. Intermission

9. Linear Regression with Priors
  - intro to pymc3
  - density == set of samples
  - histogram and kernel density estimation (http://faculty.washington.edu/yenchic/18W_425/Lec6_hist_KDE.pdf)
  - data standardization and how to interprete the posterior samples
  
10.LR with outliers, density selection, and multivariate 
  - prior selection
  - multivariate linear models
  - regression with interaction terms
  
11. Overfitting, regularization, information criteria
  - polynomial regression
  - intro to information theory
  - model selection
  
12. introduction to MCMC
  - Metropolis-Hastings
  - Hamiltonian Monte Carlo and NUTS
  
13. GLR: Generalized Linear Regression
  - Classification / Logistic Regression
  - logit transformation, log-odds
  - multinomial/categorical logistic regression, softmax
  
14. GLR examples
  - binomial regression
  - poisson regression
  
15. Mixture models and multi-level models

16. Finalization
---
