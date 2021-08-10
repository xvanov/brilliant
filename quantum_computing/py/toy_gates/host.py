import qsharp
from Qrng import BasicCircuit
from math import pi

parameters = [pi/2,0.0,0.0]
N = 100
#print(SampleQuantumRandomNumberGenerator.simulate())
print(BasicCircuit.simulate(parameters=parameters, iterations=N))
