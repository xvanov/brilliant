namespace Qrng {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Core;

    operation SampleQuantumRandomNumberGenerator() : Result {
        use q = Qubit(); // Allocate a qubit.
        H(q);            // Put the qubit to superposition. It now has a 50% chance of being 0 or 1.
        let r = M(q);    // Measure the qubit value.
        Reset(q);
        return r;
    }

    operation BasicCircuit(parameters : Double[], iterations : Int) : Double {
	let nQubits = Length(parameters);
	mutable resultM = new Int[nQubits];
	using ( q = Qubit[nQubits] ) {
                for (iter in 1..iterations) {
                    Rx(parameters[0], q[0]);
                    CNOT(q[0], q[1]);
                    for ( i in 0..nQubits ) {
			let result = M(q[i]);
                        let m = ResultArrayAsInt([result]);
                        Message($"{m}");
			set resultM w/= i <- m;
                    }
        	    Message($"Result: {resultM}");
                    ResetAll(q);
                }
        }
	return 1.0; 
}
}
