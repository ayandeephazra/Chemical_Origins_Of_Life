from scipy.integrate import solve_ivp
import numpy as np
from ode_helpers import state_plotter


def f(t, y, model1, model2):
    dydt = [1]
    for i in range(len(model1.equations())):

        sumT = 0
        string = model1.equations()[i]
        listOfWords = string.split()
        # print(listOfWords)
        y1val = False
        y2val = False
        y3val = False
        y4val = False
        y5val = False
        term = 1

        for j in range(len(listOfWords)):
            if listOfWords[j] == 'y1':
                term = term * y[1]
                y1val = True
                continue
            if listOfWords[j] == 'y2':
                term = term * y[2]
                y2val = True
                continue
            if listOfWords[j] == 'y3':
                term = term * y[3]
                y3val = True
                continue
            if listOfWords[j] == 'y4':
                term = term * y[4]
                y4val = True
                continue
            if listOfWords[j] == 'y5':
                term = term * y[5]
                y5val = True
                continue
            if listOfWords[j] == 'y1^2':
                term = term * y[1] ** 2
                y1val = True
                continue
            if listOfWords[j] == 'y2^2':
                term = term * y[2] ** 2
                y2val = True
                continue
            if listOfWords[j] == 'y3^2':
                term = term * y[3] ** 2
                y3val = True
                continue
            if listOfWords[j] == 'y4^2':
                term = term * y[4] ** 2
                y4val = True
                continue
            if listOfWords[j] == 'y5^2':
                term = term * y[5] ** 2
                y5val = True
                continue
            if listOfWords[j] == 'y1^3':
                term = term * y[1] ** 3
                y1val = True
                continue
            if listOfWords[j] == 'y2^3':
                term = term * y[2] ** 3
                y2val = True
                continue
            if listOfWords[j] == 'y3^3':
                term = term * y[3] ** 3
                y3val = True
                continue
            if listOfWords[j] == 'y4^3':
                term = term * y[4] ** 3
                y4val = True
                continue
            if listOfWords[j] == 'y5^3':
                term = term * y[5] ** 3
                y5val = True
                continue
            if listOfWords[j] == '+' or listOfWords[j] == '-':
                sumT = sumT + term
                continue

            coeff = float(listOfWords[j])
            term = term * coeff

        sumT = sumT + term
        dydt.append(sumT)

    return dydt


def forwardSimulation(model1, model2, init=[0, 0.05, 0.05, 0, 0, 0]):
    tspan = np.linspace(0, 100 - 1, 100)
    sol = solve_ivp(lambda t, y: f(t, y, model1, model2),
                    [tspan[0], tspan[-1]], init, t_eval=tspan, rtol=1e-5)
    print("forward simulation with 50-50 intiial concentration:")
    state_plotter(sol.t, sol.y, 1, True)
