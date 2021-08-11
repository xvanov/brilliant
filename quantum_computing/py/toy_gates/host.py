import qsharp
from Brilliant import KnapsackEntanglement
from math import pi
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np

'''
Instead of varying each rotation independently starting from [0, 0, 0, 0, 0], the classical optimizer only needs to proceed downhill in energy by rotating the second qubit’s state, directly to the optimal configuration.
'''


# Define an array of angles and an empty array for the output
angle_range = np.linspace(0.0, 2 * np.pi, 20)
data = [0]*20

# Run the KnapsackEntanglement operation, varying only the first parameter
for i in range(20):
        data[i] = KnapsackEntanglement.simulate(parameter = [angle_range[i], 0.0, 0.0, 0.0, 0.0], iterations = 100)

# Output the energy landscape  as a plot.
plt.xlabel('Parameter 1 Angle [radians]')
plt.ylabel('Energy')
plt.plot(angle_range, data)
plt.savefig("figure.png")

