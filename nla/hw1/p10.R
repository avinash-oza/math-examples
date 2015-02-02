source("nla_funcs.R")
libary("xtable")
omega <- matrix(c(1,-0.25,.15,-0.05,-0.3,
                  -0.25,1,-0.10,-0.25,0.10,
                  0.15,-0.1,1,0.2,0.05,
                  -0.05,-0.25,.20,1,0.10,
                  -0.3,0.10,0.05,0.10,1),nrow = 5,ncol = 5)
#Calculate covariance matrix
corr_vector <- c(0.25,0.5,1,2,4)
covar_m <- covar_calc_corr(corr_vector,omega)
print_latex(covar_m,5)

#Part ii
corr_vector <- c(4, 2,1, 0.5,0.25)
corr_mat <- covar_calc_corr(corr_vector,omega)
print_latex(corr_mat,2)

