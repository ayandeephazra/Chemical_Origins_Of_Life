import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from ode_helpers import state_plotter
import numpy as np

np.set_printoptions(suppress=True)


# hard coded dydt for first 5 params

def f(t, y, c):
    dydt = [1,
            c[2] * 2 * y[3] - c[1] * 2 * y[1] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5] - c[7] * y[1] * y[5] - c[9] * y[1] * y[3] - c[17] * y[1] * y[4],
            c[4] * 2 * y[4] - c[3] * 2 * y[2] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5] - c[15] * y[1] * y[2] - c[19] * y[5] * y[2] - c[21] * y[2] * y[4],
            c[1] * y[1] ** 2 - c[2] * y[3] + c[9] * y[1] * y[3] - 2 * c[13] * y[3] ** 2 - c[15] * y[2] * y[3],
            c[3] * y[2] ** 2 - c[4] * y[4] - c[17] * y[1] * y[4] - c[21] * y[2] * y[4],
            c[5] * y[1] * y[2] - c[6] * y[5] - c[7] * y[1] * y[5] - c[19] * y[5] * y[2]]
    return dydt


tspan = np.linspace(0, 9, 10)
yinit = [0, 0.075, 0.025, 0, 0, 0]
c = [0, 9.75, 3.5, 8, 4.5, 9.5, 4.5, 10, 3, 9.75, 8, 0.5, 2, 9.75, 0.75, 10, 0, 9.75, 0.25, 4, 5, 1.75, 6.5]

sol = solve_ivp(lambda t, y: f(t, y, c),
                [tspan[0], tspan[-1]], yinit, t_eval=tspan, rtol=1e-5)
import matplotlib.rcsetup as rcsetup

print(rcsetup.all_backends)
print(sol.y.round(6))
state_plotter(sol.t, sol.y, 1)
