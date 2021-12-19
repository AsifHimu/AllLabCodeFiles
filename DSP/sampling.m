clc;
clear all;
close all;
a=5;
f=2;
fs=50;
t=0:1/fs:1
x=a*sin(2*pi*f*t);
subplot(2,2,1);
stem(x);
subplot(2,2,4);
plot(t,x);