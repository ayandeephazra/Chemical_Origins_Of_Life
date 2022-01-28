% Load experimental data for plotting
%% Load sample data

% Load one dataset to set sizes
ExptData = load('100-0.mat');
expt_time = ExptData.GAFittingCleanExperimentalData{:,1}; % Experimental timesteps
expt_y = ExptData.GAFittingCleanExperimentalData{:,2:11}; 
expt_y = expt_y.';

% Declare the number of datasets to include and load/process them
datasets = 10;
expt_y_vers = zeros(size(expt_y,1),size(expt_y,2),datasets);
expt_y_vers(:,:,1) = expt_y;

ExptData2 = load('90-10.mat');
expt_y_vers(:,:,2) = ExptData2.GAFittingCleanExperimentalData1{:,2:11}.';
% I'm sure there's a better way to do this, I'm not sure what it is
ExptData3 = load('75-25.mat');
expt_y_vers(:,:,3) = ExptData3.GAFittingCleanExperimentalData{:,2:11}.';
ExptData4 = load('50-50.mat');
expt_y_vers(:,:,4) = ExptData4.GAFittingCleanExperimentalData{:,2:11}.';
ExptData5 = load('25-75.mat');
expt_y_vers(:,:,5) = ExptData5.GAFittingCleanExperimentalData1{:,2:11}.';
ExptData6 = load('10-90.mat');
expt_y_vers(:,:,6) = ExptData6.GAFittingCleanExperimentalData{:,2:11}.';
ExptData7 = load('0-100.mat');
expt_y_vers(:,:,7) = ExptData7.GAFittingCleanExperimentalData{:,2:11}.';
ExptData8 = load('LowC_50-0.mat');
expt_y_vers(:,:,8) = ExptData8.GAFittingCleanExperimentalData{:,2:11}.';
ExptData9 = load('LowC_25-25.mat');
expt_y_vers(:,:,9) = ExptData9.GAFittingCleanExperimentalData{:,2:11}.';
ExptData10 = load('LowC_0-50.mat');
expt_y_vers(:,:,10) = ExptData10.GAFittingCleanExperimentalData{:,2:11}.';

% Repeat the loading/processing steps for the appropriate std dev matrices
sigma_vers = zeros(size(expt_y,1),size(expt_y,2),datasets);

ExptStdDev = load('100-0_StdDev.mat');
sigma_vers(:,:,1) = ExptStdDev.GAFittingCleanExperimentalData{:,2:11}.';
ExptStdDev2 = load('90-10_StdDev.mat');
sigma_vers(:,:,2) = ExptStdDev2.GAFittingCleanExperimentalData{:,2:11}.';
ExptStdDev3 = load('75-25_StdDev.mat');
sigma_vers(:,:,3) = ExptStdDev3.GAFittingCleanExperimentalData{:,2:11}.';
ExptStdDev4 = load('50-50_StdDev.mat');
sigma_vers(:,:,4) = ExptStdDev4.GAFittingCleanExperimentalData{:,2:11}.';
ExptStdDev5 = load('25-75_StdDev.mat');
sigma_vers(:,:,5) = ExptStdDev5.GAFittingCleanExperimentalData1{:,2:11}.';
ExptStdDev6 = load('10-90_StdDev.mat');
sigma_vers(:,:,6) = ExptStdDev6.GAFittingCleanExperimentalData{:,2:11}.';
ExptStdDev7 = load('0-100_StdDev.mat');
sigma_vers(:,:,7) = ExptStdDev7.GAFittingCleanExperimentalData{:,2:11}.';
ExptStdDev8 = load('LowC_50-0_StdDev.mat');
sigma_vers(:,:,8) = ExptStdDev8.GAFittingCleanExperimentalData{:,2:11}.';
ExptStdDev9 = load('LowC_25-25_StdDev.mat');
sigma_vers(:,:,9) = ExptStdDev9.GAFittingCleanExperimentalData{:,2:11}.';
ExptStdDev10 = load('LowC_0-50_StdDev.mat');
sigma_vers(:,:,10) = ExptStdDev10.GAFittingCleanExperimentalData{:,2:11}.';

sigma_vers = max(sigma_vers,1*10^-8);


%% Solve model for parameters generated from the average of solved_params
params = sol;
% params = rsol.r;
% params = r_steps{end};
% params = r0.r;

