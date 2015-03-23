rm(list = ls())
source("../hw1/nla_funcs.R")

#financials2012 <- read.csv("~/math_examples/nla/hw7/financials2012.csv")
financials2012 <- read.csv("~/math_examples/nla/hw7/financials2012_rev.csv")

# Part i
percent_returns <- calculate_percent_returns(financials2012)

#Part ii

y <- percent_returns[,1]
# Remove JPM from frame
A <- as.matrix(percent_returns[,2:ncol(percent_returns)])

coeffs <- least_squares(A, y)
a <- rep(1, nrow(A)) # create the ones column to represent the constant
estimated_return_jpm <- cbind(a, A) %*% coeffs
ols_error <- abs(y - estimated_return_jpm)
approx_error <- sqrt(t(ols_error) %*% ols_error)

# Part iii
# Take only GS,MS,BAC
A_american <- as.matrix(percent_returns[,c(2,3,4)])

american_coeffs <- least_squares(A_american, y)
a <- rep(1, nrow(A_american)) # create the ones column to represent the constant
estimated_return_jpm_american_only <- cbind(a, A_american) %*% american_coeffs
american_ols_error <- abs(y - estimated_return_jpm_american_only)
american_approx_error <- sqrt(t(american_ols_error) %*% american_ols_error)

# Part iv

y_prices <- as.matrix(financials2012$JPM)
# All other companies
A_all <- as.matrix(financials2012[,3:ncol(financials2012)])
a <- rep(1, nrow(A_all)) # create the ones column to represent the constant

all_coeffs <- least_squares(A_all, y_prices)

estimated_price_all <- cbind(a, A_all) %*% all_coeffs
all_ols_error <- abs(y_prices - estimated_price_all)
all_approx_error <- sqrt(t(all_ols_error) %*% all_ols_error)
