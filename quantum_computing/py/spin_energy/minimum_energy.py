import qsharp
from Brilliant import SpinEnergy
from scipy.optimize import minimize
from random import uniform
from math import pi
import matplotlib.pyplot as plt

def get_minimum_energy_of_spin_system(j,h,N=100):

    progress = []
    def objective(x):
        result = SpinEnergy.simulate(parameter=x.tolist(),
                                     iterations=N,
                                     j=j,
                                     h=h)
        progress.append(result)
        return result

    starting_parameters = [uniform(0,pi), uniform(0,pi), uniform(0,pi)]
    result = minimize(objective, starting_parameters, method='Powell')
    return result

for i in range(1,11):
    # j, h = 1, 0 # ferromagnetic
    #j, h = -1, 0 # anti-ferromagnetic
    j, h = -1, 10 # anti-ferromagnetic, strong magentic field
    result = get_minimum_energy_of_spin_system(j,h)
    print(f'iteration = {i}')
    print(f'Minimum energy = {result.fun}')
    print(f'Minimum parameters = {result.x}')

'''
plt.plot(progress)
plt.xlabel('Number of energy evaluations')
plt.ylabel('Energy')
plt.savefig('progress.png')
'''
