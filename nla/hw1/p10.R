source("nla_funcs.R")
#q 11
transform(indices.close_jul26.aug9_2012, log_diff=c(NA,(diff(log(abs(Dow.Jones))))))
log_returns <- diff(log(abs(indices.close_jul26.aug9_2012$Dow.Jones)))
log_returns <- cbind(log_returns,diff(log(abs(indices.close_jul26.aug9_2012$NASDAQ))))
log_returns <- cbind(log_returns,diff(log(abs(indices.close_jul26.aug9_2012$S.P.500))))

a <- covar_calc(log_returns)