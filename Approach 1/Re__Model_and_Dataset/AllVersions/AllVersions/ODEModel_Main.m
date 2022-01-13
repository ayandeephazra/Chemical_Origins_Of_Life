clear; 

% NOTE: In the future try to use a more logical/systematic method for
% ordering species and reactions, but for now I'm going to try to keep
% things the same as the parameter fitting code.

species = {'G','A','GG', 'AA', 'GA/AG','GGA/GAG/AGG','GGG','GGGG','AAG/AGA/GAA','AAA'}; % Mostly for labelling and record keeping

% Adjust if changing number of y0 conditions run
datasets = 10; 

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

y0s = [y0_100;y0_90;y0_75;y0_50;y0_25;y0_10;y0_0;y0_lowC_50;y0_lowC_25;y0_lowC_0];

tspan = linspace(0,10,5);

% Semi-arbitrarily chosen to be a relatively good match for what I find in
% my fitting results without being literally identical
params = [9.75	3.5	8	4.5	9.5	4.5	10	3	9.75	8	0.5	2	9.75	0.75	10	0	9.75	0.25	4	5	1.75	6.5];

% r(1) = 2G -> GG, r(2) = GG -> 2G
% r(3) = 2A -> AA, r(4) = AA -> 2A
% r(5) = A+G -> AG/GA, r(6) = AG/GA -> G + A
% r(7) = AG/GA + G -> GAG/AGG/GGA, r(8) = GAG/AGG/GGA -> AG/GA + G
% r(9) = G + GG -> GGG, r(10) = GGG -> GG + G
% r(11) = GGG+G -> GGGG, r(12) = GGGG -> GGG + G
% r(13) = GG+GG -> GGGG, r(14) = GGGG -> GG + GG
% r(15) = GG + A -> GGA/AGG, r(16) = GGA/AGG -> GG + A
% r(17) = AA + G -> AAG/GAA, r(18) = AAG/GAA -> AA + G
% r(19) = GA/AG + A -> GAA/AGA/AAG, r(20) = GAA/AGA/AAG -> GA/AG + A
% r(21) = AA + A -> AAA, r(22) = AAA -> AA + A

%% Solve and plot true solution
% This simulated data can be fit perfectly (or close to it) if plugged back
% into the ParameterSolver

solvals = zeros(size(y0s,1),size(tspan,2),datasets);
for i = 1:datasets
    tempsol = ode15s(@(t,y)reactions(t,y,params),tspan,y0s(i,:));
    tempsolvals = deval(tempsol,tspan);
    solvals(:,:,i) = tempsolvals;
end

datalist = ["100-0","90-10","75-25","50-50","25-75","10-90","0-100","LowC-100-0", "LowC-50-50","LowC-0-100"];

for j = 1:datasets
    figure(j);
    sgtitle(datalist(j));
    for i = 1:length(species)
        subplot(ceil(length(species)/2),2,i);
        plot(tspan,solvals(i,:,j),'blue','LineWidth',2);
        hold on;
%         errorbar(tspan,expt_y_vers(i,:,j),sigma_vers(i,:,j),'red');
        title(char(species(i)));
%         legend('Model','Experiment','Location','best');
        hold off;
    end
end
