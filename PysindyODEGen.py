
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.integrate import odeint
from sklearn.linear_model import Lasso
import pysindy as ps
plt.interactive(False)
def lorenz(z, t):
    return [
        10 * (z[1] - z[0]),
        z[0] * (28 - z[2]) - z[1],
        z[0] * z[1] - (8 / 3) * z[2]
    ]
np.random.seed(100)

# initial concentrations Glycine to Alanine
# G A GG AA AG/GA GAG/GGA GGG GGGG AAG/AGA AAA
y0_100 = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y0_90 = [0.09, 0.01, 0, 0, 0, 0, 0, 0, 0, 0]
y0_75 = [0.075, 0.025, 0, 0, 0, 0, 0, 0, 0, 0]
y0_50 = [0.050, 0.050, 0, 0, 0, 0, 0, 0, 0, 0]
y0_25 = [0.025, 0.075, 0, 0, 0, 0, 0, 0, 0, 0]
y0_10 = [0.01, 0.09, 0, 0, 0, 0, 0, 0, 0, 0]
y0_0 = [0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0]
y0_lowC_50 = [0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y0_lowC_25 = [0.025, 0.025, 0, 0, 0, 0, 0, 0, 0, 0]
y0_lowC_0 = [0, 0.05, 0, 0, 0, 0, 0, 0, 0, 0]

t = np.linspace(0, 1, 1000)

x = 3 * np.exp(-2 * t)
y = 0.5 * np.exp(t)
X = np.stack((x, y), axis=-1)  # First column is x, second is y

differentiation_method = ps.FiniteDifference(order=2)

feature_library = ps.PolynomialLibrary(degree=3)

optimizer = ps.STLSQ(threshold=0.2)

model = ps.SINDy(
    differentiation_method=differentiation_method,
    feature_library=feature_library,
    optimizer=optimizer,
    feature_names=["x", "y"]
)


model.fit(X, t=t);


model.print()


x0 = 6
y0 = -0.1

t_test = np.linspace(0, 1, 100)
x_test = x0 * np.exp(-2 * t_test)
y_test = y0 * np.exp(t_test)

sim = model.simulate([x0, y0], t=t_test)


fig, ax = plt.subplots(1, 1, figsize=(5, 5))
ax.plot(x0, y0, "ro", label="Initial condition", alpha=0.6, markersize=8)
ax.plot(x_test, y_test, "b", label="Exact solution", alpha=0.4, linewidth=4)
ax.plot(sim[:, 0], sim[:, 1], "k--", label="SINDy model", linewidth=3)
ax.set(xlabel="x", ylabel="y")
ax.legend()
#plt.imshow(img.reshape((28, 28)))
fig.show()






