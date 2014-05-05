clear; close; clc;

%% Load the dataset (save as time and V)
% load('two-tone-basic');
% load('PokemonCenterSong_NoRest');
% load('PokemonBattleSong_NoRest');
load 'PokemonBattle.mat';
% load('PokemonCenterSong.mat');
% load ('TetrisTunes.mat');
% load('Zelda.mat');
% load('Tetris2.mat')
% load('PokemonTheme.mat');


%% Plot the data - zoom in for detail
dot = 15;
plot(time, V, 'k.', 'Markersize', dot);

%% Make a new dataset
seek_index = 1;
time_new = [0];
V_new = [V(1)];
freq = 10000; % Hz
timestep = 1/freq; % seconds
while (time_new(end) < (time(end) - 0.05))
    time_new = [time_new, time_new(end) + timestep];
    flag = 1;
    seeker = [10, 0];
    while (flag)
        seeker(2) = abs(time(seek_index) - time_new(end));
        if (seeker(2) > seeker(1))
            flag = 0;
            seek_index = seek_index - 1;
        else
            seek_index = seek_index + 1;
            seeker(1) = seeker(2);
        end
    end
    V_new = [V_new, V(seek_index)];
end

%% Plot new data - zoom in to chec evenness of new data
hold on;
plot(time_new, V_new, 'g.', 'Markersize', dot);
xlabel('Time (s)')


%% Play the new data
sound(V_new, freq);