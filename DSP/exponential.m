clc;
clear all;
n=0:1:20;
x=0.8.^n;
subplot(2,2,1);
stem(n,x);
xlabel('n');
ylabel('x(n)');
title('Exponential sequence');