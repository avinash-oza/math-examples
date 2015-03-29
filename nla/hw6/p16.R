source("../hw1/nla_funcs.R")

x <- c(0, 2/12,5/12,11/12,15/12)
y <- c(0.0075,-log(.9980)/(x[2]), -log(.9935)/(x[3]), -log(.9820)/(x[4]), -log(.9775)/(x[5]))

#Demo problem from book
#x <- c(0,2/12,6/12,1,20/12)
#y <- c(0.0050,0.0065,0.0085,0.0105,0.0120)

#########################Does not actually spline!!!###########################################
v <- efficent_cubic_spline(x,y)
coeffs<- cubic_spline_coeffs(v)

z<- splinefun(x,y,method="natural")
c <- 0.625
flow_times <- c(2/12, 5/12,8/12,11/12,14/12)
bond_price <- c*exp(-z(flow_times[1])*(flow_times[1])) +
  c*exp(-z(flow_times[2])*(flow_times[2])) +
  c*exp(-z(flow_times[3])*(flow_times[3])) +
  c*exp(-z(flow_times[4])*(flow_times[4])) +
  (100 +c)*exp(-z(flow_times[5])*(flow_times[5]))
# 
# 
# plot(z,xlab = "Months/12",ylab="Zero Rate(%)",main="Zero rate vs Date")
# points(x = x,y = y)