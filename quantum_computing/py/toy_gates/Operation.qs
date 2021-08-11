namespace Brilliant {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Core;

    operation QuantumMain() : Unit {
        // KnapsackEnergy() operation, providing an angle and number of iterations
        let parameter = [0.0, 0.0, 0.0, 0.0, 0.0]; // x1,x2,x3,y1,y2
        let energy = KnapsackEntanglement(parameter, 100);
        Message($"Energy: {energy}");
    }
    
    operation KnapsackEntanglement(parameter : Double[], iterations : Int) : Double {
        // Define a mutable variable to keep a running total for averaging
        mutable sum = 0;
        let w = [2, 1, 1];
        let c = [500, 200, 400];
        let n = [1, 2];
        let A = 1000;
 
        // Find the number of qubits to be parameterized
        let nQubits = Length(parameter);

        // Define mutable arrays for calculating spins
        mutable s = new Int[nQubits];
        
        using ( q = Qubit[nQubits] ) {
            // Allocate an array of qubits that begin in the |000> state
            for (iter in 1..iterations) {
                // Rotate the state of each qubit
                for (i in 0..nQubits - 1) {
                    Rx(parameter[0], q[1]);
                    // Entangle the qubits together using CNOT operations
                    CNOT(q[1], q[2]);
                    CNOT(q[2], q[4]);
                }
                
                // For each qubit, measure the state and convert it to a spin value
                for (i in 0..nQubits - 1) {
                    let result = M(q[i]);
                    let m = ResultArrayAsInt([result]);
                    set s w/= i <- m;
                }
                
                // Calculate the total energy from the spin values
                
        	Message($"spins: {s}");
		
                let energy =  A * ( 1 - ( s[3] + s[4] ) )^2  + A * (s[0]*w[0] + s[1]*w[1] + s[2]*w[2] - s[3]*n[0] - s[4]*n[1] )^2 - (s[0]*c[0] + s[1]*c[1] + s[2]*c[2]);
                set sum = sum + energy;
                       
                // Reset all the qubits to the |0> state
                ResetAll(q);
            }   
        }
        // Calculate the average energy over all iterations.
        let average = IntAsDouble(sum)/IntAsDouble(iterations);
        return average;
    }
}
