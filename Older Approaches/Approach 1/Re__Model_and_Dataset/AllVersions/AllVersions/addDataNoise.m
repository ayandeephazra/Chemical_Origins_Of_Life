function noisy_expt_data = addDataNoise(expt_data,std_dev,samples)
% Add noise to the data for uncertainty quantification
%   Pick from within a Gaussian somehow described by the experimental
%   standard deviation to add noise to the experimental data
%       expt_data and std_dev are matrices from experimental results
%       samples is the number of random noisy data sets to generate

row = size(expt_data,1);
col = size(expt_data,2);
d = size(expt_data,3); % number of datasets being simultaneously fit

% noise_expt_data is a 3D matrix: row x column x samples
% Now for simultaneous fitting: row x columns x datasets x samples
noisy_expt_data = repmat(expt_data,[1,1,1,samples]);

sigma_repeats = repmat(std_dev,[1,1,1,samples]);
noise_matrix = sigma_repeats.*randn(row,col,d,samples);

noisy_expt_data = noisy_expt_data + noise_matrix;

% This line sets any negative values equal to zero to prevent any
% accidental physically unrealistic results
noisy_expt_data = max(noisy_expt_data,0);
