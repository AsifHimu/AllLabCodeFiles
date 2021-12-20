clc;
clear all;
close all;

bits=[0 1 1 1 0 0 0 1 0 1];
bit_dur=1;
T=length(bits)*bit_dur;
fs=100;
t=0:1/fs:T-(1/fs);

for i=1:length(bits)
    if bits(i)==0
        x((i-1)*fs*bit_dur+1:i*fs*bit_dur)=-2;
    else
        x((i-1)*fs*bit_dur+1:i*fs*bit_dur)=2;
    end
end

subplot(3,1,1);
plot(t,x,'linewidth',2);
title("Input signal");
ylim([-5,5]);
a=5;
f=3;
sig=a*sin(2*pi*f*t);
subplot(3,1,2);
plot(t,sig);
title("Carrier signal");

m=sig.*x;
subplot(3,1,3);
plot(t,m);
