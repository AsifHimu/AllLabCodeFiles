a=3;
f=10;
fs1=500;
T=2;
ph=pi/4;
t1=0:1/fs1:T-(1/fs1);
x1=a*sin(2*pi*f*t1+ph);

subplot(2,1,1);
plot(t1,x1);
title("Main sine wave");
fs2=15;
t2=0:1/fs2:T-(1/fs2);
x2=a*sin(2*pi*f*t2+ph);

subplot(2,1,2);
plot(t2,x2);
title("Aliasing effect");