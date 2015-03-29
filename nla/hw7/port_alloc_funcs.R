options(digits=10)
library("Matrix")
library("xtable")

sharpe_ratio <- function(mu_port, r_f, sigma_port) {
  return ((mu_port - r_f)/sigma_port)
}

value_at_risk <- function(n_days, c, sigma, mu, v_0) {
  z_val <- c(2.3263, 2.0537, 1.6449,1.2816)
  names(z_val) <- c(99,98,95,90)
  
  return (sqrt(n_days/252)*sigma*z_val[as.character(c)]*v_0 - n_days/252*mu*v_0)
}

#Portfolio allocation functions

tangency_portfolio <- function(covar_matrix, mu, r_f) {
  # The dummy mu doesnt matter here
  w_T <- min_var_tangent_asset_alloc(covar_matrix, mu, r_f, 1)$w_T
  mu_tangency <- t(w_T) %*% mu
  sigma_port <- min_var_tangent_asset_alloc(covar_matrix, mu, r_f, mu_tangency)$sigma_min
  sharpe <- sharpe_ratio(mu_tangency, r_f, sigma_port)
  
  ret <- list("w_T" = w_T, "mu" = mu_tangency, "sigma" = sigma_port, "sharpe_ratio" = sharpe)
  
  return (ret)
}

min_var_asset_no_cash<- function(covar_matrix) {
  ones <- rep(1, nrow(covar_matrix)) # create the ones column to represent the constant
  
  denom <- t(ones) %*% solve(covar_matrix) %*% ones
  w_m <- (solve(covar_matrix) %*% ones)/(denom[1])
  sigma <- sqrt(1/(t(ones) %*% solve(covar_matrix) %*% ones))
  
  ret <- list("w_m" = w_m, "sigma" = sigma)
  
  return (ret)
  
}

min_var_asset_alloc <- function(covar_matrix, mu, r_f, mu_port) {
  # Takes in covar matrix as type matrix  
  
  ones <- rep(1, length(mu)) # create the ones column to represent the constant
  mu_bar <- mu - r_f*ones
   
  x <- solve(covar_matrix, mu_bar)
  w_min <- ((mu_port- r_f) * x)/(t(mu_bar) %*% x)
  w_min_cash <- 1 - t(ones)%*% w_min
  sigma_min <- sqrt(t(w_min) %*% covar_matrix %*% w_min) #Std dev of portfolio
  
  ret <- list("w_min" = w_min, "w_min_cash" = w_min_cash, "sigma_min" = sigma_min)
  
  return (ret)
}

# Returns asset allocation of min var portfolio from tangency portfolio
min_var_tangent_asset_alloc <- function(covar_matrix, mu, r_f, mu_port) {
  # Takes in covar matrix as type matrix  
  ones <- rep(1, length(mu)) # create the ones column to represent the constant
  mu_bar <- mu - r_f*ones
  
  x <- solve(covar_matrix, mu_bar)
  w_T <- 1/(t(ones)%*%x) * x # ONLY DEPENDS ON COVAR MATRIX AND EXPECTED RETURNS
  w_min_cash <- 1 - (mu_port - r_f)/(t(mu_bar)%*% w_T)
  w_min <- (1 - w_min_cash) * w_T
  sigma_min <- sqrt(t(w_min) %*% covar_matrix %*% w_min)
  
  ret <- list("w_T" = w_T, "w_min_cash" = w_min_cash, "w_min" = w_min, "sigma_min" = sigma_min)
  
  return (ret)
}

# Returns asset allocation of max return portfolio
max_return_asset_alloc <- function(covar_matrix, mu, r_f, sigma_port) {
  # Takes in covar matrix as type matrix  
  
  # The return value will give back w_min , w_min_cash and sigma_min
  ones <- rep(1, length(mu)) # create the ones column to represent the constant
  mu_bar <- mu - r_f*ones
  
  x <- solve(covar_matrix, mu_bar)
  w_max <- (sigma_port * x)/sqrt(t(mu_bar) %*% x)
  w_max_cash <- 1- t(ones)%*% w_max
  mu_max <- r_f + t(mu_bar)%*% w_max # Expected return of portfolio
  
  ret <- list("w_max" = w_max, "w_max_cash" = w_max_cash, "mu_max" = mu_max)
  
  return (ret)
}

# Returns asset allocation of max return portfolio from tangency portfolio
max_return_tangent_asset_alloc <- function(covar_matrix, mu, r_f, sigma_port) {
  # Takes in covar matrix as type matrix  
  
  # The return value will give back w_min , w_min_cash and sigma_min
  ones <- rep(1, length(mu)) # create the ones column to represent the constant
  mu_bar <- mu - r_f*ones
  
  x <- solve(covar_matrix, mu_bar)
  w_T <- (sigma_port * x)/sqrt(t(mu_bar) %*% x)
  
  val <- (t(ones)%*%solve(covar_matrix) %*% mu_bar)
  if ( val[1] > 0) {
    w_max_cash <- (1 - sigma_port/sqrt((w_T) %*% covar_matrix %*% w_T))
  }
  else {
    w_max_cash <- (1 + sigma_port/sqrt((w_T) %*% covar_matrix %*% w_T))
  }
  
  w_max <- (1 - w_max_cash) * w_T
  mu_max <- r_f + t(mu_bar)%*% w_max
  
  ret <- list("w_T" = w_T, "w_max" = w_max, "w_max_cash" = w_max_cash, "mu_max" = mu_max)
  
  return (ret)
}