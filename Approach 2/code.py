import pysindy as ps
import numpy as np
from scipy.integrate import odeint
from ode_helpers import state_plotter

c = [0, 9.75, 3.5, 8, 4.5, 9.5, 4.5, 10, 3, 9.75, 8, 0.5, 2, 9.75, 0.75, 10, 0, 9.75, 0.25, 4, 5, 1.75, 6.5]


def ayan(y, t):
    dydt = [1, c[2] * 2 * y[3] - c[1] * 2 * y[1] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
            c[4] * 2 * y[4] - c[3] * 2 * y[2] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
            c[1] * y[1] ** 2 - c[2] * y[3],
            c[3] * y[2] ** 2 - c[4] * y[4],
            c[5] * y[1] * y[2] - c[6] * y[5]]
    return dydt


n = 60
t_span = np.arange(0, 1, 0.001)

np.random.seed(6)

scale = np.random.uniform(1, n % 5, n)

init = [scale[1] * np.random.normal(10, 3, size=6) for i in range(n)]

z = [odeint(ayan, i, t_span) for i in init]

model = ps.SINDy(optimizer=ps.STLSQ(alpha=250, threshold=2),
                 feature_library=ps.PolynomialLibrary(degree=2, include_bias=False))

model.fit(z, t_span, multiple_trajectories=True)

model.print()

# enter starting condition you want to simulate
x = model.simulate([0, 0.09, 0.01, 0, 0, 0], t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

x = model.simulate([0, 0.075, 0.025, 0, 0, 0], t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

x = model.simulate([0, 0.05, 0.05, 0, 0, 0], t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

x = model.simulate([0, 0.025, 0.075, 0, 0, 0], t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

x = model.simulate([0, 0.01, 0.09, 0, 0, 0], t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)