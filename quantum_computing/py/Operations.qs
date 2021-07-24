namespace Brilliant {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;

    operation QuantumMain() : Unit {
        // Run SpinOperation(), providing an angle and number of iterations
        let spin = SpinOperation(PI()/2.0, 1000);
        Message($"Average spin: {spin}");
    }
    
    operation SpinOperation(theta : Double, iterations : Int) : Double {
        mutable n = 0;
        using ( q = Qubit() ) {
            // Allocate a qubit which begins in the |0> state
            for (i in 1..iterations) { 
                // Rotate the state of qubit q by theta radians
                Rx(theta,q);
                // Measure the qubit
                let result = M(q);
                // Convert this measurement result into a 0/1 integer.
                let m = ResultArrayAsInt([result]);
                // Transform the result int into spin value
                let s = 2 * m - 1;
                // Add the spin value to n to keep track
                set n += s;
                // Reset all the qubits to the |0> state
                Reset(q);
            }   
        }
        let average = IntAsDouble(n)/IntAsDouble(iterations);
        return average;
    }
}
