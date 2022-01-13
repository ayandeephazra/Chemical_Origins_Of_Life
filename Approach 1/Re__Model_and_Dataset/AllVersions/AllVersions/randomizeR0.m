function new_r0 = randomizeR0(old_r0,max_r0)
%RANDOMIZER0 Randomly increment/decrement the intial values for the Monte
%Carlo algorithm

r_size = size(old_r0.r,2);
% If things seem to be crashing to zero more often than they should, try
% adding a fixed number (ie +1) to the random number generator.
rands = randn(1,r_size);

new_r0 = old_r0.r + rands;
% If a value goes below 0, set it to zero.(Could cycle around, but I want 0
% to be an accessible parameter value
new_r0 = max(new_r0,0);
% If a values goes above the max parameter value, set it to the max
% parameter value.
new_r0 = min(new_r0,max_r0);

end

