import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from ode_helpers import state_plotter
from noise import noise
import numpy as np
import pysindy as ps
from scipy.integrate import odeint

fixed_cond_data = 0
fixed_cond_noise = 0


def model(n, t_span, sd):
    def original_model(y, t):

        c = [0, 9.75, 3.5, 8, 4.5, 9.5, 4.5, 10, 3, 9.75, 8, 0.5, 2, 9.75, 0.75, 10, 0, 9.75, 0.25, 4, 5, 1.75, 6.5]

        dydt = [0,
                c[2] * 2 * y[3] - c[1] * 2 * y[1] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
                c[4] * 2 * y[4] - c[3] * 2 * y[2] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
                c[1] * y[1] ** 2 - c[2] * y[3],
                c[3] * y[2] ** 2 - c[4] * y[4],
                c[5] * y[1] * y[2] - c[6] * y[5]]
        return dydt

    def solver(t_span, yinit=[0, 0.075, 0.025, 0.01, 0.005, 0.005]):
        # tspan = np.linspace(0, n - 1, n)
        # yinit = [0, 0.075, 0.025, 0, 0, 0]
        # c = [0, 9.75, 3.5, 8, 4.5, 9.5, 4.5, 10, 3, 9.75, 8, 0.5, 2, 9.75, 0.75, 10, 0, 9.75, 0.25, 4, 5, 1.75, 6.5]

        # sol = solve_ivp(original_model, [t_span[0], t_span[-1]], yinit, t_eval=t_span, rtol=1e-5)

        sol = odeint(original_model, yinit, t_span)

        # state_plotter(sol.t, sol.y, 1, True)

        return t_span, sol

    def mass_balance(t_data, y_data, y_noise_data, plot_if_true):
        if plot_if_true:
            A_bal = y_noise_data[1] + 2 * y_noise_data[3] + y_noise_data[5]

            B_bal = y_noise_data[2] + 2 * y_noise_data[4] + y_noise_data[5]

            # print(y_data.shape, t_data.shape, A_bal.shape)
            plt.plot(t_data, A_bal)
            plt.plot(t_data, B_bal)

            upper_75 = [1.2 * 0.075] * len(t_data)
            lower_75 = [0.8 * 0.075] * len(t_data)
            upper_25 = [1.2 * 0.025] * len(t_data)
            lower_25 = [0.8 * 0.025] * len(t_data)

            plt.plot(t_data, upper_25)
            plt.plot(t_data, lower_75)
            plt.plot(t_data, upper_75)
            plt.plot(t_data, lower_25)
            plt.show()

    def ic():
        scale = np.random.uniform(1, n % 5, n)
        temp = scale[1] * np.random.normal(10, 3, size=6)
        temp[temp < 0] = 0
        temp[0] = 0
        return temp

    def datasets(yinit, selection):
        global fixed_cond_data
        global fixed_cond_noise

        # yinit = [0, 0.075, 0.025, 0, 0, 0]
        if selection == 2:
            if fixed_cond_data == 0:
                yinit = [0, 0.09, 0.01, 0, 0, 0]
                fixed_cond_data = 1
            elif fixed_cond_data == 1:
                yinit = [0, 0.075, 0.025, 0, 0, 0]
                fixed_cond_data = 2
            elif fixed_cond_data == 2:
                yinit = [0, 0.05, 0.05, 0, 0, 0]
                fixed_cond_data = 3
            elif fixed_cond_data == 3:
                yinit = [0, 0.025, 0.075, 0, 0, 0]
                fixed_cond_data = 4
            elif fixed_cond_data == 4:
                yinit = [0, 0.01, 0.09, 0, 0, 0]
                fixed_cond_data = 5
                
        if selection == 3:
            if fixed_cond_noise == 0:
                yinit = [0, 0.09, 0.01, 0, 0, 0]
                fixed_cond_noise = 1
            elif fixed_cond_noise == 1:
                yinit = [0, 0.075, 0.025, 0, 0, 0]
                fixed_cond_noise = 2
            elif fixed_cond_noise == 2:
                yinit = [0, 0.05, 0.05, 0, 0, 0]
                fixed_cond_noise = 3
            elif fixed_cond_noise == 3:
                yinit = [0, 0.025, 0.075, 0, 0, 0]
                fixed_cond_noise = 4
            elif fixed_cond_noise == 4:
                yinit = [0, 0.01, 0.09, 0, 0, 0]
                fixed_cond_noise = 5

        t_data_, y_data_ = solver(t_span, yinit)
        # change sigma here,
        # change to y_data_.shape
        y_noise_data_ = y_data_ + y_data_ * np.random.normal(0, sd, size=y_data_.shape)
        # state_plotter(t_data_, y_noise_data_, 1, True, noise=1, printnoise=0)
        # True to do mass balance calc and display plot, else not
        mass_balance(t_data_, y_data_, y_noise_data_, False)

        if selection == 1:
            return t_data_
        if selection == 2:
            return y_data_
        if selection == 3:
            return y_noise_data_

        # return t_data_, y_data_, y_noise_data_

    scale = np.random.uniform(1, n % 5, n)
    data = [datasets(ic(), 2) for i in range(n)]
    noise_data = [datasets(ic(), 3) for i in range(n)]

    retmodel = ps.SINDy(optimizer=ps.STLSQ(alpha=250, threshold=3, max_iter=15),
                        feature_library=ps.PolynomialLibrary(degree=2, include_bias=False))

    return data, noise_data, retmodel
