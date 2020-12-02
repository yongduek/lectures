#
# Q. which of the variables are related to calcium oxalate crystals (COC)
#
library('boot')
data('urine')
?urine
head(urine)
tail(urine)

## remove missing values
dat = na.omit(urine)
dim(dat)
pairs(dat)
# some variables show high correlation
# -> we have to deal with the collinearity between the predictors
# == variable selection (determine which variable relates to the response)

# design matrix

X = scale(dat[,-1], center=TRUE, scale=TRUE)  # -1, omit the first column which is the response
head(X)
colMeans(X) ## should be close to zero

apply(X, 2, sd) # sd to second axis (column axis)


library('rjags')
mod1_string = " model {
  for (i in 1:length(y)) {
    y[i] ~ dbern(p[i])
    
    logit(p[i]) = int + b[1]*gravity[i] + b[2]*ph[i] + b[3]*osmo[i] + b[4]*cond[i] + b[5]*urea[i] + b[6]*calc[i]
  }
  
  int ~ dnorm(0, 1./25.)
  for (j in 1:6) {
    b[j] ~ ddexp(0, sqrt(2)) # var=1.0
  }
} "

set.seed(92)
head(X)
data_jags = list(y=dat$r, 
                 gravity=X[,'gravity'],
                 ph=X[,'ph'],
                 osmo=X[,'osmo'],
                 cond=X[,'cond'],
                 urea=X[,'urea'],
                 calc=X[,'calc'])

params=c('int', 'b')

mod1 = jags.model(textConnection(mod1_string),
                  data=data_jags,
                  n.chains=3)
update(mod1, 1000)

mod1_sim = coda.samples(model=mod1,
                        variable.names = params,
                        n.iter=5000)

mod1_csim = as.mcmc(do.call(rbind, mod1_sim))
head(mod1_csim)

## convergence diagnositics
plot(mod1_sim, ask=TRUE)

gelman.diag(mod1_sim)
autocorr.diag(mod1_sim)
autocorr.plot(mod1_sim)
effectiveSize(mod1_sim)

## calculate DIC
dic1 = dic.samples(mod1, n.iter=1000)
dic1

par(mfrow=c(3,2))
densplot(mod1_csim[,1:6], xlim=c(-3,3))
colnames(X)
