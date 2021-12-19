clc;
clear all;
close all;

a=2;
f=1000;
fs=10000;
t=0:1/fs:0.05-(1/fs);
x=a*sin(2*pi*f*t);
subplot(4,2,1);
plot(t,x);

N=500;
n=0:N-1;
%hamming window
hw=0.54-0.46*cos((2*pi*n)/(N-1));
subplot(4,2,3);
plot(n,hw);

hamming= x.*hw;
subplot(4,2,4);
plot(n,hamming);
%rectangular window
rw=ones(1,N);
subplot(4,2,5);
plot(n,rw);

rectangular=x.*rw;
subplot(4,2,6);
plot(n,rectangular);
%triangular window
tw=1-(abs(2*n-N+1)/(N-1));
subplot(4,2,7);
plot(n,tw);

triangular=x.*tw;
subplot(4,2,8);
plot(n,triangular);