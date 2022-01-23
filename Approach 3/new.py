import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from ode_helpers import state_plotter
from noise import noise
import numpy as np


def original_model(t, y):
    c = [0, 9.75, 3.5, 8, 4.5, 9.5, 4.5, 10, 3, 9.75, 8, 0.5, 2, 9.75, 0.75, 10, 0, 9.75, 0.25, 4, 5, 1.75, 6.5]
    dydt = [1,
            c[2] * 2 * y[3] - c[1] * 2 * y[1] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
            c[4] * 2 * y[4] - c[3] * 2 * y[2] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
            c[1] * y[1] ** 2 - c[2] * y[3],
            c[3] * y[2] ** 2 - c[4] * y[4],
            c[5] * y[1] * y[2] - c[6] * y[5]]
    return dydt


def solver(n, yinit=[0, 0.075, 0.025, 0.01, 0.005, 0.005]):
    tspan = np.linspace(0, n - 1, n * 50)
    # yinit = [0, 0.075, 0.025, 0, 0, 0]
    # c = [0, 9.75, 3.5, 8, 4.5, 9.5, 4.5, 10, 3, 9.75, 8, 0.5, 2, 9.75, 0.75, 10, 0, 9.75, 0.25, 4, 5, 1.75, 6.5]

    sol = solve_ivp(original_model, [tspan[0], tspan[-1]], yinit, t_eval=tspan, rtol=1e-5)

    # print(sol.y.__class__)
    # print(sol.y.round(6))
    state_plotter(sol.t, sol.y, 1, True)

    return sol.t, sol.y


t_data, y_data = solver(2, yinit=[0, 0.075, 0.025, 0, 0, 0])

y_noise_data = y_data + y_data * np.random.normal(0, 0.1, size=y_data.shape)

A_bal = y_noise_data[1] + 2 * y_noise_data[3] + y_noise_data[5]

B_bal = y_noise_data[2] + 2 * y_noise_data[4] + y_noise_data[5]

state_plotter(t_data, y_noise_data, 1, True)

print(y_data.shape, t_data.shape, A_bal.shape)
plt.plot(t_data, A_bal)
plt.plot(t_data, B_bal)

upper_75 = [1.2*0.075]*len(t_data)
lower_75 = [0.8*0.075]*len(t_data)
upper_25 = [1.2*0.025]*len(t_data)
lower_25 = [0.8*0.025]*len(t_data)

plt.plot(t_data, upper_25)
plt.plot(t_data, lower_75)
plt.plot(t_data, upper_75)
plt.plot(t_data, lower_25)


plt.show()
