source("../hw1/nla_funcs.R")

T_2 = c(4.69,4.81,4.81,4.79,4.79,4.83,4.81,4.81,4.83,4.81,4.82,4.82,4.80,4.78,4.79)
T_3 = c(4.58,4.71,4.72,4.78,4.77,4.75,4.71,4.72,4.76,4.73,4.75,4.75,4.73,4.71,4.71)
T_5 = c(4.57,4.69,4.70,4.77,4.77,4.73,4.72,4.74,4.77,4.75,4.77,4.76,4.75,4.72,4.71)
T_10 = c(4.63,4.73,4.74,4.81,4.80,4.79,4.76,4.77,4.80,4.77,4.80,4.80,4.78,4.73,4.73)

B <- cbind(T_2,T_5,T_10) # The vector without the ones column
a <- rep(1, nrow(B)) # create the ones column to represent the constant


# Part i
# Use 2,5, and 10 to represent the 3 year yields
B_with_ones <- cbind(a, B)
coeffs <- least_squares(B, T_3)
approx_T_3_ols <- B_with_ones%*% coeffs # From y=Ax

approx_diff_ols <- abs(T_3 - approx_T_3_ols)
approx_error_ols <- sqrt(t(approx_diff_ols)%*%approx_diff_ols) #Calculate norm=w^t w

# Part ii
approx_T_3_linear_interp <- (2/3)*T_2 + (1/3)*T_5
approx_T_3_linear_interp_diff <- abs(T_3 - approx_T_3_linear_interp )
linear_interp_error <- sqrt(t(approx_T_3_linear_interp_diff)%*%approx_T_3_linear_interp_diff) #Calculate norm=w^t w


# Part iii

approx_T_3_cubic <- c(0*(1:length(T_2) ))
# Declare the years for the cubic spline
x <- c(2, 5, 10)

for (i in 1:length(T_2)) {
  y <- B[i,]
  z<- splinefun(x,y,method="natural")
  approx_T_3_cubic[i] <- z(3)
}

approx_T_3_cubic_interp_diff <- abs(T_3 - approx_T_3_cubic )
cubic_interp_error <- sqrt(t(approx_T_3_cubic_interp_diff)%*%approx_T_3_cubic_interp_diff) #Calculate norm=w^t w


