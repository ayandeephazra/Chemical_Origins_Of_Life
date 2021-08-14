import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from ode_helpers import state_plotter
import numpy as np


def f(t, y, c):
    dydt = [0, 7 * y[3] - 19.5 * y[1] ** 2 - 9.5 * y[1] * y[2] + 4.5 * y[5] - 10 * y[1] * y[5] - 9.75 * y[1] * y[3] - 9.75 * y[1] * y[4],
            9 * y[4] - 16 * y[2] ** 2 - 9.5 * y[1] * y[2] + 4.5 * y[5] - 10 * y[1] * y[2] - 4 * y[5] * y[2] - 1.75 * y[2] * y[4],
            9.75 * y[1] ** 2 - 3.5 * y[3] + 9.75 * y[1] * y[3] - 19.5 * y[3] ** 2 - 10 * y[2] * y[3],
            8 * y[2] ** 2 - 4.5 * y[4] - 9.75 * y[1] * y[4] - 1.75 * y[2] * y[4],
            9.5 * y[1] * y[2] - 4.5 * y[5] - 10 * y[1] * y[5] - 4 * y[5] * y[2]]
    return dydt

tspan = np.linspace(0, 5, 5)
yinit = [0, 0.1, 0, 0, 0, 0]
c = [4, 3, -2, 0.5]

sol = solve_ivp(lambda t, y: f(t, y, c),
                [tspan[0], tspan[-1]], yinit, t_eval=tspan, rtol = 1e-5)

print(sol.y)
state_plotter(sol.t, sol.y, 1)
