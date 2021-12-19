clc;
clear all;
close all;
x=[1 2 3 4];%input signal
h=[1 1 1 1];%second signal

N1=length(x);
N2=length(h);
X = [x,zeros(1,N2)];
H = [h,zeros(1,N1)];

for i=1:N1+N2-1
    y(i)=0;
    for j=1:N1
        if(i-j+1>0)
            y(i)=y(i)+X(j)*H(i-j+1)
        end
    end
end

stem(y);
title("Convolution between tewo sequences");
    