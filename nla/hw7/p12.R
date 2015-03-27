source("port_alloc_funcs.R")

m <- c(0.08, 0.12, 0.16)
sigma_1 <- 0.25;sigma_2 <- 0.25; sigma_3 <- 0.30
rho_1_2 <- -0.25; rho_2_3 <- -0.25; rho_1_3 <- 0.25
sigma <- c(sigma_1,sigma_2,sigma_3)

covar_1_2 <- sigma_1*sigma_2*rho_1_2
covar_2_3 <- sigma_2*sigma_3*rho_2_3
covar_1_3 <- sigma_1*sigma_3*rho_1_3


# Part i
var <- value_at_risk(5, 95, sigma, m, 100000000)

# Part ii

# Asset 1 and 2
c_var_1_2 <- matrix(c(sigma_1^2, covar_1_2, covar_1_2, sigma_2^2 ), byrow = TRUE, nrow = 2)
ret_1_2 <- min_var_asset_no_cash(c_var_1_2)
w_1_2 <- ret_1_2$w_m
mu_1_2 <- t(w_1_2)%*% c(m[1], m[2])
sigma_1_2 <- ret_1_2$sigma

var_1_2 <- value_at_risk(5, 95, sigma_1_2, mu_1_2, 100000000)

# Asset 2 and 3
c_var_2_3 <- matrix(c(sigma_2^2, covar_2_3, covar_2_3, sigma_3^2 ), byrow = TRUE, nrow = 2)
ret_2_3 <- min_var_asset_no_cash(c_var_2_3)
w_2_3 <- ret_2_3$w_m
mu_2_3 <- t(w_2_3)%*% c(m[2], m[3])
sigma_2_3 <- ret_2_3$sigma

var_2_3 <- value_at_risk(5, 95, sigma_2_3, mu_2_3, 100000000)

# Asset 1 and 3
c_var_1_3 <- matrix(c(sigma_1^2, covar_1_3, covar_1_3, sigma_3^2 ), byrow = TRUE, nrow = 2)
ret_1_3 <- min_var_asset_no_cash(c_var_1_3)
w_1_3 <- ret_1_3$w_m
mu_1_3 <- t(w_1_3)%*% c(m[1], m[3])
sigma_1_3 <- ret_1_3$sigma

var_1_3 <- value_at_risk(5, 95, sigma_1_3, mu_1_3, 100000000)

# Part iii
c_var_all <- matrix(c(sigma_1^2, covar_1_2, covar_1_3, covar_1_2, sigma_2^2, covar_2_3, covar_1_3, covar_2_3,sigma_3^2 ), byrow = TRUE, nrow = 3)
ret_all <- min_var_asset_no_cash(c_var_all)
w_all <- ret_all$w_m
mu_all <- t(w_all)%*% m
sigma_all <- ret_all$sigma

var_all <- value_at_risk(5, 95, sigma_all, mu_all, 100000000)