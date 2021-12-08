import numpy as np
from scipy.integrate import odeint
from ode_helpers import state_plotter
import pysindy as ps
from noise import noise


###############################
def model_with_noise(n, t_span, sd, ic=np.array([0, 0.09, 0.01, 0, 0, 0])):
    c = [0, 9.75, 3.5, 8, 4.5, 9.5, 4.5, 10, 3, 9.75, 8, 0.5, 2, 9.75, 0.75, 10, 0, 9.75, 0.25, 4, 5, 1.75, 6.5]

    def ayan(y, t):
        dydt = [1, c[2] * 2 * y[3] - c[1] * 2 * y[1] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
                c[4] * 2 * y[4] - c[3] * 2 * y[2] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
                c[1] * y[1] ** 2 - c[2] * y[3],
                c[3] * y[2] ** 2 - c[4] * y[4],
                c[5] * y[1] * y[2] - c[6] * y[5]]
        return dydt

    np.random.seed(6)

    scale = np.random.uniform(1, n % 5, n)

    # print("ic", 100 * (ic + noise(1, sd, ic)))
    init = [50*(ic + noise(1, sd, ic)) for i in range(n)]
    # FIX!
    #print("init", list(init))
    #state_plotter(t_span, np.array(list(init)), 1, True, noise=1)
    # init = [scale[1] * np.random.normal(10, 3, size=6) for i in range(n)]
    z = [odeint(ayan, i, t_span) for i in init]
    row = len(z)
    col = len(z[0])

    #t = np.array(np.random.normal(10, 3 * sd, size=(row, col, 6))).tolist()
    #z = z + t * np.array(z)

    retmodel = ps.SINDy(optimizer=ps.STLSQ(alpha=250, threshold=2),
                        feature_library=ps.PolynomialLibrary(degree=2, include_bias=False))

    return retmodel, z
