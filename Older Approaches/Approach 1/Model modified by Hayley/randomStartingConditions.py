from PysindyODEGen_variableIC import ode_gen
import numpy as np


def randomStartingConditions(printVals):
    orglist = []
    Xlist = []
    tlist = []

    for i in range(10):
        G = 0.1 * np.random.normal(loc=0, scale=1, size=1)
        G[G < 0] = -1 * G
        A = 0.1 * np.random.normal(loc=0, scale=1, size=1)
        A[A < 0] = -1 * A

        print(G, A)
        init = [0, G[0], A[0], 0, 0, 0]

        val = ode_gen(printVals, 100, init)

        # no noise
        orglist.append(val[0])
        # noise
        Xlist.append(val[1])
        # time
        tlist.append(val[2])

        #val 3 and 4 are model and model2, sans and with noise
    return orglist, Xlist, tlist, val[3], val[4], init


randomStartingConditions(False)
