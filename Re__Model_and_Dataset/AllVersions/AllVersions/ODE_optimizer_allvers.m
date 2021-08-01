%% Documentation used for this code is linked below.
% https://www.mathworks.com/help/optim/ug/fit-ode-problem-based-least-squares.html

% Note: Must use MATLAB 2019a

% Note: Would like to figure out how to increase the number of
% MaximumFunctionEvaluations, but MATLAB makes this seemingly simple task
% horrifically difficult for some reason.

clear;

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

%% Optimization variable (name, dimensionality, lb, ub)
r_size = 22;    % Number of parameters - change to match number of parameters trying to fit in reactions
rmax = 10; % Maximum parameter value
r = optimvar('r',r_size,"LowerBound",0,"UpperBound",rmax);

r0.r = repmat(5,1,r_size);

%% Make function out of ODE solving; declare the objective function
myfcn_100 = fcn2optimexpr(@SolveWithFoundParams,r,tspan,y0_100);
myfcn_90 = fcn2optimexpr(@SolveWithFoundParams,r,tspan,y0_90);
myfcn_75 = fcn2optimexpr(@SolveWithFoundParams,r,tspan,y0_75);
myfcn_50 = fcn2optimexpr(@SolveWithFoundParams,r,tspan,y0_50);
myfcn_25 = fcn2optimexpr(@SolveWithFoundParams,r,tspan,y0_25);
myfcn_10 = fcn2optimexpr(@SolveWithFoundParams,r,tspan,y0_10);
myfcn_0 = fcn2optimexpr(@SolveWithFoundParams,r,tspan,y0_0);

myfcn_lowC_50 = fcn2optimexpr(@SolveWithFoundParams,r,tspan,y0_lowC_50);
myfcn_lowC_25 = fcn2optimexpr(@SolveWithFoundParams,r,tspan,y0_lowC_25);
myfcn_lowC_0 = fcn2optimexpr(@SolveWithFoundParams,r,tspan,y0_lowC_0);

%% Monte Carlo Procedure
% For now I'm just going to go for a fixed number of iterations rather than a
% convergence criteria, since my sumsq differences are so different from
% experiment to experiment.
mc_iterations = 5;
% Lower accpetance term -> less accepted steps that are unfavorable.
acceptance_term = 0.01;

% Solve the first version of the problem
obj = sum(sum(((myfcn_100-expt_y_vers(:,:,1))./sigma_vers(:,:,1)).^2)) + ...
    sum(sum(((myfcn_90-expt_y_vers(:,:,2))./sigma_vers(:,:,2)).^2)) + ...
    sum(sum(((myfcn_75-expt_y_vers(:,:,3))./sigma_vers(:,:,3)).^2)) + ...
    sum(sum(((myfcn_50-expt_y_vers(:,:,4))./sigma_vers(:,:,4)).^2)) + ...
    sum(sum(((myfcn_25-expt_y_vers(:,:,5))./sigma_vers(:,:,5)).^2)) + ...
    sum(sum(((myfcn_10-expt_y_vers(:,:,6))./sigma_vers(:,:,6)).^2)) + ...
    sum(sum(((myfcn_0-expt_y_vers(:,:,7))./sigma_vers(:,:,7)).^2)) + ...
    sum(sum(((myfcn_lowC_50-expt_y_vers(:,:,8))./sigma_vers(:,:,8)).^2)) + ...
    sum(sum(((myfcn_lowC_25-expt_y_vers(:,:,9))./sigma_vers(:,:,9)).^2)) + ...
    sum(sum(((myfcn_lowC_0-expt_y_vers(:,:,10))./sigma_vers(:,:,10)).^2));

prob = optimproblem("Objective",obj);
[rsol,error] = solve(prob,r0);
error_steps = {error};
r0_steps = {r0.r};
r_steps = {rsol.r};

for i = 1:mc_iterations
   % Save the original related values
   old_r0 = r0.r;
   old_error = error;
   old_rsol = rsol.r;
  
   % Randomly increment r0 and resolve the problem
   r0.r = randomizeR0(r0,rmax);
   [rsol,error] = solve(prob,r0);
   
   % If the values with the new r0 are worse than the old values, revert to
   % the old values, unless they're accepted within some threshold
   % proportional to how bad they actually are
   % Second and argument should usually just automatically be true, so that
   % the new error being greater than the old error is enough to switch
   % back to the old error. However, on occasion, this term should flip to
   % false and cause the and statement to fail, allowing an unfavorable
   % change to stick
   if error > old_error && abs(randn) > acceptance_term*(old_error/error)^2
      r0.r = old_r0;
      error = old_error;
      rsol.r = old_rsol;
   else
       % Otherwise keep new values and mark that a step has been kept
       % Purely for debugging/progress tracking
      error_steps(end+1) = {error};
      r0_steps(end+1) = {r0.r};
      r_steps(end+1) = {rsol.r};
   end
end

%% After finishing the MC algorithm, solve for multiple experimental variations

samples = 3;  % Number of times to add noise to the experimental data and resolve
solved_params = zeros(samples,r_size); % saves the parameter values from each solve
expt_variations = addDataNoise(expt_y_vers,sigma_vers,samples); % Save the experimental noise conditions that go with each set of parameters just in case

%% Make the first run the experimental data with no additional variations
% Specifically, whatever the solution was to final accepted MC step.

% Apparently at least this does need to be here, or at least the problem
% redefintion does. I have no idea why, but that's what was causing my
% issue with r0 not moving properly between sections.

