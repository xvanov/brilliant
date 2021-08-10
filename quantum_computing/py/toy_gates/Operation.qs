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
	mutable s = new Int[nQubits];
	mutable s1 = 0;
	mutable s2 = 0;
	mutable s3 = 0;
	using ( q = Qubit[nQubits] ) {
                for (iter in 1..iterations) {

                    Rx(parameters[0], q[0]);
                    CNOT(q[0], q[1]);
		    CNOT(q[1], q[2]);

                    for ( i in 0..nQubits-1 ) {
			let result = M(q[i]);
                        let m = ResultArrayAsInt([result]);
			set s w/= i <- m;
                    }

		    set s1 = s1 + s[0];
		    set s2 = s2 + s[1];
		    set s3 = s3 + s[2];
                    ResetAll(q);
                }
        }
	let as1 = IntAsDouble(s1)/IntAsDouble(iterations);
	return as1; 
}
}
