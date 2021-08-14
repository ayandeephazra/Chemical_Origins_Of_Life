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
x = 3 * np.exp(-2 * t)
y = 0.5 * np.exp(t)
# First column is x, second is y

y100_init = [0.09, 0.01, 0, 0, 0]
y100_1 = [0.075, 0.053246277, 0.053244499, 0.053244498, 0.053244501]
y100_2 = [0.025, 0.019920837, 0.019919003, 0.019919049, 0.019919044]
y100_3 = [0, 0.007370377, 0.007369057, 0.007369122, 0.00736912]
y100_4 = [0, 6.38e-04, 6.38e-04, 6.38e-04, 6.38e-04]
y100_5 = [0, 2.63e-03, 2.63e-03, 2.63e-03, 2.63e-03]

X = np.stack((y100_1, y100_2, y100_3, y100_4, y100_5), axis=-1)
differentiation_method = ps.FiniteDifference(order=2)

feature_library = ps.PolynomialLibrary(degree=3)

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

for i in range(10):
    y100_init = [0.09, 0.01, 0, 0, 0]
    y100_1 = [0.09, 0.064133, 0.064338, 0.064892, 0.065589]
    y100_2 = [0.01, 0.004364, 0.002306, 0.001209, 0.00063]
    y100_3 = [0., 0.0126, 0.012769, 0.013014, 0.013315]
    y100_4 = [0., 0.000039, 0.000011, 0.000003, 0.000001]
    y100_5 = [0., 0.000588, 0.000312, 0.000166, 0.000087]

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
    optimizer = ps.STLSQ(threshold=0.000005)

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
