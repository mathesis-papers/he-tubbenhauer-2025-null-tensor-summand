# Quantitative null tensor summands

This revision extends He–Tubbenhauer’s December 2025 right-idempotent-generated
case to Conjecture 4.2 of *Tensor powers of representations of (diagram)
monoids*, arXiv:2508.04054v1, p. 17, over every field. It combines classical
null-splitting and multiplicity principles with tensor-rank decay.

## Mathematical coverage

- For finite singular semigroup actions of dimension `d` and ranks `r_s`,
  `d^n−2 sum_s r_s^n ≤ mu(V^(tensor n)) ≤ b(n) ≤ d^n`; hence `b(n)/d^n→1`.
- The exact maximal null multiplicity is `dim K−dim(K∩I)`, a specialization
  of the composition-pairing principle of Juteau–Mautner–Williamson (2009).
  McAlister’s 1971 criterion is an earlier semigroup antecedent.
- Conjecture 3A.2 holds when the finite unit-group order is invertible in the
  field. The monoid and unit-group counts differ by at most `2 sum_s r_s^n`.
  The trivial-unit-group case holds in every characteristic.
- A two-element right-zero semigroup satisfies Proposition 4.4’s uniform
  composition-ratio hypothesis but has `b(n)=2^n−1`, not `2^n`, for every
  positive exponent. The replacement `b(n)~d^n` holds without that hypothesis.
- Every nilpotent Jordan-block multiplicity is a second difference of tensor
  ranks, consistent with Brualdi’s classical two-factor decomposition (1985).
- The published Example 4.3 fusion matrix gives `b(n)=6^n−7` and null
  multiplicity `6^n−8` for `n≥2`.
- The earlier `C2 ∪ S3 ∪ {0}` example has exact null multiplicity
  `3^n−2^n−1` and total count `3^n−(2^n−(−1)^n)/3` for `n≥1`.

The source item coverage table distinguishes proved assertions, the
refuted-and-corrected finite-exponent display, credited earlier results, and
statements outside the stated hypotheses. Only `ht2508` is a problem identifier;
the related source locators are recorded in the note without additional IDs.

## Files and building

The source archive contains `note.tex`, `metadata.json`, `verify.py`,
`verification.txt`, this `README.md`, and `SHA256SUMS`. The typeset `note.pdf`
is supplied separately. The bibliography is embedded in the LaTeX source.

Use Tectonic 0.17.0:

```sh
tectonic --untrusted note.tex
```

Alternatively, with a LaTeX distribution:

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error note.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error note.tex
```

The source uses standard AMS, geometry, booktabs, tabularx, Latin Modern,
microtype and hyperref packages. BibTeX is unnecessary.

## Exact finite checks

```sh
python3 verify.py > verification-new.txt
diff -u verification.txt verification-new.txt
```

The checker uses only Python’s standard library. It covers all 1023 nonempty
families of singular binary 2×2 matrices at tensor exponents 1–3, every
null-image projection at exponent 1, and the full-family exponent-5 bound.
It checks all block sizes in 25 Jordan-chain cases (`2≤d≤6`, `1≤n≤5`), the
published fusion matrix through exponent 12, and explicit right-zero
decompositions at exponents 1–7. It also checks the earlier semigroup example
through exponent 12. The universal statements have written proofs;
the computations cover precisely these finite ranges.

## Lean declaration scope

The declaration `D5.S3.HomologicalAlgebra.TensorNullSummand.result` proves
Conjecture 4.2 under the original algebraically closed-field and finite
identity-free-semigroup hypotheses: a positive null direct summand, existence
of an indecomposable-count sequence and the ratio limit for every such sequence.
In the same file, `exists_null_tensor_power`, `exists_summand_count` and
`tensor_counts_tendsto` give the existence/count-limit statements over any
field without excluding a semigroup identity. The tensor-rank declaration
`tensor_power_range_le` is an upper bound, not an equality.

The pinned file is:
https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/HomologicalAlgebra/TensorNullSummand.lean

The exact maximal-multiplicity identity, exact tensor-rank identity, nonmodular
monoid corollary, right-zero decomposition, Jordan formulas and fusion recurrence
have the written proofs in the note. `verification.txt` gives the finite ranges.

## Creators and license

1. Haobo Ma — ChronoAI Pte Ltd, Singapore.
2. Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

Creative Commons Attribution 4.0 International (CC BY 4.0; `cc-by-4.0`).
https://creativecommons.org/licenses/by/4.0/
