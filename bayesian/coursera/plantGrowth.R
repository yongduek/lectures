data('PlantGrowth')
?PlantGrowth

boxplot(weight ~ group, data=PlantGrowth)

## linear model

lmod = lm(weight ~ group, data=PlantGrowth)
summary(lmod)
anova(lmod)


## JAGS model with non-informative prior

library('jags')
mod_string = " model {
  for (i in 1:length(y)) {
    y[i] ~ dnorm(mu[grp[i]], prec)
  }
  for (j in 1:3) {
    mu[j] ~ dnorm(0., 1/1.e6) 
  }
  prec ~ dgamma(5/2., 5*1./2.)
  sig = sqrt(1./prec)
} "

set.seed(82)
str(PlantGrowth)

data_jags = list(y=PlantGrowth$weight,
                 grp=as.numeric(PlantGrowth$group))
params = c('mu', 'sig')

mod = jags.model(textConnection(mod_string), data=data_jags,
                 n.chains=3)

update(mod,1e3)  ## run 1000 iterations burn-in

mod_sim = coda.samples(model=mod,
                       variable.names=params,
                       n.iter=5e3)

mod_csim = as.mcmc(do.call(rbind, mod_sim))  ## combine the samples

## diagnostic
plot(mod_sim)  ## trace plot, visualize
gelman.diag(mod_sim)  ## 1
autocorr.diag(mod_sim)  ## good
effectiveSize(mod_sim)  ## almost 5000 x 3

## calculate posterior mean of the parameters

pm_parameters = colMeans(mod_csim)  ## column mean
print(pm_parameters)

coefficients(lmod)


## residual analysis
yhat = pm_parameters[1:3][data_jags$grp]
yhat

resid = data_jags$y - yhat

plot(resid)  ## good, no pattern found visually
plot(yhat, resid)  # the first group has a large variance compared to the third one
# this gives you a chance to examine the model of three variances, each for each group

##

summary(mod_sim)
HPDinterval(mod_csim)
HPDinterval(mod_csim, prob=0.91)


##  Prob[mu_3 > mu_1]
head(mod_csim)
mean(mod_csim[,3] > mod_csim[,1])

## Suppose the treatment 2 would be costly, and t2 is supposed to have 10% more yield
## Prob[mu_3 > mu_1*1.1]
mean(mod_csim[,3] > 1.1*mod_csim[,1])
# -> result is 0.49, almost 50:50 odds, adopting tr2 will increase the mean yield of the plants by at least 10%


###################################################
##  Separate Variance for each of the three groups
###################################################

## JAGS model with non-informative prior

mod_string3 = " model {
  for (i in 1:length(y)) {
    y[i] ~ dnorm(mu[grp[i]], prec[grp[i]])
  }
  for (j in 1:3) {
    mu[j] ~ dnorm(0., 1/1.e6) 
  }
  for (k in 1:3) {
    prec[k] ~ dgamma(5/2., 5*1./2.)
    sig[k] = sqrt(1./prec[k])
  }
} "

set.seed(82)
str(PlantGrowth)

mod3 = jags.model(textConnection(mod_string3), 
                  data=data_jags,
                  n.chains=3)

update(mod3,1e3)  ## run 1000 iterations burn-in

mod_sim3 = coda.samples(model=mod3,
                       variable.names=params,
                       n.iter=5e3)

mod_csim3 = as.mcmc(do.call(rbind, mod_sim3))  ## combine the samples

## diagnostic
plot(mod_sim3)  ## trace plot, visualize
gelman.diag(mod_sim3)  ## 1
autocorr.diag(mod_sim3)  ## good
effectiveSize(mod_sim3)  ## almost 5000 x 3

## calculate posterior mean of the parameters

pm_parameters3 = colMeans(mod_csim3)  ## column mean
print(pm_parameters3)

coefficients(lmod)  # to compare

## residual analysis
yhat3 = pm_parameters[1:3][data_jags$grp]
yhat3

resid3 = data_jags$y - yhat3

plot(resid3)  ## good, no pattern found visually
plot(yhat3, resid3)  # the first group has a large variance compared to the third one
# this gives you a chance to examine the model of three variances, each for each group

##

summary(mod_sim3)
HPDinterval(mod_csim3)
HPDinterval(mod_csim3, prob=0.91)


##  Prob[mu_3 > mu_1]
head(mod_csim3)
mean(mod_csim3[,3] > mod_csim3[,1])

## Suppose the treatment 2 would be costly, and t2 is supposed to have 10% more yield
## Prob[mu_3 > mu_1*1.1]
mean(mod_csim3[,3] > 1.1*mod_csim3[,1])
# -> result is 0.49, almost 50:50 odds, adopting tr2 will increase the mean yield of the plants by at least 10%



####
head(mod_csim)
dmu31 = mod_csim[,3] - mod_csim[,1]
HPDinterval(dmu31, prob=.95)
# -> the interval contains 0, indicating that the data lack strong evidence for mu3 being not equal to m1.