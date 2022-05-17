clc;
close all;
clear all;
fs=8000;
ts=1/fs;
N=8;
n=0:N-1;
x=sin(2*pi*1000*n*ts);
X=zeros(1,N);
for m=1:N
    for n=1:N
        X(m)=X(m)+x(n)*exp(-j*2*pi*(n-1)*(m-1)/N);
    end
end
n=0:N-1;
subplot(3,2,1);
stem(n,x);
subplot(3,2,2);
stem(n,real(X));