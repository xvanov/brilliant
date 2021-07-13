namespace Brilliant {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;

    operation QuantumMain() : Unit {
        // Define the message.    	
        //let message = [RandomInt(2), RandomInt(2)];
        let message = [1];
        Message($"Message is {message}");

        using ( (AliceQ, MiddleQ, BobQ) = (Qubit(), Qubit(), Qubit()) ) {
            // Prepare the Bell state.
            PrepareBell(MiddleQ, BobQ);
            
            if (message[0] == 1) {
                X(AliceQ);};
            //if (message[1] == 1) {X(MiddleQ);};
            
            // Alice sends her qubit to Bob, who decodes the message
            Decode(AliceQ, MiddleQ);
            let resultAlice = M(AliceQ);
            let resultMiddle = M(MiddleQ);
            let bitAlice = ResultArrayAsInt([resultAlice]);
            let bitMiddle = ResultArrayAsInt([resultMiddle]);
            let measured = [bitAlice, bitMiddle];
            // Measure the qubits and report the result.
            // Alice encodes the message
            Encode(BobQ, measured);
            
            ExtractMessage(AliceQ, BobQ);

            // Return all qubits to the |0> state before finishing with them.
            Reset(AliceQ); Reset(MiddleQ); Reset(BobQ); 
        } 
    }
    operation Encode(Q : Qubit, message : Int[]) : Unit {
        // Encode the message into Alice's qubit
        if (message[0] == 0 and message[1] == 0) {
            // No operation.
        } elif (message[0] == 1 and message[1] == 0) {
            X(Q);
        } elif (message[0] == 0 and message[1] == 1) {
            Z(Q);
        } elif (message[0] == 1 and message[1] == 1) {
            Z(Q);
            X(Q);
        }
    }
    operation Decode(AliceQ : Qubit, MiddleQ : Qubit) : Unit {
        // Decode the message from the two qubits.
        CNOT(AliceQ, MiddleQ);
        H(AliceQ);
    }
    operation PrepareBell(AliceQ : Qubit, BobQ : Qubit) : Unit {
        H(AliceQ);
        CNOT(AliceQ, BobQ);
    }
    operation ExtractMessage(AliceQ : Qubit, BobQ : Qubit) : Unit {
        let resultAlice = M(AliceQ);
        let resultBob = M(BobQ);
        let bitAlice = ResultArrayAsInt([resultAlice]);
        let bitBob = ResultArrayAsInt([resultBob]);
        Message($"Result: {bitAlice}, {bitBob}");
    }
}
