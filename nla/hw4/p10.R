source("../hw1/nla_funcs.R")
payoff_data <- read.csv("~/math_examples/nla/hw4/p10_data.csv")
all_strikes <- read.csv("~/math_examples/nla/hw4/p10_all_strikes.csv")

payoff_matrix <- as.matrix(payoff_data[2:ncol(payoff_data)])
print_latex(payoff_data,digits=6,rownames_on = FALSE)

#Part ii
inv <- solve(payoff_matrix)

#         C1200 C1275 C1350 C1425 P1200 P1050 P950  P800     
s_t_0 <- c(53.8,22.3, 6.8,  1.625,54.9, 14.75, 5.8, 1.425)

Q<- solve(payoff_matrix,s_t_0)

model_based_prices <- as.matrix(all_strikes[,2: ncol(all_strikes)])%*%Q
strike_to_model_price<- cbind(all_strikes$Op_type,as.data.frame( model_based_prices))
write.csv(strike_to_model_price,"p10_strike_model_price.csv")
#print_latex(strike_to_model_price,digits=9,rownames_on = FALSE)