import qsharp
from Qrng import BasicCircuit
parameters = [1.0,0.0,0.0]
N = 100
#print(SampleQuantumRandomNumberGenerator.simulate())
print(BasicCircuit.simulate(parameters=parameters, iterations=N))
