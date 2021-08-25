import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import invgauss as ig
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.integrate import odeint
from sklearn.linear_model import Lasso
import pysindy as ps
from generate_Sindy_model import generate
from IVPSolver_n_timepoints import solver

matplotlib.use('TkAgg')

plt.interactive(False)

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


def ode_gen(timepoints = 100, initial=[0, 0.075, 0.025, 0., 0., 0.]):
    print("##########################################################################################################")
    #####################################################################
    # IN THIS FORMAT ONLY, INDEX 0 MUST BE 0 TO COMPILE CODE
    # X = solver(timepoints, [0, 0.075, 0.025, 0., 0., 0.])
    # REST 5 DATAPOINTS CAN BE WHATEVER YOU WANT THE CONCENTRATIONS TO BE
    #####################################################################

    X = solver(timepoints, initial)
    t = np.linspace(0, timepoints - 1, timepoints)
    print("\n", t, "\n")
    print("MODULAR\n\n", X)
    print("\nOriginal Data Matrix\n\n", X.round(4), "\n")
    model = generate(X, t)

    print("\n")

    t1 = np.random.normal(loc=0, scale=0.01, size=timepoints)
    # t1[t1<0] = 0
    t2 = np.random.normal(loc=0, scale=0.01, size=timepoints)
    # t2[t2 < 0] = 0
    t3 = np.random.normal(loc=0, scale=0.01, size=timepoints)
    # t3[t3 < 0] = 0
    t4 = np.random.normal(loc=0, scale=0.01, size=timepoints)
    # t4[t4 < 0] = 0
    t5 = np.random.normal(loc=0, scale=0.01, size=timepoints)
    # t5[t5 < 0] = 0

    noise = np.stack((t1, t2, t3, t4, t5), axis=-1)
    print("Noise", "\n\n", noise.round(4), "\n\nNoise * Data\n\n", (X * noise).round(4), "\n")
    X = X + X * noise
    X[X < 0] = 0
    print("\n Recovered Data (after noise addition)\n\n", X.round(4), "\n")
    model2 = generate(X, t)

    print("Original System\n")
    model.print()
    print("\nRecovered System\n")
    model2.print()

    print("\n")
