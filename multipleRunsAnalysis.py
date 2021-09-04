from randomStartingConditions import randomStartingConditions
from originalSystemPrettyPrint import originalSystemPrettyPrint
import pysindy as ps

ret = randomStartingConditions()

differentiation_method = ps.FiniteDifference(order=2)

feature_library = ps.PolynomialLibrary(degree=3)

# use 0.05 for good clean results
optimizer = ps.STLSQ(threshold=0.001)

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

# ret 0 is no noise data, ret 1 is noise data and ret 2 is time data
model.fit(ret[0], ret[2], multiple_trajectories=True, quiet=True)

print(originalSystemPrettyPrint(), "\n")
print("this is your multiple run system")
model.print()
