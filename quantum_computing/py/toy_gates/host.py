import qsharp
from Qrng import SampleQuantumRandomNumberGenerator

parameter = [1,0,0]
N = 100
#print(QCircuit.simulate(parameter=parameter, iterations=N))
print(SampleQuantumRandomNumberGenerator.simulate())
