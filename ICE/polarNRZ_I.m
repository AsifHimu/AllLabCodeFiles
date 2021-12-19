clc;
close all;
clear all;

bits=[0 1 0 1 1];
bit_dur=1;
T=length(bits)*bit_dur;
fs=100;
t=0:1/fs:T-(1/fs);

lastbit=1;
for i=1:length(bits)
    if bits(i)==1
        x((i-1)*fs*bit_dur+1:i*fs*bit_dur)=-lastbit;
        lastbit=-lastbit;
    else
        x((i-1)*fs*bit_dur+1:i*fs*bit_dur)=lastbit;
    end
end
%subplot(4,1,1);
plot(t,x,'linewidth',2);
ylim([-5,5]);
grid on;
%demodulation
lastbit=1;
for i=1:length(x)/(fs*bit_dur)
    if x((i-1)*fs*bit_dur+1:i*fs*bit_dur)~= lastbit;
        disp(1);
        lastbit=-lastbit;
    else
        disp(0);
    end
end