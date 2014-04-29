clc;close;clear;
load('VinPulse.mat');
plot(time, Vin);
axis([0 .01 -1 6]);
title('Vin vs Time');
xlabel('Vin (Volts)');
ylabel('Time (Seconds)');

%%

clc;close;clear;
load('ROoutput.mat');
plot(time, ROoutput);
axis([0 1 -1 6]);
title('Ring Oscillator Output vs Time');
xlabel('Ring Oscillator Output (Volts)');
ylabel('Time (Seconds)');

%%

fs = 44100;
audiowrite('Output.wav', ROoutput, fs);