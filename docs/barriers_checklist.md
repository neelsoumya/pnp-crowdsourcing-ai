# Barrier checklist
Answer all before investing heavily in an approach. A "no" or "unsure" is fine; hiding it is not.
1. **Relativization:** Does every step hold if all machines get access to an arbitrary oracle? If yes, the approach cannot work (BGS).
2. **Algebrization:** Does it survive giving machines access to a low-degree extension of an oracle? If yes, it cannot work (Aaronson-Wigderson).
3. **Natural proofs:** Is the key property (a) efficiently computable from the truth table (constructive), (b) true for a large fraction of Boolean functions (large), and (c) false for functions in P/poly? If all three, it contradicts strong pseudorandom functions (Razborov-Rudich).
4. **Does your argument prove too much?** Would the same argument "show" something known to be false (e.g. a separation that fails relative to some oracle, or a lower bound for a function known to be easy)?
5. **Smallest real result:** What restricted model/class gives a publishable partial result first?
6. **What changes in the argument for P = NP?** If nothing, the argument is suspect.
