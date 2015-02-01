#Calculates the percent return of the elements. Takes in complete frame with dates
calculate_percent_returns <- function(data_matrix) {
  data <- data_matrix[,2:length(data_matrix)] # Strip away the dates from the data
  percent_returns = diff(as.matrix(data))/as.matrix(data[-nrow(data),])
  return (percent_returns)
}

#Calculates the percent return of the elements. Takes in complete frame with dates
calculate_log_returns <- function(data_matrix) {
  data <- data_matrix[,2:length(data_matrix)] # Strip away the dates from the data
  log_returns <- diff(log(abs(as.matrix(data))))
  percent_returns = diff(as.matrix(data))/as.matrix(data[-nrow(data),])
  return (percent_returns)
}


# Calculates the covariance matrix for a returns matrix
covar_calc <- function(returns_matrix) {
  col_avgs <- colMeans(returns_matrix)
  
  t_bar <- sweep(returns_matrix,2,col_avgs)
  
  covar_matrix = 1/(dim(returns_matrix)[1] -1)*t(t_bar)%*%t_bar
  return (covar_matrix)
}

covar_calc_corr <- function(corr_vector, correl_matrix) {
  D1 <- diag(corr_vector)
  return(D1%*%correl_matrix%*%D1)
}

correlation_calc <- function(corr_vector, covar_matrix) {
  # Formula for correlation is 
  D1_inv <- diag(corr_vector^(-1))
  return (D1_inv%*%covar_matrix%*%D1_inv)
}