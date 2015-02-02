print_latex<- function(mat,digits=-3,rownames_on=FALSE,colnames_on=FALSE) {
  a <- matrix(rnorm(nrow(mat) *ncol(mat)), nrow(mat) ,ncol(mat))
  l_table <- xtable(mat, digits=digits, align=rep("",ncol(a)+1))
  print(l_table, floating=FALSE, hline.after=NULL,tabular.environment="bmatrix", include.rownames=rownames_on, include.colnames=colnames_on)
}

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
  return (log_returns)
}


# Calculates the covariance matrix for a returns matrix
covar_calc <- function(returns_matrix) {
  col_avgs <- colMeans(returns_matrix)
  t_bar <- sweep(returns_matrix,2,col_avgs)
  #print(print_latex(t_bar))
  
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