import qsharp
from Brilliant import KnapsackEnergy
from math import pi

parameter = [pi, 0.0, 0.0, 0.0, pi]
iterations = 100
print('Calculating average energy of system...')
print(f'initial parameters:\nqubit parameters: {parameter}\niterations={iterations}')
average_energy = KnapsackEnergy.simulate(parameter=parameter, iterations=iterations)
print(f"average spin energy = {average_energy}")
