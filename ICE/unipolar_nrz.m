clc;
close all;
clear all;

bits=[0,1,1,0,0,1];
bit_dur=2;

T=length(bits)*bit_dur;
fs=100;
t=0:1/fs:T-(1/fs);

for i=1:length(bits)
    if bits(i)==0
        x((i-1)*fs*bit_dur+1:i*fs*bit_dur)=0;
    else
        x((i-1)*fs*bit_dur+1:i*fs*bit_dur)=5;
    end
end
subplot(4,1,1);
plot(t,x);
ylim([-5,7]);
subplot(4,1,2);
stem(x);
%demodulation
for i=1:length(x)/(fs*bit_dur)
    if x(1,(i-1)*fs*bit_dur+1:i*fs*bit_dur) == zeros(1,fs*bit_dur)
        disp(0)
    else
        disp(1)
    end
end