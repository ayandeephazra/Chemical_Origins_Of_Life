import numpy as np
from scipy.integrate import odeint
from ode_helpers import state_plotter
import pysindy as ps
from noise import noise


def picker(ic, sd):
    randplaceholder = np.random.normal(10, 3, size=6)
    ###############################################
    # 1 is scale factor, change as needed
    ###############################################
    ret = 1 * (randplaceholder + randplaceholder * noise(1, sd, ic))
    # ret = 1*(ic + ic * noise(1, sd, ic))
    # ret_abs = abs(ret)
    ret[ret < 0] = 0
    return ret


###############################
def model_with_noise(n, t_span, sd, ic=np.array([0, 0.09, 0.01, 0, 0, 0])):
    c = [0, 9.75, 3.5, 8, 4.5, 9.5, 4.5, 10, 3, 9.75, 8, 0.5, 2, 9.75, 0.75, 10, 0, 9.75, 0.25, 4, 5, 1.75, 6.5]

    def ayan(y, t):
        dydt = [0, c[2] * 2 * y[3] - c[1] * 2 * y[1] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
                c[4] * 2 * y[4] - c[3] * 2 * y[2] ** 2 - c[5] * y[1] * y[2] + c[6] * y[5],
                c[1] * y[1] ** 2 - c[2] * y[3],
                c[3] * y[2] ** 2 - c[4] * y[4],
                c[5] * y[1] * y[2] - c[6] * y[5]]
        return dydt

    #np.random.seed(6)

    scale = np.random.uniform(1, n % 5, n)

    # change back to this if things go wrong
    # init = [50*(ic + noise(1, sd, ic)) for i in range(n)]
    init = [scale[i] * picker(ic, sd) for i in range(n)]

    # DEBUG PRINT STATEMENTS

    init_np = np.array(init)
    state_plotter(t_span, init_np.T, 1, True, noise=0, printnoise=1)

    z = [odeint(ayan, i, t_span) for i in init]
    row = len(z)
    col = len(z[0])

    retmodel = ps.SINDy(optimizer=ps.STLSQ(alpha=250, threshold=3),
                        feature_library=ps.PolynomialLibrary(degree=2, include_bias=False))

    return retmodel, z
