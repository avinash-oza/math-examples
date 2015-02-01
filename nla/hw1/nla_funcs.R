# Calculates the covariance matrix for a returns matrix
covar_calc <- function(returns_matrix) {
  col_avgs <- colMeans(returns_matrix)
  
  t_bar <- sweep(returns_matrix,2,col_avgs)
  
  covar_matrix = 1/(dim(returns_matrix)[1] -1)*t(t_bar)%*%t_bar
  return (covar_matrix)
} 