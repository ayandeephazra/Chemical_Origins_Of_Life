import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from ode_helpers import state_plotter
import numpy as np

np.set_printoptions(suppress=True)
c = [0, 9.75, 3.5, 8, 4.5, 9.5, 4.5, 10, 3, 9.75, 8, 0.5, 2, 9.75, 0.75, 10, 0, 9.75, 0.25, 4, 5, 1.75, 6.5]


def f(t, y):
    dydt = [1, c[2] * 2 * y[3] - c[1] * 2 * y[1] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
            c[4] * 2 * y[4] - c[3] * 2 * y[2] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
            c[1] * y[1] ** 2 - c[2] * y[3],
            c[3] * y[2] ** 2 - c[4] * y[4],
            c[5] * y[1] * y[2] - c[6] * y[5]]
    return dydt


# number of samples, say p, p*n
def solver(n, yinit=[0, 0.075, 0.025, 0, 0, 0]):
    tspan = np.linspace(0, (10*(n - 1) / 1000), 10*n)
    yinit = [0, 0.09, 0.01, 0, 0, 0]

    sol = solve_ivp(f, [0, 1], yinit, dense_output=True, t_eval=tspan)

    print(tspan)
    state_plotter(sol.t, sol.y, 1, True)

    return sol.y.T[:, 1:]


solver(1000)
