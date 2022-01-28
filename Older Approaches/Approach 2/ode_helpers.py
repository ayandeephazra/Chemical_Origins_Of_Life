import numpy as np
import matplotlib.pyplot as plt


# plot is a boolean that decides if we should display plot or not
def state_plotter(times, states, fig_num, plot, noise=0, printnoise=0):
    num_states = np.shape(states)[0]
    num_cols = int(np.ceil(np.sqrt(num_states)))
    num_rows = int(np.ceil(num_states / num_cols))
    if noise == 0 and printnoise == 0:
        plt.figure("No-Noise G = " + str(states[1][0]) + " A = " + str(states[2][0]) + " for " + str(len(times)) + " timepoints")
    if noise == 1 and printnoise==0:
        plt.figure("Noise G = " + str(states[1][0]) + " A = " + str(states[2][0]) + " for " + str(len(times)) + " timepoints")
    if noise == 0 and printnoise == 1:
        plt.figure("Noise Data for G = " + str(states[1][0]) + " A = " + str(states[2][0]) + " for " + str(len(times)) + " timepoints")
    plt.clf()
    fig, ax = plt.subplots(num_rows, num_cols, num=fig_num, clear=True,
                           squeeze=False)

    for n in range(num_states):
        if n != 0:
            row = n // num_cols
            col = n % num_cols
            ax[row][col].plot(times, states[n], 'k.:')
            ax[row][col].set(xlabel='Time',
                             ylabel='$y_{:0.0f}(t)$'.format(n),
                             title='$y_{:0.0f}(t)$ vs. Time'.format(n))

    for n in range(num_states, num_rows * num_cols):
        if n != 0:
            fig.delaxes(ax[n // num_cols][n % num_cols])

    print("states", states)
    fig.tight_layout()
    # plt.figure("G = " + str(states[1][0]) + " A = " + str(states[2][0]))
    # plt.subtitle("G = " + str(states[1][0]) + " A = " + str(states[2][0]))

    if noise == 0 and printnoise==0:

        plt.savefig("outputs//No-Noise Recovered G = " + str(states[1][0]) + " A = " + str(states[2][0]) + " for " + str(
            len(times)) + " timepoints" + ".jpg")
    if noise == 1 and printnoise==0:
        plt.savefig("outputs//Noise Recovered G = " + str(states[1][0]) + " A = " + str(states[2][0]) + " for " + str(
            len(times)) + " timepoints" + ".jpg")

    if noise == 0 and printnoise == 1:
        plt.savefig(
            "outputs//Noise Values for G = " + str(states[1][0]) + " A = " + str(states[2][0]) + " for " + str(
                len(times)) + " timepoints" + ".jpg")
    if plot:
        plt.show()
    return fig, ax, plt
