import qsharp
from Brilliant import SpinEnergy


parameter = [0.0, 0.0, 0.0]
iterations = 100
j = 1
h = 2
print('Calculating average energy of system...')
print(f'initial parameters:\nqubit parameters: {parameter}\niterations={iterations}\nj={j}, h={h}')
average_energy = SpinEnergy.simulate(parameter=parameter, iterations=iterations, j=j, h=h)
print(f"average spin energy = {average_energy}")
