namespace Brilliant {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Math;

    operation QuantumMain() : Unit {
        // Define the message.
        let message = [RandomInt(2), RandomInt(2)];
        Message($"Message is: {message}");

        using ( (AliceQ, BobQ) = (Qubit(), Qubit()) ) {
            // Prepare the Bell state.
            PrepareBell(AliceQ, BobQ);

            // Alice encodes the message
            Encode(AliceQ, message);
            
            // Alice sends her qubit to Bob, who decodes the message
            Decode(AliceQ, BobQ);

            // Measure the qubits and report result.
            ExtractMessage(AliceQ, BobQ);

            // Return all qubits to the |0> state before finishing with them.
            Reset(AliceQ); Reset(BobQ); 
        } 
    }
    operation Encode(AliceQ : Qubit, message : Int[]) : Unit {
        // Encode the message into Alice's qubit
        if (message[0] == 0 and message[1] == 0) {
            // No operation.
        } elif (message[0] == 0 and message[1] == 1) {
            X(AliceQ);
        } elif (message[0] == 1 and message[1] == 0) {
            Z(AliceQ);
        } elif (message[0] == 1 and message[1] == 1) {
            Z(AliceQ);
            X(AliceQ);
        }
    }
    operation Decode(AliceQ : Qubit, BobQ : Qubit) : Unit {
        // Decode the message from the two qubits.
        CNOT(AliceQ, BobQ);
        H(AliceQ);
    }
    operation PrepareBell(AliceQ : Qubit, BobQ : Qubit) : Unit {
        H(AliceQ);
        CNOT(AliceQ, BobQ);
    }
    operation ExtractMessage(AliceQ : Qubit, BobQ : Qubit) : Unit {
        let resultAlice = M(AliceQ);
        let resultBob = M(BobQ);
        Message($"Result: {resultAlice}, {resultBob}");
    }
}
