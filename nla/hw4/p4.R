source("../hw1/nla_funcs.R")

M <- matrix(c(60,40,0,10),ncol=2)
M <- t(M)

#Strip off the row names

s_t_0<- c(50,4)

#Part ii
Q <- solve(M,s_t_0)