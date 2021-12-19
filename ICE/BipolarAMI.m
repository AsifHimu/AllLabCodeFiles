clc;
close all;
clear all;

bits=[0 1 0 0 1 0 1 1 1 1 0];
bit_dur=2;
T=length(bits)*bit_dur;
fs=100;
t=0:1/fs:T-(1/fs);

lastbit=1;
for i=1:length(bits)
    if bits(i)==0
        x((i-1)*fs*bit_dur+1:i*fs*bit_dur)=0;
    else
        x((i-1)*fs*bit_dur+1:i*fs*bit_dur)=lastbit;
        lastbit=-lastbit;
    end
end
plot(t,x,'linewidth',2);
ylim([-5,5]);
xlim([0,T]);

%demodulation
for i=1:length(x)/(fs*bit_dur)
    if x((i-1)*fs*bit_dur+1:i*fs*bit_dur)==zeros(1,fs*bit_dur)
        disp(0)
    else
        disp(1)
    end
end

        