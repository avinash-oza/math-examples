source("../hw1/nla_funcs.R")
payoff_data <- read.csv("~/math_examples/nla/hw4/p8_data.csv")
all_strikes <- read.csv("~/math_examples/nla/hw4/p8_all_strikes.csv")

payoff_matrix <- as.matrix(payoff_data[2:ncol(payoff_data)])
print_latex(payoff_data,digits=6,rownames_on = FALSE)

#Strip off the row names

#Part i
inv <- solve(payoff_matrix)
print_latex(inv,digits=9,rownames_on = FALSE,colnames_on = FALSE)
#         P1200 P1275 P1350 P1375 C1375 C1400 C1450 C1550 C1600
s_t_0<- c(51.55,70.15,95.30,105.30,84.9,71.10,47.25,15.80,7.90)

#Part ii
Q <- solve(payoff_matrix,s_t_0)

#Part iii
model_based_prices <- as.matrix(all_strikes[,2: ncol(all_strikes)])%*%Q
strike_to_model_price<- cbind(all_strikes$Op_name,as.data.frame( model_based_prices))
print_latex(strike_to_model_price,digits=9,rownames_on = FALSE)