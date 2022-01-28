function dydt = reactions(~,y,r)
%REACTIONS - ODE reaction model
%   Update to show reaction model being used as needed

% First number in zeros() is number of species - figure out how to auto-update if
% possible. Next number is always one.

dydt = zeros(10,1);

% species = {'G','A','GG', 'AA', 'GA/AG','GGA/GAG/AGG','GGG','GGGG','AAG/AGA/GAA','AAA'};
% Edit r() to add/remove parameters
dydt(1) = r(2)*2*y(3)-r(1)*2*y(1)^2-r(5)*y(1)*y(2)+r(6)*y(5)-r(7)*y(1)*y(5)+r(8)*y(6)-r(9)*y(1)*y(3)+r(10)*y(7)-r(11)*y(7)*y(1)+r(12)*y(8)-r(17)*y(1)*y(4)+r(18)*y(9); % G
dydt(2) = r(4)*2*y(4)-r(3)*2*y(2)^2-r(5)*y(1)*y(2)+r(6)*y(5)-r(15)*y(3)*y(2)+r(16)*y(6)-r(19)*y(5)*y(2)+r(20)*y(9)-r(21)*y(2)*y(4)+r(22)*y(10); % A
dydt(3) = r(1)*y(1)^2 - r(2)*y(3)-r(9)*y(1)*y(3)+r(10)*y(7)-2*r(13)*y(3)^2+2*r(14)*y(8)-r(15)*y(3)*y(2)+r(16)*y(6); % GG
dydt(4) = r(3)*y(2)^2 - r(4)*y(4)-r(17)*y(1)*y(4)+r(18)*y(9)-r(21)*y(2)*y(4)+r(22)*y(10); % AA
dydt(5) = r(5)*y(1)*y(2)-r(6)*y(5)-r(7)*y(5)*y(1)+r(8)*y(6)-r(19)*y(5)*y(2)+r(20)*y(9); % GA/AG - ignoring ordering because I can't differentiate anyway
dydt(6) = r(7)*y(5)*y(1)-r(8)*y(6)+r(15)*y(3)*y(2)-r(16)*y(6); % GAG/AGG/GGA - ordering is more significant here because it's another path from GA to GG (for example), but I'm going to leave it for now
dydt(7) = r(9)*y(1)*y(3) - r(10)*y(7) - r(11)*y(7)*y(1)+r(12)*y(8); % GGG
dydt(8) = r(11)*y(7)*y(1)-r(12)*y(8)+r(13)*y(3)^2 - r(14)*y(8); % GGGG
dydt(9) = r(17)*y(4)*y(1)-r(18)*y(9)+r(19)*y(5)*y(2)-r(20)*y(9); % AAG/AGA/GAA
dydt(10) = r(21)*y(2)*y(4)-r(22)*y(10); % AAA

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

end

