plot(hw4[hw4$maturity == 130/365,]$strike, hw4[hw4$maturity == 130/365,]$impl_vol, main="Impl_vol vs Strike for T=130/365", ylab = "Impl_vol", xlab ="Strike")
text(hw4[hw4$maturity == 130/365,]$strike, hw4[hw4$maturity == 130/365,]$impl_vol, labels=hw4[hw4$maturity == 130/365,]$impl_vol, cex=0.6, pos=4)

plot(hw4[hw4$maturity == 208/365,]$strike, hw4[hw4$maturity == 208/365,]$impl_vol, main="Impl_vol vs Strike for T=208/365", ylab = "Impl_vol", xlab ="Strike")
text(hw4[hw4$maturity == 208/365,]$strike, hw4[hw4$maturity == 208/365,]$impl_vol, labels=hw4[hw4$maturity == 208/365,]$impl_vol, cex=0.6, pos=4)

plot(hw4[hw4$maturity == 306/365,]$strike, hw4[hw4$maturity == 306/365,]$impl_vol, main="Impl_vol vs Strike for T=306/365", ylab = "Impl_vol", xlab ="Strike")
text(hw4[hw4$maturity == 306/365,]$strike, hw4[hw4$maturity == 306/365,]$impl_vol, labels=hw4[hw4$maturity == 306/365,]$impl_vol, cex=0.6, pos=4)