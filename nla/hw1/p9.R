source("nla_funcs.R")

omega <- matrix(c(1,-0.525,1.375,-0.075,-0.75,
                  -0.525,2.25,.1875,.1875,-0.675,
                  1.375,0.1875,6.25,0.4375,-1.875,
                  -0.075,0.1875,0.4375,0.25,0.3,
                  -0.75,-0.675,-1.875,0.3,0),nrow = 5,ncol = 5)
#Calculate covariance matrix
corr_vector = sqrt(c(1,2.25,6.25,0.25,9))
correlation_calc(corr_vector, omega)

