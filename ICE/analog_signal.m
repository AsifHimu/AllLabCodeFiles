clc;
clear all;
close all;
a=5;
f=2;
T=2;
fs=50;
t=0:1/fs:T;
ph=pi/2;
x = a*sin(2*pi*f*t+ph);
subplot(2,1,1);
plot(t,x);
xlabel("T");
ylabel("x(t)");
title("Analog signal sine wave with 90 degree phase");

subplot(2,1,2);
stem(x);
title("Digital signal sine wave with 90 degree phase");


