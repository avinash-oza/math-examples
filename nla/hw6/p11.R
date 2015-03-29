source("../hw1/nla_funcs.R")

# Weekly returns
data.DJ30.july2011.june2013_weekly <- read.csv("~/math_examples/nla/hw6/data-DJ30-july2011-june2013_weekly.csv")
col_names <- colnames(data.DJ30.july2011.june2013_weekly)[2:9]
# Part i :Daily percenage returns calculation 
log_weekly_returns <- calculate_log_returns(data.DJ30.july2011.june2013_weekly)


#####Test code
# weekly_percent_returns <- calculate_percent_returns(data.DJ30.july2011.june2013_monthly)
# not_used <- covar_calc(weekly_percent_returns)
# 
# c_vector <- sqrt(diag(not_used))
# test_log <- correlation_calc(c_vector,not_used) 
#############

a <- covar_calc(log_weekly_returns)

corr_vector <- sqrt(diag(a))
corr_matrix_weekly_log <- correlation_calc(corr_vector,a) 
print_latex(cbind(as.data.frame.AsIs(col_names),corr_matrix_weekly_log),10,FALSE,FALSE)

# Monthly returns
data.DJ30.july2011.june2013_monthly <- read.csv("~/math_examples/nla/hw6/data-DJ30-july2011-june2013_monthly.csv")
col_names <- colnames(data.DJ30.july2011.june2013_monthly)[2:9]
# Part i :Daily percenage returns calculation 
log_monthly_returns <- calculate_log_returns(data.DJ30.july2011.june2013_monthly)

b <- covar_calc(log_monthly_returns)

corr_vector <- sqrt(diag(b))
corr_matrix_monthly_log <- correlation_calc(corr_vector,b) 
print_latex(cbind(as.data.frame.AsIs(col_names),corr_matrix_monthly_log),10,FALSE,FALSE)