obj = sum(sum(((myfcn_100-expt_y_vers(:,:,1))./sigma_vers(:,:,1)).^2)) + ...
    sum(sum(((myfcn_90-expt_y_vers(:,:,2))./sigma_vers(:,:,2)).^2)) + ...
    sum(sum(((myfcn_75-expt_y_vers(:,:,3))./sigma_vers(:,:,3)).^2)) + ...
    sum(sum(((myfcn_50-expt_y_vers(:,:,4))./sigma_vers(:,:,4)).^2)) + ...
    sum(sum(((myfcn_25-expt_y_vers(:,:,5))./sigma_vers(:,:,5)).^2)) + ...
    sum(sum(((myfcn_10-expt_y_vers(:,:,6))./sigma_vers(:,:,6)).^2)) + ...
    sum(sum(((myfcn_0-expt_y_vers(:,:,7))./sigma_vers(:,:,7)).^2)) + ...
    sum(sum(((myfcn_lowC_50-expt_y_vers(:,:,8))./sigma_vers(:,:,8)).^2)) + ...
    sum(sum(((myfcn_lowC_25-expt_y_vers(:,:,9))./sigma_vers(:,:,9)).^2)) + ...
    sum(sum(((myfcn_lowC_0-expt_y_vers(:,:,10))./sigma_vers(:,:,10)).^2));
[rsol, error] = solve(prob,r0);
expt_variations(:,:,1) = expt_y;
solved_params(1,:) = rsol.r;

%%
for i = 2:samples
    temp_expt_y_vers = expt_variations(:,:,:,i);
    
    obj = sum(sum(((myfcn_100-temp_expt_y_vers(:,:,1))./sigma_vers(:,:,1)).^2)) + ...
    sum(sum(((myfcn_90-temp_expt_y_vers(:,:,2))./sigma_vers(:,:,2)).^2)) + ...
    sum(sum(((myfcn_75-temp_expt_y_vers(:,:,3))./sigma_vers(:,:,3)).^2)) + ...
    sum(sum(((myfcn_50-temp_expt_y_vers(:,:,4))./sigma_vers(:,:,4)).^2)) + ...
    sum(sum(((myfcn_25-temp_expt_y_vers(:,:,5))./sigma_vers(:,:,5)).^2)) + ...
    sum(sum(((myfcn_10-temp_expt_y_vers(:,:,6))./sigma_vers(:,:,6)).^2)) + ...
    sum(sum(((myfcn_0-temp_expt_y_vers(:,:,7))./sigma_vers(:,:,7)).^2)) + ...
    sum(sum(((myfcn_lowC_50-temp_expt_y_vers(:,:,8))./sigma_vers(:,:,8)).^2)) + ...
    sum(sum(((myfcn_lowC_25-temp_expt_y_vers(:,:,9))./sigma_vers(:,:,9)).^2)) + ...
    sum(sum(((myfcn_lowC_0-temp_expt_y_vers(:,:,10))./sigma_vers(:,:,10)).^2));
    
    prob = optimproblem("Objective",obj);
    [rsol,error] = solve(prob,r0);
    solved_params(i,:) = rsol.r;
end

sol = mean(solved_params);
sdsol = std(solved_params);

save('NewFinalFit')
%% Calculate error - tried to do this in SolvedModel, but getting differences in error numbers in LOO tests
% Seems to work fine in this version
solvals = zeros(size(expt_y_vers));
y0s = [y0_100;y0_90;y0_75;y0_50;y0_25;y0_10;y0_0;y0_lowC_50;y0_lowC_25;y0_lowC_0];

% For each dataset, solve the ODE for the fitted parameters and evaluate
% the points of that ODE at the same times as the experimental data was
% collected. Save those points for plotting.
for i = 1:datasets
    tempsol = ode15s(@(t,y)reactions(t,y,rsol.r),tspan,y0s(i,:));
    tempsolvals = deval(tempsol,tspan);
    solvals(:,:,i) = tempsolvals;
end

% error = 7.1714e+08, testerror = 7.7644e+08
% Maybe fixable if I replace expt_y_vers with the last step of
% expt_variations? That should be the next thing to try.
testerror = sum(sum(((solvals(:,:,1)-expt_y_vers(:,:,1))./sigma_vers(:,:,1)).^2)) + ...
    sum(sum(((solvals(:,:,2)-expt_y_vers(:,:,2))./sigma_vers(:,:,2)).^2)) + ...
    sum(sum(((solvals(:,:,3)-expt_y_vers(:,:,3))./sigma_vers(:,:,3)).^2)) + ...
    sum(sum(((solvals(:,:,4)-expt_y_vers(:,:,4))./sigma_vers(:,:,4)).^2)) + ...
    sum(sum(((solvals(:,:,5)-expt_y_vers(:,:,5))./sigma_vers(:,:,5)).^2)) + ...
    sum(sum(((solvals(:,:,6)-expt_y_vers(:,:,6))./sigma_vers(:,:,6)).^2)) + ...
    sum(sum(((solvals(:,:,7)-expt_y_vers(:,:,7))./sigma_vers(:,:,7)).^2)) + ...
    sum(sum(((solvals(:,:,8)-expt_y_vers(:,:,8))./sigma_vers(:,:,8)).^2)) + ...
    sum(sum(((solvals(:,:,9)-expt_y_vers(:,:,9))./sigma_vers(:,:,9)).^2)) + ...
    sum(sum(((solvals(:,:,10)-expt_y_vers(:,:,7))./sigma_vers(:,:,10)).^2));