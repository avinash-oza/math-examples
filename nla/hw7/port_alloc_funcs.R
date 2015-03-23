options(digits=10)
library("Matrix")
library("xtable")

#Portfolio allocation functions

min_var_asset_alloc <- function(covar_matrix, mu, r_f, mu_port) {
  # Takes in covar matrix as type matrix  
  
  ones <- rep(1, length(mu)) # create the ones column to represent the constant
  mu_bar <- mu - r_f*ones
   
  x <- solve(covar_matrix, mu_bar)
  w_min <- ((mu_port- r_f) * x)/(t(mu_bar) %*% x)
  w_min_cash <- 1 - t(ones)%*% w_min
  sigma_min <- sqrt(t(w_min) %*% covar_matrix %*% w_min)
  
#  return (w_min)
  return (w_min_cash)
#  return (sigma_min)
}

# Returns asset allocation of min var portfolio from tangency portfolio
min_var_tangent_asset_alloc <- function(covar_matrix, mu, r_f, mu_port) {
  # Takes in covar matrix as type matrix  
  
  # The return value will give back w_min , w_min_cash and sigma_min
  ones <- rep(1, length(mu)) # create the ones column to represent the constant
  mu_bar <- mu - r_f*ones
  
  x <- solve(covar_matrix, mu_bar)
  w_T <- 1/(t(ones)%*%x) * x
  w_min_cash <- 1 - (mu_port - r_f)/(t(mu_bar)%*% w_T)
  w_min <- (1 - w_min_cash) * w_T
  sigma_min <- sqrt(t(w_min) %*% covar_matrix %*% w_min)
  
  return (w_T)
  #  return (w_min)
  #return (w_min_cash)
  #  return (sigma_min)
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
  mu_max <- r_f + t(mu_bar)%*% w_max
  
  #return (w_max)
  #  return (w_max_cash)
    return (mu_max)
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
  
  #return (w_max)
  return (w_max_cash)
  return (mu_max)
}