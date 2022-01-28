import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
from scipy.stats import invgauss as ig

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


# .random.seed(100)
print("")
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

# time in units of days, 1 is 1 day
t = np.linspace(0, 4, 5)
print(t)


for i in range(10):
    y100_init = [0.1, 0, 0, 0, 0]

    y100_1 = [0.1, 0.070946, 0.071542, 0.072157, 0.072738]
    y100_2 = [0., 0., 0., 0., 0.]
    y100_3 = [0., 0.015611, 0.015936, 0.016219, 0.016489]
    y100_4 = [0., 0., 0., 0., 0.]
    y100_5 = [0., 0., 0., 0., 0.]

    X = np.stack((y100_1, y100_2, y100_3, y100_4, y100_5), axis=-1)

    t1 = np.random.normal(loc=0, scale=0.1, size=5)
    # t1[t1<0] = 0
    t2 = np.random.normal(loc=0, scale=0.1, size=5)
    # t2[t2 < 0] = 0
    t3 = np.random.normal(loc=0, scale=0.1, size=5)
    # t3[t3 < 0] = 0
    t4 = np.random.normal(loc=0, scale=0.1, size=5)
    # t4[t4 < 0] = 0
    t5 = np.random.normal(loc=0, scale=0.1, size=5)
    # t5[t5 < 0] = 0

    noise = np.stack((t1, t2, t3, t4, t5), axis=-1)
    print(X, "\n\n", noise.round(5), "\n\n", (X * noise).round(5), "\n")
    X = X + X * noise
    X[X < 0] = 0
    print(X.round(5), "\n")
    differentiation_method = ps.FiniteDifference(order=2)

    feature_library = ps.PolynomialLibrary(degree=3)

    # use 0.05 for good clean results
    optimizer = ps.STLSQ(threshold=0.00001)

    model = ps.SINDy(
        differentiation_method=differentiation_method,
        feature_library=feature_library,
        optimizer=optimizer,
        feature_names=["y1", "y2", "y3", "y4", "y5"]
    )

    model.fit(X, t=t);

    model.equations(precision=5)
    model.print()
    print("\n")
