import pysindy as ps
import numpy as np
from scipy.integrate import odeint
from ode_helpers import state_plotter
from model import model
from model_with_noise import model_with_noise
from noise import noise

n = 60
t_span = np.arange(0, 1, 0.001)

ret = model(n, t_span)

model = ret[0]
z = ret[1]

model.fit(z, t_span, multiple_trajectories=True)

model.print()

sd = 0.025

# enter starting condition you want to simulate
ic = np.array([0, 0.09, 0.01, 0.00, 0.00, 0])
x = model.simulate(ic, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

#noise1 = noise(1, sd, ic)

#array = np.array(ic + ic*noise1)

#x = model.simulate(array, t_span)

#print(x.round(3))

#state_plotter(t_span, x.transpose(), 1, True)

ret2 = model_with_noise(n, t_span, sd, ic)

model2 = ret2[0]
z = ret2[1]

model2.fit(z, t_span, multiple_trajectories=True)

print("grwgrwgwrg")
model2.print()

x = model2.simulate(ic, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)
###################################################################

ic2 = np.array([0, 0.075, 0.025, 0, 0, 0])
x = model.simulate(ic2, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

noise2 = noise(1, sd, ic2)

array = np.array(ic2 + ic2*noise2)

x = model.simulate(array, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)
###################################################################

ic3 = np.array([0, 0.05, 0.05, 0, 0, 0])
x = model.simulate(ic3, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

noise3 = noise(1, sd, ic3)

array = np.array(ic3 + ic3*noise3)

x = model.simulate(array, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)
###################################################################

ic4 = np.array([0, 0.025, 0.075, 0, 0, 0])
x = model.simulate(ic4, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

noise4 = noise(1, sd, ic4)

array = np.array(ic4 + ic4*noise4)

x = model.simulate(array, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)
###################################################################

ic5 = np.array([0, 0.01, 0.09, 0, 0, 0])
x = model.simulate(ic5, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

noise5 = noise(1, sd, ic5)

array = np.array(ic5 + ic5*noise5)

x = model.simulate(array, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)