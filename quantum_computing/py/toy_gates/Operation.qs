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
    
}
