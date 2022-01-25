import numpy
import pysindy as ps
import numpy as np
from scipy.integrate import odeint
from ode_helpers import state_plotter
from model import model
from data_plotter import data_plotter

from noise import noise


def simulate(n, t_span, sd, ic):
    ##########################################################
    # MAIN MODEL INSTANTIATION / CHANGE NOTHING
    ##########################################################
    ret = model(n, t_span, sd)

    model1 = ret[2]
    z = list(ret[0])
    normal_data = np.array(ret[0])

    # plotting no-noise data
    data_plotter(t_span, normal_data[2].T, 1, True)

    model1.fit(z, t_span, multiple_trajectories=True)

    model1.print()

    print()
    x = model1.simulate(ic, t_span)
    model1_coeffs = x

    #print("coeffs", x.round(3))

    state_plotter(t_span, x.transpose(), 1, True)
    # ret2 = model_with_noise(n, t_span, sd, ic)

    model2 = ret[2]
    z = list(ret[1])
    noise_data = np.array(ret[1])
    print("ND", noise_data[0].T)
    #plotting noise data
    data_plotter(t_span, noise_data[2].T, 1, True, noise=1)

    model2.fit(z, t_span, multiple_trajectories=True)

    model2.print()

    x = model2.simulate(ic, t_span)
    model2_coeffs = x
    species = x.transpose()

    #print("simulated values", x.round(3))

    state_plotter(t_span, x.transpose(), 1, True, noise=1)

    # ERROR IN COEFFICIENTS

    print(model2.coefficients())
    print(model1.coefficients())
    print("Fractional Error between Noise and No-Noise Model Coefficients",
          np.sum(np.abs(model2.coefficients() - model1.coefficients())) / np.sum(np.absolute(model1.coefficients())))

    ############################################################################################################
    ############################################################################################################

    # MASS BALANCE CHECKING

    #   G -> 75.07, A -> 89.09, GA/AA/GG -> 132.12, 160.171, 146.14

    ############################################################################################################
    # NO NOISE MODEL MASS BALANCE ERROR ANALYSIS
    ############################################################################################################

    error_percent_list = []
    # expected_mass_balance = model1_coeffs[0][1] / 75.07 + model1_coeffs[0][2] / 89.09 + model1_coeffs[0][3] / 132.12 + \
    # model1_coeffs[0][4] / 160.171 + model1_coeffs[0][5] / 146.14
    expected_mass_balance = ic[1] * 75.07 + ic[2] * 89.09 + ic[3] * 132.12 + ic[4] * 160.171 + ic[5] * 146.14

    for i in range(len(x)):
        mass_balance = model1_coeffs[i][1] * 75.07 + model1_coeffs[i][2] * 89.09 + model1_coeffs[i][3] * 132.12 + \
                       model1_coeffs[i][4] * 160.171 + model1_coeffs[i][5] * 146.14
        error_percent = (mass_balance - expected_mass_balance) * 100 / expected_mass_balance
        error_percent_list.append(abs(error_percent))

    sum = 0
    for i in range(len(error_percent_list)):
        # print(error_percent_list[i])
        sum = sum + error_percent_list[i]

    average_error_percent = sum / len(error_percent_list)

    print("No-Noise Model Average Error Percent:", average_error_percent, "%")

    ############################################################################################################
    # NOISE MODEL MASS BALANCE ERROR ANALYSIS
    ############################################################################################################

    error_percent_list = []
    # expected_mass_balance = model2_coeffs[0][1] / 75.07 + model2_coeffs[0][2] / 89.09 + model2_coeffs[0][3] / 132.12 + \
    # model2_coeffs[0][4] / 160.171 + model2_coeffs[0][5] / 146.14
    expected_mass_balance = ic[1] * 75.07 + ic[2] * 89.09 + ic[3] * 132.12 + ic[4] * 160.171 + ic[5] * 146.14

    for i in range(len(x)):
        mass_balance = model2_coeffs[i][1] * 75.07 + model2_coeffs[i][2] * 89.09 + model2_coeffs[i][3] * 132.12 + \
                       model2_coeffs[i][4] * 160.171 + model2_coeffs[i][5] * 146.14
        error_percent = (mass_balance - expected_mass_balance) * 100 / expected_mass_balance
        error_percent_list.append(abs(error_percent))

    sum = 0
    for i in range(len(error_percent_list)):
        # print(error_percent_list[i])
        sum = sum + error_percent_list[i]

    average_error_percent = sum / len(error_percent_list)

    print("Noise Model Average Error Percent:", average_error_percent, "%")
