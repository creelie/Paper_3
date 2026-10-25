# Hexagon submission fields

Submit a replacement version of 2610.00474v1; do not create a duplicate work.
The new version identifier is assigned by Hexagon after submission and is not
asserted in advance. Existing record: https://hexagonmath.org/2610.00474v1

## Title

Even-intersecting families of lattice paths and the Catalan numbers

## Abstract - copy the complete block

We classify the families of $2^n$ North--East lattice paths from $(0,0)$ to $(n,n)$ in which every two distinct paths have an even number of common edges. Each family is determined by a unique noncrossing perfect matching of the $2n$ step positions: the two steps in every matched pair have opposite directions. Consequently there are exactly $\frac1{n+1}\binom{2n}{n}$ extremal families, proving the Catalan classification conjecture. More generally, we determine all equality cases of the associated weighted inequality for systems of binary words. They correspond to noncrossing partial matchings whose unmatched points lie under no arc, and their number at length $m$ is $\binom m{\lfloor m/2\rfloor}$. The proof is elementary. Its rigidity step identifies a possible exceptional pair of words and then excludes that pair from every admissible grouping. All arguments, including the underlying inequality, are given in full; finite computations are supplementary.

The block uses explicit TeX commands rather than macros defined only in main.tex.

## Subjects, tags and MSC2020

Primary subject: math.CO
Cross-list subjects: None
Tags: lattice paths, Catalan numbers, even intersections, Eventown theorem, noncrossing matchings
MSC2020 primary code: 05A15
MSC2020 additional codes: 05D05, 05A05
arXiv identifier: leave blank. No arXiv identifier is asserted.

## Contributors - preserve this order

Contributor 1: Deep Bhattacharjee
Affiliation: Formerly, Electro-Gravitational Space Propulsion Laboratory (EGSPL), Bhubaneswar, Odisha 751030, India
ORCID: 0000-0003-0466-750X

The affiliations are former affiliations, not assertions of current employment.

## Authorship and understanding selections

Text: A mix of human-written and AI-generated.
Human understanding: All parts of this contribution have been checked and understood by a human.
The user explicitly supplied both declarations for all six papers on 25 October 2026.

## Provenance statement - copy this paragraph

Claude through Claude Code assisted the original proof arguments, finite verification programs and drafting. OpenAI Codex assisted the induction and exceptional-pair audit, the nonnegative-coordinate range in the cell lemma, independent geometric-edge checks, references and typesetting. The submitting author declares that all parts have been
checked and understood by a human and takes responsibility for the content.
The Lean checks cover stated finite ranges, including path-family classification for n at most 3. The all-length classification is justified by the written induction and is not claimed to be fully formalised in Lean.

## Tools used

- Anthropic Claude / Claude Code
- OpenAI Codex
- Lean 4
- Python / SAT
- C and C++
- Julia
- LaTeX / pdfLaTeX

Use the corresponding system/tool entry if available and Other for an unlisted
tool. Do not invent a model version for an entry that is not documented.

## Formalisation links

https://github.com/creelie/Paper_3/tree/v1.2.0/verification/original/lean

Scope: The Lean checks cover stated finite ranges, including path-family classification for n at most 3. The all-length classification is justified by the written induction and is not claimed to be fully formalised in Lean.
If the portal rejects a host/path, leave it for manual review rather than
uploading Lean material in the article source ZIP.

## Files and licence

Required source ZIP: Even-intersecting_families_of_lattice_paths_and_the_Catalan_numberstex.zip
Reference PDF: Even-intersecting_families_of_lattice_paths_and_the_Catalan_numbers.pdf
AI provenance upload: AI_PROVENANCE.md (outside the source ZIP).
Licence selection: CC BY 4.0, matching the existing Hexagon manuscript record.
The manuscript source ZIP contains the article, bibliography and required
figures only. It excludes Lean developments, executables, journal correspondence,
other manuscripts and private model traces. Standard TeX Live classes/packages
are build dependencies rather than relicensed files in this ZIP.

## Review before submitting

Use pdfLaTeX, main document main.tex. The extracted ZIP was rebuilt locally and
its full extracted text and page count matched the supplied PDF. Confirm the
rendered title, abstract, byline, references and final portal preview. This
packet does not press the portal's Process or Submit button on the author's behalf.
