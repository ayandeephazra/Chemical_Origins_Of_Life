# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 08:59:23 2022

@author: Ayan Deep Hazra
"""
import operator
import itertools

ewns = [[0] * 360] * 360


def theta_python(theta1, theta2):
    ew = theta1 + 180
    # ns = 180 - theta2 if theta2 > 179 else 179 - theta2
    ns = -1 * (theta2 - 179)
    return ew, ns


def python_theta(ew, ns):
    theta1 = ew - 180
    theta2 = -1 * ns + 179
    return theta1, theta2


def antipode_theta(theta1, theta2):
    antitheta1 = theta1 - 180 if theta1 >= 0 else theta1 + 180
    antitheta2 = theta2 - 180 if theta2 >= 0 else theta2 + 180
    return antitheta1, antitheta2


visited = []


def recursive_colorer(starttheta1, starttheta2, val, visited):
    visited.append((starttheta1, starttheta2))
    if starttheta1 > 178 or starttheta1 < -179 or starttheta2 > 178 or starttheta2 < -179:
        return
    else:
        poss1 = [starttheta1, starttheta1 - 1, starttheta1 + 1]
        poss2 = [starttheta2, starttheta2 - 1, starttheta2 + 1]
        cartesian_product = itertools.product(poss1, poss2)
        cartesian_list = list(set(cartesian_product) - set(visited))
        #  cartesian_list.remove((starttheta1, starttheta2))
        for pair in cartesian_list:
            recursive_colorer(0, 0, 0, visited)
            # cartesian_list.append(list(set(recursive_colorer(pair[0], pair[1], 0))))
            print(cartesian_list)

    return cartesian_list


print(recursive_colorer(0, 0, 0, visited))







