rm(list = ls())
setwd("~/git_repos/math_examples/nla/fall2016_final")
source("../hw1/nla_funcs.R")

#financials2012 <- read.csv("~/math_examples/nla/hw7/financials2012.csv")
financials2012 <- read.csv("data-7-cov_corr_july2011-june2013_weekly.csv")
#REQUIRES DATA WITH FURTHEST DATE AT THE TOP AND CLOSEST AT BOTTOM T1<T2

# IF T1 > T2, next line is needed
financials2012 <- financials2012[nrow(financials2012):1, ]

# Part i
percent_returns <- calculate_percent_returns(financials2012)
write.csv(percent_returns, "percent_returns.csv")

y <- percent_returns[,1]
# Remove JPM from frame
A <- as.matrix(percent_returns[,2:ncol(percent_returns)])

covar_matrix_returns <- covar_calc(percent_returns)
write.csv(covar_matrix_returns, "percent_returns.csv")
U <- chol(covar_matrix_returns)

# Take only GS,MS,BAC
A_american <- as.matrix(percent_returns[,c(2,3,4,5,6,7)])

# CHECK IF CONSTANT IS NEEDED OR NOT
american_coeffs <- least_squares(A_american, y)
a <- rep(1, nrow(A_american)) # create the ones column to represent the constant
estimated_return_jpm_american_only <- cbind(a, A_american) %*% american_coeffs
american_ols_error <- abs(y - estimated_return_jpm_american_only)
american_approx_error <- sqrt(t(american_ols_error) %*% american_ols_error)

spoptionValues <- read.csv("MTH9821_Midterm_2013_SPX_Options.csv")
cMinusP = as.matrix(spoptionValues$Price - spoptionValues$Price.1)
y = cMinusP
onesColumn <- rep_len(1, nrow(as.matrix(spoptionValues$Call.Strike))) # create the ones column to represent the constant
firstColumn = as.matrix(-1*spoptionValues$Call.Strike)
AMatrix <- cbind(onesColumn,firstColumn)

res = least_squares(AMatrix, y)

