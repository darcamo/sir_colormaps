#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import math

from pyphysim.util.conversion import *


if __name__ == '__main__':
    # Positions of the access nodes in the figure
    ANs = 10 * np.array([-.5 + 1j * 1.5,
                         1.5 + 1j * 1.5,
                         0.5 + 1j * 0.5,
                         -.5 + 1j * -0.5,
                         1.5 + 1j * -0.5,
                         0.5 + 1j * -1.5])
    # Positions of point A and B
    A = 10
    B = 5-5j

    # Calculates teh distances
    dists_A = np.abs(ANs - A)
    dists_B = np.abs(ANs - B)

    # Number of walls between points A and B and each
    n_walls_A = np.array([2, 2, 0, 2, 2, 2])
    n_walls_B = np.array([3, 3, 1, 1, 1, 1])

    # Calculates the path loss from A and B to each access node
    #PL_A = 18.7 \cdot \log_{10}(7.07) + 46.8 + 20 \cdot \log_{10}(900e6/5)
    PL_A_3 = 18.7 * np.log10(dists_A[2]) + 46.8 + 20 *np.log10(900e-3/5)
    PL_A = 36.8 * np.log10(dists_A) + 43.8 + 20 *np.log10(900e-3/5) + 5 * (n_walls_A - 1 + 1)
    PL_A[2] = PL_A_3

    PL_B = 36.8 * np.log10(dists_B) + 43.8 + 20 *np.log10(900e-3/5) + 5 * (n_walls_B - 1 + 1)

    # Index of desired signal and interference
    d_idx = np.zeros(6, dtype=bool)
    d_idx[2] = True
    i_idx = np.logical_not(d_idx)

    # Path loss in linear scale
    PL_A_linear = dB2Linear(-PL_A)
    PL_B_linear = dB2Linear(-PL_B)

    # Set the print options
    np.set_printoptions(formatter={'float': lambda x: format(x, '6.2E')})

    # Compute the SIR
    SIR_A = linear2dB(PL_A_linear[d_idx] / np.sum(PL_A_linear[i_idx]))
    SIR_B = linear2dB(PL_B_linear[d_idx] / np.sum(PL_B_linear[i_idx]))
