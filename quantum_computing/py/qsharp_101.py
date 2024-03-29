import qsharp
from Brilliant import SpinOperation

# Define the angle theta and the number of iterations
angle = 1.57
num_iter = 10000

# Run SpinOperation, providing the inputs above.
spin = SpinOperation.simulate(theta = angle, iterations = num_iter)

# Output the parameters and the resulting average spin value.
print("Input parameter is", angle, ", number of iterations is", num_iter)
print("Average spin is", spin)
