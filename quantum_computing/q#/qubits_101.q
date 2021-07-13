	mutable n_ones = 0;
        for (i in 0 .. 100) {                 // This for loop repeats 6 times.
		    using ( q = Qubit() ) {
		        H(q); T(q); H(q);
		        
		        let result = M(q);
                let resultInt = ResultArrayAsInt([result]);
                

		        Message($"Result: {result}");
		        
		        if (result == Zero) {
		            // No operation.
		        } else {
                    set n_ones = n_ones + 1;
		            X(q);
		        }
		    } 
		}
        Message($"Number of ones: {n_ones}");

