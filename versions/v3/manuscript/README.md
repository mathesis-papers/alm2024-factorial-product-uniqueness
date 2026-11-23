# Equal products of m!/m^m over distinct parameter sets

Haobo Ma (ChronoAI Pte Ltd, Singapore) and Wenlin Zhang (National University of
Singapore; ChronoAI Pte Ltd, Singapore).

## Result

Ma and Zhang give a prime-exponent proof answering Problem 5.6 of Aivazidis,
Loukaki and Müller negatively.
Two disjoint eighteen-element sets of integers greater than one have equal
products of `m! / m^m` and the same parameter sum, 965. The proof gives an
adjacent-ratio identity and a ten-prime exponent table. Adjoining common
parameters gives distinct sets of every equal cardinality at least eighteen
with equal sums. For each cardinality at least nineteen, infinitely many
rational values have two such representations. The original eighteen-element
sets are disjoint; the common-parameter extensions are not disjoint.

The posing locator is Problem 5.6, page 1281, in *Journal of Group Theory*
27 (2024), no. 6, 1233–1285, DOI `10.1515/jgth-2024-0030`; the preprint
locator is Problem 5.6, page 37, arXiv `2209.00986v2` (May 31, 2023).
The first version, arXiv `2209.00986v1` (September 2, 2022), poses the question
without the distinctness restriction as Problem 12.6, page 38. The example
answers that version as well.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a standard TeX installation with `pdflatex`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is contained in `note.tex`; no BibTeX database or figures are
required.

## Exact arithmetic

Python 3.9 or later, using its standard library:

```sh
python3 verify.py > verification.json
```

The checker independently evaluates the factorial-weight products and the
adjacent ratios as exact rational numbers. Trial division supplies the prime
exponents in the proof table. It also checks disjointness, cardinalities,
the adjacent-pair reconstruction, equality of the parameter sums, and all
decreasing partial sums. It evaluates common-parameter extensions at
cardinalities 18, 19, 20 and 25 and three distinct common product values.
Failure gives a nonzero exit status, including when Python assertions are
disabled. `verification.json` records the expected mathematical output.

## Mathematical coverage

The note contains written proofs of the counterexample, its common-parameter
extension, infinitely many multiply represented values, and uniqueness for
coordinatewise-comparable lists. The finite checks cover the explicit sets,
prime-exponent table, sums, partial sums and the listed finite extensions.
Universal conclusions follow from the written proofs, not finite sampling.
The pinned Lean declaration
`D5.S3.FiniteGroups.FactorialProductNonunique.result` proves the negation of
finite-set factorial-weight uniqueness, using the same sets; the weight is
`D5.S3.FiniteGroups.TransversalProbabilityMonotone.orbitWeight`.
Their source links at commit `736015507f370926a4b39c6a5ca4f090fc50cae3` appear in
the note; `metadata.json` also links the counterexample declaration. That
declaration does not state the equal-sum or arbitrary-cardinality corollaries. The
prime-side uniqueness theorem (Theorem 4.6)
has different hypotheses. The source's Appendix A gives majorisation
comparison results; the two parameter vectors are incomparable in weak
majorisation (first partial sums 141 > 140, ninth partial sums 714 < 715).
Problems 5.1–5.5 and 5.7–5.8 are itemized as not covered. The note makes no
claim that eighteen is the least possible counterexample cardinality.

## License

Copyright 2026 Haobo Ma and Wenlin Zhang. Creative Commons Attribution 4.0
International, `CC BY 4.0` (`cc-by-4.0`).
