source("../hw1/nla_funcs.R")


p_2_options <- read.csv("~/math_examples/nla/hw7/p_2_options.csv")

A <- as.matrix(-p_2_options$STRIKE)
y <- p_2_options$CALL_PRICE - p_2_options$PUT_PRICE 

pvf_disc <- least_squares(A, y)
