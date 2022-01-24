import numpy as np
from scipy.integrate import odeint
from ode_helpers import state_plotter
import pysindy as ps


def model(n, t_span):
    c = [0, 9.75, 3.5, 8, 4.5, 9.5, 4.5, 10, 3, 9.75, 8, 0.5, 2, 9.75, 0.75, 10, 0, 9.75, 0.25, 4, 5, 1.75, 6.5]

    def ayan(y, t):
        dydt = [0, c[2] * 2 * y[3] - c[1] * 2 * y[1] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
                c[4] * 2 * y[4] - c[3] * 2 * y[2] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
                c[1] * y[1] ** 2 - c[2] * y[3],
                c[3] * y[2] ** 2 - c[4] * y[4],
                c[5] * y[1] * y[2] - c[6] * y[5]]
        return dydt

    np.random.seed(5)

    scale = np.random.uniform(1, n % 5, n)

    init = [scale[i] * np.random.normal(10, 3, size=6) for i in range(n)]

    z = [odeint(ayan, i, t_span) for i in init]

    retmodel = ps.SINDy(optimizer=ps.STLSQ(alpha=250, threshold=3),
                        feature_library=ps.PolynomialLibrary(degree=2, include_bias=False))

    print("zz", z)

    return retmodel, z