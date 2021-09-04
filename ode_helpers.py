import numpy as np
import matplotlib.pyplot as plt


def state_plotter(times, states, fig_num):
    num_states = np.shape(states)[0]
    num_cols = int(np.ceil(np.sqrt(num_states)))
    num_rows = int(np.ceil(num_states / num_cols))
    plt.figure("G = " + str(states[1][0]) + " A = " + str(states[2][0]) + " for " + str(len(times)) + " timepoints")
    plt.clf()
    fig, ax = plt.subplots(num_rows, num_cols, num=fig_num, clear=True,
                           squeeze=False)

    for n in range(num_states):
        row = n // num_cols
        col = n % num_cols
        ax[row][col].plot(times, states[n], 'k.:')
        ax[row][col].set(xlabel='Time',
                         ylabel='$y_{:0.0f}(t)$'.format(n),
                         title='$y_{:0.0f}(t)$ vs. Time'.format(n))

    for n in range(num_states, num_rows * num_cols):
        fig.delaxes(ax[n // num_cols][n % num_cols])

    print("states", states)
    fig.tight_layout()
    # plt.figure("G = " + str(states[1][0]) + " A = " + str(states[2][0]))
    # plt.subtitle("G = " + str(states[1][0]) + " A = " + str(states[2][0]))

    plt.savefig("outputs//G = " + str(states[1][0]) + " A = " + str(states[2][0]) + " for " + str(len(times)) + " timepoints" + ".jpg")
    #plt.show()
    return fig, ax, plt
