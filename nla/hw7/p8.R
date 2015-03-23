rm(list = ls())
source("port_alloc_funcs.R")

m <- c(0.04, 0.035, 0.05, 0.034)
r_f <- 0.01
covar_matrix <- matrix(c(0.09,0.01,0.03,-0.015,0.01,0.0625,-0.02,-0.01,0.03,-0.02,0.1225,0.02,-0.015,-0.01,0.02,0.0576), byrow = TRUE, nrow=4)

# Part i

# Find tangency portfolio weights
w_T_i <- min_var_tangent_asset_alloc(covar_matrix, m, r_f, 4 )$w_T 
# Find expected return of tangency portfolio
mu_port_i <- t(w_T_i)%*% m 
# Find std using expected return
sigma_port <- min_var_tangent_asset_alloc(covar_matrix, m, r_f, mu_port_i)$sigma_min 
# Find Sharpe ratio
s_ratio_i <- sharpe_ratio(mu_port_i, r_f, sigma_port)

# Part ii

val_ii <- min_var_asset_alloc(covar_matrix, m, r_f, 0.03)
w_ii <- val_ii$w_min
sigma_min_ii <- val_ii$sigma_min

s_ratio_ii <- sharpe_ratio(0.03, r_f, sigma_min_ii)


# Part iii
val_iii <- max_return_asset_alloc(covar_matrix, m, r_f, 0.27)
mu_iii <- val_iii$mu_max

s_ratio_iii <- sharpe_ratio(mu_iii, r_f, 0.27)

# Part iv
ret_iv <- min_var_asset_no_cash(covar_matrix)
w_full <- ret_iv$w_m
sigma <- ret_iv$sigma
mu_full <- t(w_full) %*% m
s_ratio_iv <- sharpe_ratio(mu_port = mu_full, r_f = r_f, sigma_port = sigma)


