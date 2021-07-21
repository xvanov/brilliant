namespace Brilliant {
open Microsoft.Quantum.Canon;
open Microsoft.Quantum.Intrinsic;
open Microsoft.Quantum.Convert;

operation QuantumMain() : Unit {
	using ( q = Qubit() ) { 
            // The state of q begins as |0>
            // Measure the qubit
            let result = M(q);
            // Convert this measurement result into a 0/1 integer.
            let m = ResultArrayAsInt([result]);
            let s = 2*m - 1;
            // Return the integer measurement as a console message
            Message($"Result: {m}, {s}");
            // Reset all the qubits to the |0> state
            Reset(q);
        }
    }
}
