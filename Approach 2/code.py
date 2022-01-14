import pysindy as ps
import numpy as np
from scipy.integrate import odeint
from ode_helpers import state_plotter
from model import model
from model_with_noise import model_with_noise
from noise import noise

# increase for better results
n = 100
#############################
# 100 is realistic
# 1000 is good recovery
#############################

days = 2
t_span = np.arange(0, days, days/n)

ret = model(n, t_span)

model = ret[0]
z = ret[1]

model.fit(z, t_span, multiple_trajectories=True)

model.print()
###############################################
sd = 0.01
###############################################
# enter starting condition you want to simulate
ic = np.array([0, 0.09, 0.01, 0.00, 0.00, 0])
x = model.simulate(ic, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

ret2 = model_with_noise(n, t_span, sd, ic)

model2 = ret2[0]
z = ret2[1]

model2.fit(z, t_span, multiple_trajectories=True)

print("model 3")
model2.print()

x = model2.simulate(ic, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True, noise=1)
###################################################################

ic2 = np.array([0, 0.075, 0.025, 0, 0, 0])
x = model.simulate(ic2, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

ret2 = model_with_noise(n, t_span, sd, ic2)

model2 = ret2[0]
z = ret2[1]

model2.fit(z, t_span, multiple_trajectories=True)

print("model 2")
model2.print()

x = model2.simulate(ic2, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True, noise=1)
###################################################################

ic3 = np.array([0, 0.05, 0.05, 0, 0, 0])
x = model.simulate(ic3, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

ret2 = model_with_noise(n, t_span, sd, ic3)

model2 = ret2[0]
z = ret2[1]

model2.fit(z, t_span, multiple_trajectories=True)

print("model 2")
model2.print()

x = model2.simulate(ic3, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True, noise=1)
###################################################################

ic4 = np.array([0, 0.025, 0.075, 0, 0, 0])
x = model.simulate(ic4, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

ret2 = model_with_noise(n, t_span, sd, ic4)

model2 = ret2[0]
z = ret2[1]

model2.fit(z, t_span, multiple_trajectories=True)

print("model 2")
model2.print()

x = model2.simulate(ic4, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True, noise=1)
###################################################################

ic5 = np.array([0, 0.01, 0.09, 0, 0, 0])
x = model.simulate(ic5, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True)

ret2 = model_with_noise(n, t_span, sd, ic5)

model2 = ret2[0]
z = ret2[1]

model2.fit(z, t_span, multiple_trajectories=True)

print("model 2")
model2.print()

x = model2.simulate(ic5, t_span)

print(x.round(3))

state_plotter(t_span, x.transpose(), 1, True, noise=1)

print(model2.coefficients())
print(model.coefficients())
print(np.sum(np.abs(model2.coefficients() - model.coefficients())) / np.sum(np.absolute(model.coefficients())))
