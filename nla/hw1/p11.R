source("nla_funcs.R")

indices.close_jul26.aug9_2012 <- read.csv("~/math_examples/nla/hw1/indices-close_jul26-aug9_2012.csv")
#q 11
log_returns <- calculate_log_returns(indices.close_jul26.aug9_2012)
print_latex(log_returns,-3, FALSE,TRUE)
a <- covar_calc(log_returns)
print_latex(a)