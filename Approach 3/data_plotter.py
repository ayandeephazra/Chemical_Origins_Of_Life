import numpy as np
import matplotlib.pyplot as plt


# plot is a boolean that decides if we should display plot or not
def data_plotter(times, states, fig_num, plot, noise=0, printnoise=0):
    num_states = np.shape(states)[0]
    num_cols = int(np.ceil(np.sqrt(num_states)))
    num_rows = int(np.ceil(num_states / num_cols))
    if noise == 0 and printnoise == 0:
        plt.figure("Data Run-- No-Noise [" + str(np.around(states[1][0], 3)) + ", " + str(
            round(states[2][0], 3)) + ", " + str(
            round(states[3][0], 3)) + ", " + str(
            round(states[4][0], 3)) + ", " + str(round(states[5][0], 3)) + "] for " + str(
            len(times)) + " timepoints")
    if noise == 1 and printnoise == 0:
        plt.figure(
            "Data Run-- Noise [" + str(round(states[1][0], 3)) + ", " + str(
                round(states[2][0], 3)) + ", " + str(
                round(states[3][0], 3)) + ", " + str(
                round(states[4][0], 3)) + ", " + str(round(states[5][0], 3)) + "] for " + str(
                len(times)) + " timepoints")
    if noise == 0 and printnoise == 1:
        plt.figure(
            "Data Run-- Noise Data [" + str(np.around(states[1][0], 3)) + ", " + str(
                np.around(states[2][0], 3)) + ", " + str(
                np.around(states[3][0], 3)) + ", " + str(
                np.around(states[4][0], 3)) + ", " + str(np.around(states[5][0], 3)) + "] for " + str(
                len(times)) + " timepoints")
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

    if noise == 0 and printnoise == 0:
        plt.savefig(
            "outputs//Data Run-- No-Noise Recovered [" + str(round(states[1][0], 3)) + ", " + str(
                round(states[2][0], 3)) + ", " + str(
                round(states[3][0], 3)) + ", " + str(
                round(states[4][0], 3)) + ", " + str(round(states[5][0], 3)) + "] for " + str(
                len(times)) + " timepoints" + ".jpg")
    if noise == 1 and printnoise == 0:
        plt.savefig("outputs//Data Run-- Noise Recovered [" + str(round(states[1][0], 3)) + ", " + str(
            round(states[2][0], 3)) + ", " + str(
            round(states[3][0], 3)) + ", " + str(
            round(states[4][0], 3)) + ", " + str(round(states[5][0], 3)) + "] for " + str(
            len(times)) + " timepoints" + ".jpg")

    if noise == 0 and printnoise == 1:
        plt.savefig(
            "outputs//Data Run-- Noise Values for [" + str(np.around(states[1][0], 3)) + ", " + str(
                np.around(states[2][0], 3)) + ", " + str(
                np.around(states[3][0], 3)) + ", " + str(
                np.around(states[4][0], 3)) + ", " + str(np.around(states[5][0], 3)) + "] for " + str(
                len(times)) + " timepoints" + ".jpg")
    if plot:
        plt.show()
    return fig, ax, plt
