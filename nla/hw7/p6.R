rm(list = ls())
source("port_alloc_funcs.R")

mu_1 <- 0.08
mu_2 <- 0.12

m <- c(mu_1, mu_2)

sigma_1 <-0.15
sigma_2 <- 0.20
rho_1_2 <- 0.25
r_f <- 0.05

# Part i

covar_matrix <- matrix(c(sigma_1^2, sigma_1*sigma_2*rho_1_2, sigma_1*sigma_2*rho_1_2, sigma_2^2), byrow = TRUE, nrow=2)
# Only return w_T
w_t <- min_var_tangent_asset_alloc(covar_matrix, m, r_f, 1)$w_T

# Part ii
ret_ii <- min_var_asset_alloc(covar_matrix, m, r_f, 0.07)
w_t_ii <- ret_ii$w_min
sigima_ii <- ret_ii$sigma_min

#Part iii
ret_iii <- min_var_asset_alloc(covar_matrix, m, r_f, 0.11)
w_t_iii <- ret_iii$w_min
sigma_iii <- ret_iii$sigma_min

#Part iv
ret_iv <-  max_return_asset_alloc(covar_matrix, m, r_f, 0.12)
w_t_iv <- ret_iv$w_max
mu_iii <- ret_iv$mu_max

#Part v
ret_v <- max_return_asset_alloc(covar_matrix, m, r_f, 0.18)
w_t_v <- ret_v$w_max
mu_v <- ret_v$mu_max

# Part vi
w_t_vi <- min_var_asset_alloc(covar_matrix, m, 0.0525, 0.07)$w_min


