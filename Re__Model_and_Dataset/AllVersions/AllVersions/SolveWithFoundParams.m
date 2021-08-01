function solpts = SolveWithFoundParams(r, tspan, y0)
%SOLVEWITHFOUNDPARAMS a MATLAB function that computes the ODE solution using parameters r

sol = ode15s(@(t,y)reactions(t,y,r),tspan,y0);
solpts = deval(sol,tspan);

end

