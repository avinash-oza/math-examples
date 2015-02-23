source("../hw1/nla_funcs.R")
payoff_data <- read.csv("~/math_examples/nla/hw4/p9_data.csv")

payoff_matrix <- as.matrix(payoff_data[2:ncol(payoff_data)])
print_latex(payoff_data,digits=6,rownames_on = FALSE)

#           P1200 P1300 P1400 C1400 C1450 C1550 C1600
s_t_0 <- c(51.55,77.70,116.55,71.10,47.25,15.80,7.90)

Q<- solve(payoff_matrix,s_t_0)