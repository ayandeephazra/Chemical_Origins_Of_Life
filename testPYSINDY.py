
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.integrate import odeint
from sklearn.linear_model import Lasso

import pysindy as ps

np.random.seed(100)

# initial concentrations
# G A GG AA AG/GA GAG/GGA GGG GGGG AAG/AGA AAA
y0_100 = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y0_90 = [0.09, 0.01, 0, 0, 0, 0, 0, 0, 0, 0]
y0_75 = [0.075, 0.025, 0, 0, 0, 0 ,0, 0, 0, 0]
y0_50 = [0.050, 0.050, 0, 0, 0, 0, 0, 0, 0, 0]
y0_25 = [0.025, 0.075, 0, 0, 0, 0, 0, 0, 0, 0]
y0_10 = [0.01, 0.09, 0, 0, 0, 0, 0, 0, 0, 0]
y0_0 = [0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0]
y0_lowC_50 = [0.05 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]
y0_lowC_25 = [0.025, 0.025, 0, 0, 0, 0, 0, 0, 0, 0]
y0_lowC_0 = [0, 0.05, 0, 0, 0, 0, 0, 0, 0, 0]

def lorenz(z, t):
    return [
        10 * (z[1] - z[0]),
        z[0] * (28 - z[2]) - z[1],
        z[0] * z[1] - (8 / 3) * z[2]
    ]

# Generate measurement data
dt = .002

t_train = np.arange(0, 10, dt)
x0_train = [-8, 8, 27]
x_train = odeint(lorenz, x0_train, t_train)

# Instantiate and fit the SINDy model
model = ps.SINDy()
model.fit(x_train, t=dt)
model.print()


# Evolve the Lorenz equations in time using a different initial condition
t_test = np.arange(0, 15, dt)
x0_test = np.array([8, 7, 15])
x_test = odeint(lorenz, x0_test, t_test)

# Compare SINDy-predicted derivatives with finite difference derivatives
print('Model score: %f' % model.score(x_test, t=dt))

# Predict derivatives using the learned model
x_dot_test_predicted = model.predict(x_test)

# Compute derivatives with a finite difference method, for comparison
x_dot_test_computed = model.differentiate(x_test, t=dt)

fig, axs = plt.subplots(x_test.shape[1], 1, sharex=True, figsize=(7, 9))
for i in range(x_test.shape[1]):
    axs[i].plot(t_test, x_dot_test_computed[:, i],
                'k', label='numerical derivative')
    axs[i].plot(t_test, x_dot_test_predicted[:, i],
                'r--', label='model prediction')
    axs[i].legend()
    axs[i].set(xlabel='t', ylabel='$\dot x_{}$'.format(i))
fig.show()