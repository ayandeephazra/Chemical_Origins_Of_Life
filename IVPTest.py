from scipy.integrate import solve_ivp
import numpy as np


def dy1_dt(t, y1, y2, y3, y4,
           y5): return 7 * y3 - 19.5 * y1 ** 2 - 9.5 * y1 * y2 + 4.5 * y5 - 10 * y1 * y5 - 9.75 * y1 * y3 - 9.75 * y1 * y4


def dy2_dt(y1, y2, y3, y4,
           y5): return 9 * y4 - 16 * y2 ** 2 - 9.5 * y1 * y2 + 4.5 * y5 - 10 * y1 * y2 - 4 * y5 * y2 - 1.75 * y2 * y4


def dy3_dt(y1, y2, y3, y4,
           y5): return 9.75 * y1 ** 2 - 3.5 * y3 + 9.75 * y1 * y3 - 19.5 * y3 ** 2 - 10 * y2 * y3


def dy4_dt(y1, y2, y3, y4,
           y5): return 8 * y2 ** 2 - 4.5 * y4 - 9.75 * y1 * y4 - 1.75 * y2 * y4


def dy5_dt(y1, y2, y3, y4,
           y5): return 9.5 * y1 * y2 - 4.5 * y5 - 10 * y1 * y5 - 4 * y5 * y2


tspan = np.linspace(0, 5, 100)
sol = solve_ivp(lambda t, y: dy1_dt(t, y1, y2, y3, y4, y5), [0, 5], [0.1, 0, 0, 0, 0], t_eval=tspan)

print(sol)
