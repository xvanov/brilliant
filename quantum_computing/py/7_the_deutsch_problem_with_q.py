namespace Brilliant {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation QuantumMain() : Unit {
        using ( (query, target) = (Qubit(), Qubit()) ) {
            // Prepare the query and target qubits for a phase query.
            H(query);
            X(target);
            H(target);
            // Apply an Oracle!
			XOracle(query, target);
            MeasureAndMessage(query, target);
            Reset(query); Reset(target);
        }
    }
    operation XOracle(query : Qubit, target : Qubit) : Unit {
        // An oracle with f(x) = x
        CNOT(query,target);
    }
    operation NOTXOracle(query : Qubit, target : Qubit) : Unit {
        // An oracle with f(x) = NOT(x)
        X(query);
        CNOT(query,target);
    }
    operation ZeroOracle(query : Qubit, target : Qubit) : Unit {
        // An oracle with f(x) = 0.
        // No operation
    }
    operation OneOracle(query : Qubit, target : Qubit) : Unit {
        // An oracle with f(x) = 1.
        X(target);
    }
    operation MeasureAndMessage(query : Qubit, target : Qubit) : Unit {
        let resultQuery = M(query);
        let resultTarget = M(target);
        Message($"Result: {resultQuery}, {resultTarget}");
    }
}
