rm(list = ls())
source("port_alloc_funcs.R")

sigma_1 <- 0.18; sigma_2 <- 0.20; sigma_3 <- 0.24
rho_1_2 <- -0.50; rho_2_3 <- -0.25; rho_1_3 <- 0.15

var_1 <- sigma_1^2
var_2 <- sigma_2^2
var_3 <- sigma_3^2


covar_1_2 <- sigma_1*sigma_2*rho_1_2
covar_1_3 <- sigma_1*sigma_3*rho_1_3
covar_2_3 <- sigma_2*sigma_3*rho_2_3

m <- c(0.06, 0.09, 0.12)
r_f <- 0.03
covar_matrix <- matrix(c(var_1, covar_1_2, covar_1_3, covar_1_2, var_2, covar_2_3, covar_1_3, covar_2_3, var_3 ), byrow = TRUE, nrow=3)

# Part i Calculate by hand
ret_i <- min_var_tangent_asset_alloc(covar_matrix, m, r_f, 1)
w_T_i <- ret_i$w_T
mu_i <- t(w_T_i) %*% m
# Use above expected return to calculate std dev
ret_i_a <- min_var_tangent_asset_alloc(covar_matrix, m, r_f, mu_i)
sigma_i <- ret_i_a$sigma_min

# Part ii
ret_ii <-  min_var_asset_alloc(covar_matrix, m, r_f, 0.10)
w_ii <- ret_ii$w_min
sigma_ii <- ret_ii$sigma_min

# Part iii
ret_iii <- max_return_asset_alloc(covar_matrix, m, r_f, 0.20)
w_iii <- ret_iii$w_max
mu_iii <- ret_iii$mu_max

