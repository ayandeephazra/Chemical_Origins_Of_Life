import pysindy as ps
import numpy as np
from scipy.integrate import odeint
from ode_helpers import state_plotter
from model import model

n = 60
t_span = np.arange(0, 1, 0.001)

ret = model(n, t_span)

model = ret[0]
z = ret[1]

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