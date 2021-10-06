import matplotlib.pyplot as plt
import matplotlib
import pysindy as ps

matplotlib.use('TkAgg')


#########################################################################################
# Method to generate ODE system based on a data matrix
# does this for any number of parameters and any number of timepoints
#########################################################################################
def generate(matrix, t):
    differentiation_method = ps.FiniteDifference(order=2)

    feature_library = ps.PolynomialLibrary(degree=3)

    # use 0.05 for good clean results
    optimizer = ps.STLSQ(threshold=0.0001)

    optimizer.fit_intercept = False

    speciesName = []

    for i in range(matrix.shape[1]):
        speciesName.append("y" + str(i + 1))

    model = ps.SINDy(
        differentiation_method=differentiation_method,
        feature_library=feature_library,
        optimizer=optimizer,
        feature_names=speciesName  # ["y1", "y2", "y3", "y4", "y5"]

    )

    model.fit(matrix, t=t)

    model.equations(precision=5)
    return model
