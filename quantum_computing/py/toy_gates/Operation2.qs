[?1049h[?1h=[1;18r[23m[24m[0m[H[J[?25l[18;1H"Operation.qs" 31L, 996B[1;1Hnamespace Qrng {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Core;[8;5Hoperation SampleQuantumRandomNumberGenerator() : Result {[9;9Huse q = Qubit(); // Allocate a qubit.[10;9HH(q);[12C// Put the qubit to superposition. It now has a 55[11;1H0% chance of being 0 or 1.[12;9Hlet r = M(q);    // Measure the qubit value.[13;9HReset(q);[14;9Hreturn r;
    }[17;5Hoperation QCircuit(parameter : Double[], iterations : Int) : Result {[1m[34m@                                                                         [0m[18;57H1,1[11CTop[1;1H[34h[?25h[?25l[34h[?25h[?25l[18;1H[31mThe ycmd server SHUT DOWN ...t4.log' to check the logs.[0m[18;57H[K[18;57H1,1[11CTop[1;1H[34h[?25h[?25l[18;1HType  :qa  and press <Enter> to exit Vim[18;41H[K[18;57H1,1[11CTop[1;1H[34h[?25h[?25l[18;57H[K[18;57H1,1[11CTop[1;1H[34h[?25h[?25l[18;57H[K[18;57H1,1[11CTop[1;1H[34h[?25h[?25l[18;57H[K[18;57H1,1[11CTop[1;1H[34h[?25h[?25l[18;57H[K[18;57H1,1[11CTop[1;1H[34h[?25h[?25l[18;1H[1m-- VISUAL BLOCK --[0m[18;19H[K[18;57H1,1[11CTop[1;1H[34h[?25h[?25l[18;1H[K[18;57H1,1[11CTop[1;1H[34h[?25h[18;1H
[?1l>[?1049lnamespace Qrng {
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
    
    operation QCircuit(parameter : Double[], iterations : Int) : Result {         let nQubits = Length(parameter);
        mutable resultM = Int[nQubits];
        using ( q = Qubit[nQubits] ) {
        for (iter in 1..iterations) {
            Rx(parameter[0], q[0]);
            CNOT(q[0], q[1]);
            for ( i in 0..nQubits ) {
	    	let m = ResultArrayAsInt(q[i]);
		set resultM w/= i <- m;
                }
            ResetAll(q);
            }
        }
    return resultM;
    }
}
