from randomStartingConditions import randomStartingConditions
from originalSystemPrettyPrint import originalSystemPrettyPrint
import pysindy as ps
from forwardSimulation import forwardSimulation


def thresholdSweep(thresh):
    # PARAMETER PRINTS VALUES TO SCREEN
    ret = randomStartingConditions(False)

    # forward simulation aspect
    model = ret[3]
    model2 = ret[4]
    init = ret[5]

    print("here", model.equations())

    forwardSimulation(model, model2, init)
    ################################

    differentiation_method = ps.FiniteDifference(order=2)

    feature_library = ps.PolynomialLibrary(degree=3)

    # parametrized the thresh parameter
    optimizer = ps.STLSQ(threshold=thresh)

    optimizer.fit_intercept = False

    speciesName = []

    # ret[0].shape[1]

    # we will use the first matrix of the list as a template, which makes sense
    # all matrices are the same in dimensionality
    for i in range(ret[0][0].shape[1]):
        speciesName.append("y" + str(i + 1))

    model = ps.SINDy(
        differentiation_method=differentiation_method,
        feature_library=feature_library,
        optimizer=optimizer,
        feature_names=speciesName  # ["y1", "y2", "y3", "y4", "y5"]
    )

    differentiation_method2 = ps.FiniteDifference(order=2)

    feature_library2 = ps.PolynomialLibrary(degree=3)

    # use 0.05 for good clean results
    optimizer2 = ps.STLSQ(threshold=thresh)

    optimizer2.fit_intercept = False

    speciesName2 = []

    # ret[0].shape[1]

    # we will use the first matrix of the list as a template, which makes sense
    # all matrices are the same in dimensionality
    for i in range(ret[1][0].shape[1]):
        speciesName2.append("y" + str(i + 1))

    model2 = ps.SINDy(
        differentiation_method=differentiation_method2,
        feature_library=feature_library2,
        optimizer=optimizer2,
        feature_names=speciesName2  # ["y1", "y2", "y3", "y4", "y5"]
    )
    #####################
    #####################

    # ret 0 is no noise data, ret 1 is noise data and ret 2 is time data
    model.fit(ret[0], ret[2], multiple_trajectories=True, quiet=True)
    model2.fit(ret[1], ret[2], multiple_trajectories=True, quiet=True)
    print("##########################################################################################################")
    print(originalSystemPrettyPrint(), "\n")
    print("this is the multiple run system sans noise with threshold: ", thresh, "\n")
    model.print()

    # print(type(model.predict(multiple_trajectories=True)))
    print("\nthis is the multiple run system with noise with threshold: ", thresh, "\n")
    model2.print()


thresholdSweep(0.001)
