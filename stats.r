x <- seq(0,1,0.1)

y <- exp(x)

z <- x**2


plot(x, y, main='title', xlab="x-etiqueta")
points(x,z)
plot(x, y, xlim = c(0,1), ylim = c(0,3))
par(mfrow=c(1,2))



temp1<-cbind(x,x,x)
temp2 <- cbind(y,z,2*x)

matplot(temp1, temp2, col=c('green', 'red', 'blue', lwd=2,type='l', lty=c("dash", "l", "l")))

