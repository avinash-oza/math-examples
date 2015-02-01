source("nla_funcs.R")

indices.close_jul26.aug9_2012 <- read.csv("~/math_examples/nla/hw1/indices-close_jul26-aug9_2012.csv")
#q 11
diff(log(abs(as.matrix(indices.close_jul26.aug9_2012[,2: length(indices.close_jul26.aug9_2012)]))))
a <- covar_calc(log_returns)