%% Declare initial concentrations and time span
% y0 = expt_y(:,1).'; % Initial concentrations- try changing to theoretical inital concentrations at some point, espeically for alanine.
% Create multiple y0s if fitting data from multiple starting points
y0_100 = [0.1 0 0 0 0 0 0 0 0 0];
y0_90 = [0.09 0.01 0 0 0 0 0 0 0 0];
y0_75 = [0.075 0.025 0 0 0 0 0 0 0 0];
y0_50 = [0.050 0.050 0 0 0 0 0 0 0 0];
y0_25 = [0.025 0.075 0 0 0 0 0 0 0 0];
y0_10 = [0.01 0.09 0 0 0 0 0 0 0 0];
y0_0 = [0 0.1 0 0 0 0 0 0 0 0];
y0_lowC_50 = [0.05 0 0 0 0 0 0 0 0 0];
y0_lowC_25 = [0.025 0.025 0 0 0 0 0 0 0 0];
y0_lowC_0 = [0 0.05 0 0 0 0 0 0 0 0];

tspan = expt_time;
y0s = [y0_100;y0_90;y0_75;y0_50;y0_25;y0_10;y0_0;y0_lowC_50;y0_lowC_25;y0_lowC_0];


%% Solve model for parameters generated from the averaged of solved_params
params = sol;

solvals = zeros(size(expt_y_vers));
for i = 1:datasets
    tempsol = ode15s(@(t,y)reactions(t,y,params),tspan,y0s(i,:));
    tempsolvals = deval(tempsol,tspan);
    solvals(:,:,i) = tempsolvals;
end

error = sum(sum(((solvals(:,:,1)-expt_y_vers(:,:,1))./sigma_vers(:,:,1)).^2)) + ...
    sum(sum(((solvals(:,:,2)-expt_y_vers(:,:,2))./sigma_vers(:,:,2)).^2)) + ...
    sum(sum(((solvals(:,:,3)-expt_y_vers(:,:,3))./sigma_vers(:,:,3)).^2)) + ...
    sum(sum(((solvals(:,:,4)-expt_y_vers(:,:,4))./sigma_vers(:,:,4)).^2)) + ...
    sum(sum(((solvals(:,:,5)-expt_y_vers(:,:,5))./sigma_vers(:,:,5)).^2)) + ...
    sum(sum(((solvals(:,:,6)-expt_y_vers(:,:,6))./sigma_vers(:,:,6)).^2)) + ...
    sum(sum(((solvals(:,:,7)-expt_y_vers(:,:,7))./sigma_vers(:,:,7)).^2)) + ...
    sum(sum(((solvals(:,:,8)-expt_y_vers(:,:,8))./sigma_vers(:,:,8)).^2)) + ...
    sum(sum(((solvals(:,:,9)-expt_y_vers(:,:,9))./sigma_vers(:,:,9)).^2)) + ...
    sum(sum(((solvals(:,:,10)-expt_y_vers(:,:,7))./sigma_vers(:,:,10)).^2));

sumsq = sum(sum((solvals(:,:,1)-expt_y_vers(:,:,1)).^2)) + ...
    sum(sum((solvals(:,:,2)-expt_y_vers(:,:,2)).^2)) + ...
    sum(sum((solvals(:,:,3)-expt_y_vers(:,:,3)).^2)) + ...
    sum(sum((solvals(:,:,4)-expt_y_vers(:,:,4)).^2)) + ...
    sum(sum((solvals(:,:,5)-expt_y_vers(:,:,5)).^2)) + ...
    sum(sum((solvals(:,:,6)-expt_y_vers(:,:,6)).^2)) + ...
    sum(sum((solvals(:,:,7)-expt_y_vers(:,:,7)).^2)) + ...
    sum(sum((solvals(:,:,8)-expt_y_vers(:,:,8)).^2)) + ...
    sum(sum((solvals(:,:,9)-expt_y_vers(:,:,9)).^2)) + ...
    sum(sum((solvals(:,:,10)-expt_y_vers(:,:,10)).^2));
species = ["G", "A", "GG", "AA", "GA/AG", "GAG/AGG/GGA", "GGG", "GGGG", "AAG/GAA/AGA", "AAA"];
datalist = ["100-0","90-10","75-25","50-50","25-75","10-90","0-100","LowC-100-0", "LowC-50-50","LowC-0-100"];

%% Plotting solved data on top of experimental data
for j = 1:datasets
    figure(j);
    sgtitle(datalist(j));
    for i = 1:length(species)
        subplot(ceil(length(species)/2),2,i);
        plot(tspan,solvals(i,:,j),'blue','LineWidth',2);
        hold on;
        errorbar(tspan,expt_y_vers(i,:,j),sigma_vers(i,:,j),'red');
        title(char(species(i)));
%         legend('Model','Experiment','Location','best');
        hold off;
    end
end