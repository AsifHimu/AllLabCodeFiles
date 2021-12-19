clc;
clear all;
close all;

bits=[1 1 0 1 0];
bit_dur=1;
T=length(bits)*bit_dur;
fs=100;
t=0:1/fs:T-(1/fs);

a=ones(1,(fs/2)*bit_dur)*1;
b=zeros(1,(fs/2)*bit_dur);
one=[a b];
c=ones(1,(fs/2)*bit_dur)*(-1);
zero=[c b];

for i=1:length(bits)
    if bits(i)==1
        x((i-1)*fs*bit_dur+1:i*fs*bit_dur)=one;
    else
        x((i-1)*fs*bit_dur+1:i*fs*bit_dur)=zero;
    end
end

plot(t,x,'linewidth',2);
ylim([-5,5]);
grid on;

%demodulation
for i=1:length(x)/(fs*bit_dur)
    if x((i-1)*fs*bit_dur+1:i*fs*bit_dur) == one
        disp(1);
    else
        disp(0);
    end
end
