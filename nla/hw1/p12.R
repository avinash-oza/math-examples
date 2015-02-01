source("nla_funcs.R")

indices_data <- read.csv("~/math_examples/nla/hw1/indices-july2011.csv")
# Part i :Daily percenage returns calculation 
percent_returns <- calculate_percent_returns(indices_data)

a <- covar_calc(percent_returns)
corr_vector <- sqrt(diag(a))
corr_matrix_daily_percent <- correlation_calc(corr_vector,a) 
  
# Part i :Daily log returns
log_returns <- calculate_log_returns(indices_data)
b <- covar_calc(log_returns)
corr_vector <- sqrt(diag(b))
corr_matrix_daily_log <- correlation_calc(corr_vector,b) 

#Part ii: Weekly returns
weekly_mat <- indices_data[c(2,7,12,16,21,26,31,36,40,45,50,55,60,65,70,75,79,84,89,94,99,104,108,113,118,123,128,132,137,142),]
# Percent returns
weekly_percent_returns <- calculate_percent_returns(weekly_mat)
c <- covar_calc(weekly_percent_returns)
corr_vector <- sqrt(diag(c))
corr_matrix_weekly_percent <- correlation_calc(corr_vector,c) 

# Log returns
weekly_log_returns <- calculate_log_returns(weekly_mat)
d <- covar_calc(weekly_log_returns)
corr_vector <- sqrt(diag(d))
corr_matrix_weekly_log <- correlation_calc(corr_vector,d) 

# Part iii Monthly returns
monthly_mat <- indices_data[c(2,22,41,64,84,105,127),]

# Percent returns
monthly_percent_returns <- calculate_percent_returns(monthly_mat)
e <- covar_calc(monthly_percent_returns)
corr_vector <- sqrt(diag(e))
corr_matrix_monthly_percent <- correlation_calc(corr_vector,e) 

# Log returns
monthly_log_returns <- calculate_log_returns(monthly_mat)
f <- covar_calc(monthly_log_returns)
corr_vector <- sqrt(diag(f))
corr_matrix_monthly_log <- correlation_calc(corr_vector,f) 