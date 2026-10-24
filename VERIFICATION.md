# Verification scope

Fresh checks on 24 October 2026:

- Independent exact Python geometric-edge checks, without external libraries: rigidity lemma and canonical-pair formula k=1..9; exact (not merely parity) cell identity on every relevant nonnegative cell; skeleton weight and intersection identities for every skeleton at m=0..8; all path families of size 2^n, and absence of size 2^n+1, for n=1..4. Counts are 1, 2, 5 and 14 families. Output: `verification/current/independent-checks.json`.
- Original SAT/Python verifier: all extremal admissible systems m=0..5 (counts 1,1,2,3,6,10), absence of larger norm, all extremal path families n=1..4, all admissible groupings k=0..7, and rigidity k=1..9. All checks pass. Output: `verification/current/original-sat.txt`. CaDiCaL's comments about falsified original clauses accompany expected unsatisfiable subproblems; they are not failed mathematical checks. This run does not claim the larger historical m=6 or n=5 tests were repeated.
- Fresh Lean 4.34.1 compilation of all seven finite theorems. Four use no axioms and three use only `propext`. No `sorryAx`, `native_decide` axiom, external Mathlib, or custom axiom is used. Output: `verification/current/lean-kernel.txt` and the machine-checked axiom summary.

Lean ranges: rigidity k<=6; canonical-pair identity k<=7; skeleton identity m<=6; skeleton count m<=12; the path-family classification n<=3. These are finite kernel evaluations. **The all-length theorem is not formalized** and is justified by the complete written induction.

The original C, C++, Julia and shell programs are retained without new execution claims. The current Python geometric method and the SAT model give different finite implementations. They supplement the proof rather than replacing it. Compiler/kernel/software correctness remains relevant to these supplementary checks, but no computational output is a premise of the written general proof.
