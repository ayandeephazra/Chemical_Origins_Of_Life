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
t = np.linspace(0, 9, 10)
print(t)

for i in range(10):
    y100_init = [0.09, 0.01, 0, 0, 0]
    y100_1 = [0.075, 0.05378, 0.053235, 0.053343, 0.053796, 0.054456, 0.055241, 0.056101, 0.057004, 0.057937]
    y100_2 = [0.025, 0.011974, 0.007087, 0.004183, 0.002455, 0.001431, 0.000827, 0.000473, 0.000268, 0.000151]
    y100_3 = [0., 0.008662, 0.008583, 0.008655, 0.008829, 0.009067, 0.009345, 0.009652, 0.00998, 0.01032]
    y100_4 = [0., 0.000284, 0.000101, 0.000036, 0.000012, 0.000004, 0.000001, 0., 0., 0.]
    y100_5 = [0., 0.001347, 0.000791, 0.000469, 0.000278, 0.000164, 0.000096, 0.000056, 0.000032, 0.000018]

    X = np.stack((y100_1, y100_2, y100_3, y100_4, y100_5), axis=-1)

    t1 = np.random.normal(loc=0, scale=0.1, size=10)
    # t1[t1<0] = 0
    t2 = np.random.normal(loc=0, scale=0.1, size=10)
    # t2[t2 < 0] = 0
    t3 = np.random.normal(loc=0, scale=0.1, size=10)
    # t3[t3 < 0] = 0
    t4 = np.random.normal(loc=0, scale=0.1, size=10)
    # t4[t4 < 0] = 0
    t5 = np.random.normal(loc=0, scale=0.1, size=10)
    # t5[t5 < 0] = 0

    noise = np.stack((t1, t2, t3, t4, t5), axis=-1)
    print(X, "\n\n", noise.round(5), "\n\n", (X * noise).round(5), "\n")
    X = X + X * noise
    X[X < 0] = 0
    print(X.round(5), "\n")
    differentiation_method = ps.FiniteDifference(order=2)

    feature_library = ps.PolynomialLibrary(degree=3)

    # use 0.05 for good clean results
    optimizer = ps.STLSQ(threshold=0.0001)

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
