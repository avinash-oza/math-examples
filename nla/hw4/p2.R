a <- matrix(c(1,1,1,1,32,38,42,44,0,2,6,8,8,2,0,0), ncol=4)
a<- t(a)
expand(lu(a))$L
expand(lu(a))$U

s = c(0,4,6,6)
c <-solve(a,s)

s_t_0 <- c(1,40,8,5)