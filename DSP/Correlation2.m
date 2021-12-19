clc;
close all;
clear all;

x=[1 2 3 4];
h=[1 2 1 2];

h=fliplr(h);
n1=length(x);
n2=length(h);

X=[x,zeros(1,n2)];
Y=[h,zeros(1,n1)];

for i=1:n1+n2-1
    y(i)=0;
    for j=1:n1
        if(i-j+1>0)
            y(i)=y(i)+X(j)*Y(i-j+1);
        end
    end
end
title("Correlation solution");
stem(y);