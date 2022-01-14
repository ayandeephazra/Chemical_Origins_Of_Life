import numpy as np


def noise(timepoints=5, sigma=0.1, initial=[0, 0.075, 0.025, 0., 0., 0.]):
    #t1 = np.random.normal(loc=1*initial[1], scale=100*(initial[1]+initial[2])*sigma, size=timepoints)
    #t1[t1 < 0] = 0
    #t2 = np.random.normal(loc=1*initial[2], scale=100*(initial[1]+initial[2])*sigma, size=timepoints)
    #t2[t2 < 0] = 0
    #t3 = np.random.normal(loc=1*initial[3], scale=100*(initial[1]+initial[2])*sigma, size=timepoints)
    #t3[t3 < 0] = 0
    #t4 = np.random.normal(loc=1*initial[4], scale=100*(initial[1]+initial[2])*sigma, size=timepoints)
    #t4[t4 < 0] = 0
    #t5 = np.random.normal(loc=1*initial[5], scale=100*(initial[1]+initial[2])*sigma, size=timepoints)
    #t5[t5 < 0] = 0

    t1 = np.random.normal(loc=0, scale=sigma, size=timepoints)
    # t1[t1 < 0] = 0
    t2 = np.random.normal(loc=0, scale=sigma, size=timepoints)
    #t2[t2 < 0] = 0
    t3 = np.random.normal(loc=0, scale=sigma, size=timepoints)
    # t3[t3 < 0] = 0
    t4 = np.random.normal(loc=0, scale=sigma, size=timepoints)
    # t4[t4 < 0] = 0
    t5 = np.random.normal(loc=0, scale=sigma, size=timepoints)
    # t5[t5 < 0] = 0
    retnoise = np.stack((0, t1[0], t2[0], t3[0], t4[0], t5[0]), axis=-1)
    print("retnoise", retnoise)

    # retnoise[retnoise<0] = -1*retnoise

    return retnoise
