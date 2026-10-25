# Even-intersecting lattice paths and Catalan numbers

## Current upload package

[Paper_3 package](Paper_3%20package/README.md) contains the reviewed Hexagon/Overleaf source ZIP, the current PDF, AI provenance, complete Hexagon fields and supporting files for **Journal of Combinatorial Theory, Series A**. The package records the current proof/check scope and has no margin line numbers. No journal submission or acceptance is claimed. Version: 1.3.0.


**Sole author: Deep Bhattacharjee.** Submission revision 1.2.0, 24 October 2026.

Every family of 2^n North-East lattice paths from (0,0) to (n,n) with pairwise even numbers of common edges comes from a unique noncrossing perfect matching of the step positions. The two letters at each matched pair are opposite. There are exactly C_n such extremal families. The manuscript proves the stronger classification of equality in the underlying binary-word inequality for every length m, with exactly binom(m,floor(m/2)) extremal systems.

- [Submission manuscript](Paper_3_Annals.pdf)
- [Revision DOI](https://doi.org/10.5281/zenodo.23608134)
- [Original preprint: hexagon:2610.00474v1](https://hexagonmath.org/2610.00474v1)
- [Preceding archive, version 1.1.0](https://doi.org/10.5281/zenodo.23552911)
- [Source repository](https://github.com/creelie/Paper_3)

The main theorem has a complete written proof for all lengths. The inequality originally stated in Shankar's question paper is reproved here. No unproved mathematical statement from that preprint is used as a premise. Finite computations are supplementary. The seven accompanying Lean theorems concern stated finite ranges only; they do not formalize the all-length classification.

Prepared in `aomart` for possible submission to Annals of Mathematics. No journal submission, peer review or acceptance has been obtained. Correctness and editorial significance are separate questions; acceptance cannot be guaranteed. The Electronic Journal of Combinatorics is a natural specialist alternative if the author chooses it, subject to exclusive-submission requirements.

## Reproduce

Standard-library-only independent exact checks:

```
python scripts/verify.py
```

These encode actual geometric edge sets, check the rigidity and cell lemmas through word length 9, skeleton identities through length 8, and enumerate all extremal path families for n <= 4. They do not extrapolate those finite checks to all lengths.

Fresh core-Lean finite checks and axiom audit (Lean 4.34.1):

```
python scripts/verify.py --lean /path/to/lean
```

The original optional SAT checks require `python-sat==1.9.dev17`:

```
python verification/original/python/verify_sat.py 5 4
```

This checks all extremal systems through m=5, all path families through n=4, groupings through k=7 and rigidity through k=9. The original C, C++, Julia and shell programs are preserved; they were not freshly executed for this revision. See [VERIFICATION.md](VERIFICATION.md).

Build the manuscript and its three vector figures with a TeX distribution containing aomart, aomplain and TikZ:

```
python scripts/build_manuscript.py
```

The final single ZIP is made only after the public Zenodo record is confirmed and its PDF checksum matches. `scripts/package_submission.py` enforces this. See [PROOF-AUDIT.md](PROOF-AUDIT.md) and [SELECTION-NOTES.md](SELECTION-NOTES.md) for proof scope and literature screening.
