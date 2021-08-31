from PysindyODEGen_variableIC import ode_gen
import numpy as np

for i in range(1):
    G = 0.1*np.random.normal(loc=0, scale=1, size=1)
    G[G<0] = -1*G
    A = 0.1 * np.random.normal(loc=0, scale=1, size=1)
    A[A<0] = -1*A

    print(G, A)

    init = [0, 0.0, 0.1, 0, 0, 0]

    ode_gen(100, init)
