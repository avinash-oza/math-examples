options(digits=10)
print_latex<- function(mat,digits=-3,rownames_on=TRUE,colnames_on=TRUE) {
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

cubic_spline <- function(x, y) {
  
  library("Matrix")
  n <- length(x) -1
  
  b <- c(0*1:(4*n))
  
  M_bar <- matrix(0,nrow = 4*n,ncol = 4*n)
  M_bar[1,3] <- 2; M_bar[1,4] <-6*x[1]
  M_bar[4*n,4*n -1] <- 2;M_bar[4*n,4*n]<-6*x[n+1]
  
  for(i in 1:n) {
    vec_val <- i+1
    
    b[4*i-2] = y[vec_val-1]; b[4*i-1] = y[vec_val]
    
    M_bar[4*i-2,4*i-3] <- 1;M_bar[4*i-2,4*i-2] <- x[vec_val-1]
    M_bar[4*i-2,4*i-1] <- (x[vec_val-1])^2; M_bar[4*i-2,4*i] <- (x[vec_val-1])^3
    M_bar[4*i-1,4*i-3] <- 1;M_bar[4*i-1,4*i-2] <- x[vec_val]
    M_bar[4*i-1,4*i-1] <- (x[vec_val])^2;M_bar[4*i-1,4*i] <- (x[vec_val])^3
  }
  
  for(i in 1:(n-1)) {
    vec_val <- i+1
    
    M_bar[4*i,4*i-2] <- 1; M_bar[4*i,4*i-1] <- 2*x[vec_val]
    M_bar[4*i,4*i] <- 3*(x[vec_val])^2; M_bar[4*i,4*i+2] <- -1
    M_bar[4*i,4*i+3] <- -2*x[vec_val]; M_bar[4*i,4*i+4] <- -3*(x[vec_val])^2
    M_bar[4*i+1,4*i-1] <- 2; M_bar[4*i +1,4*i] <- 6*x[vec_val]
    M_bar[4*i+1,4*i+3] <- -2; M_bar[4*i+1,4*i+4] <- -6*x[vec_val]
  }
  
  return (solve(M_bar,b))
  #return (b)
  
}