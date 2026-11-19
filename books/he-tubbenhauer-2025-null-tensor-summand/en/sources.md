# Exact Lean comparison, sources and participation

## What does the public theorem actually say?

Only the following narrower statement, exactly matching the public Lean declaration, receives a Lean theorem reference here. It is an explicit specialization of manuscript Theorem 2, not verification of the whole paper.

::: {.theorem #original-conjecture title="The public Lean statement of the original Conjecture 4.2" lean="D5/S3/HomologicalAlgebra/TensorNullSummand.result" mathesis="collected:he-tubbenhauer-2025-null-tensor-summand:2:s2"}
For every algebraically closed field $k$, nonempty finite semigroup $S$, finite-dimensional $k$-vector space $V$, and multiplicative map $\rho:S\to\operatorname{End}_k(V)$, if $S$ has no two-sided identity and every $\rho(s)$ is noninvertible, then:

1. There exists $m\in\mathbb N$, $m\geq1$, such that $V^{\otimes m}$ with its diagonal action has a one-dimensional zero-action direct summand with an invariant complement.
2. There exists a sequence $b:\mathbb N\to\mathbb N$ such that, for each $n\in\mathbb N$, $b(n)$ counts some finite internal indecomposable decomposition of $V^{\otimes n}$.
3. Every sequence $b$ satisfying that count condition has $b(n)/(\dim_k V)^n\to1$.
:::

The second and third clauses include $n=0$, with the zeroth tensor power equal to $k$. Existence of a count sequence and convergence for every count sequence are separate assertions. The null summand is an actual one-dimensional subspace with an invariant complement. Each counted piece is nonzero, invariant under every operation and admits no nontrivial invariant direct-sum splitting. The same operation acts in each tensor slot. This says more than finding $Z$ in a quotient or choosing one favourable decomposition.

Read the [public theorem source](lean:D5/S3/HomologicalAlgebra/TensorNullSummand.result) at the [cited revision](trureturing:). The formalized statement has the hypotheses and conclusions listed above.

## How the whole paper differs from this one theorem

| Manuscript result | Relationship to public Lean | Shared request |
|---|---|---|
| Lemma 1: maximal null multiplicity | Complement construction is available; the public theorem does not state maximality, additivity or exact multiplicity | [Maximal multiplicity and rank bound](https://github.com/the-omega-institute/trureturing-requests/issues/44) |
| Theorem 2: quantitative bounds over any field | The public theorem is a qualitative special case; the complete quantitative statement remains to formalize | [Any-field tensor bounds](https://github.com/the-omega-institute/trureturing-requests/issues/45) |
| Corollary 3: composition length and error | No matching public composition-factor statement was identified | [Composition multiplicities and length](https://github.com/the-omega-institute/trureturing-requests/issues/46) |
| Corollary 4: monoid comparison | Different from the all-singular semigroup conclusion | [Nonmodular monoid comparison](https://github.com/the-omega-institute/trureturing-requests/issues/47) |
| Corollary 5: right-zero decomposition and correction | No matching public exact decomposition and classification was identified | [Right-zero decomposition](https://github.com/the-omega-institute/trureturing-requests/issues/48) |
| Corollary 6: exact group-union counts | No matching public complex-character count was identified | [Group-union example](https://github.com/the-omega-institute/trureturing-requests/issues/49) |
| Proposition 7: Jordan tensor multiplicities | Public Jordan-chain and iterate-rank theorem is a related ingredient, not these tensor-count formulas | [Jordan tensor multiplicities](https://github.com/the-omega-institute/trureturing-requests/issues/50) |
| Corollary 8: published matrix recurrence | No matching public recurrence statement was identified | [Fusion-matrix recurrence](https://github.com/the-omega-institute/trureturing-requests/issues/51) |

The source also contains ingredients under weaker hypotheses, including existence and convergence without algebraic closure or the exclusion of an identity. Those ingredients do not state all the quantitative formulas above. The related [Jordan-chain theorem](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S1/Eigenstructure/NilpotentJordanChains.lean) supplies general chain and rank machinery; deriving the paper's exact tensor multiplicities remains a separate task. The repository retains a [detailed statement comparison](https://github.com/mathesis-papers/he-tubbenhauer-2025-null-tensor-summand/blob/main/.mathesis/REVIEW.md).

## Sources, DOI and priority

This explanation accompanies Haobo Ma and Wenlin Zhang's [public version 2](https://mathesis-omega-research.apps.chrono-ai.fun/papers/he-tubbenhauer-2025-null-tensor-summand?version=2), dated 5 November 2026 and collected on 14 November. No DOI is currently recorded for this paper.

Sources are listed by their mathematical role. The original paper in this repository contains the exact arguments for its results.

- David He and Daniel Tubbenhauer, [Tensor powers of representations of (diagram) monoids](https://arxiv.org/abs/2508.04054v1), 2025: Conjectures 4.2 and 3A.2, Propositions 4.1 and 4.4, Example 4.3. Credit for those questions and prior results remains with them.
- The same authors, [Affine diagram categories, algebras and monoids](https://arxiv.org/abs/2512.05510v2), version of 19 December 2025: Theorem 4A.14(e)–(f) already proves the right-idempotent-generated case. The later v3 and journal version cited in the manuscript do not change that first-proof date.
- The same authors, [Growth problems for representations of finite monoids](https://arxiv.org/abs/2502.02849v1), Example 2.2; v2, Example 1. This is the source of the group-union example.
- D. B. McAlister, [The category of representations of a completely 0-simple semigroup](https://doi.org/10.1017/S1446788700009460), 1971, Definition 1.4 and Corollary 2.6: antecedents for null direct summands.
- D. Juteau, C. Mautner and G. Williamson, [Parity sheaves](https://doi.org/10.1090/S0894-0347-2014-00804-3), preprint 2009, journal 2014, Lemma 3.1: antecedent multiplicity pairing.
- R. A. Brualdi, [Combinatorial verification of the elementary divisors of tensor products](https://doi.org/10.1016/0024-3795(85)90233-2), 1985, Theorem 4.6(4): nilpotent tensor blocks.
- K. Coulembier, V. Ostrik and D. Tubbenhauer, [Growth rates of the number of indecomposable summands in tensor powers](https://doi.org/10.1007/s10468-023-10245-7), 2024, Theorem 1.4(a), Remark 1.5(a): background root growth for general representations. A root limit is different from the ratio limit here.
- P. Etingof and collaborators, [Introduction to representation theory](https://math.mit.edu/~etingof/reprbook.pdf), 2011, Theorems 3.8.1 and 4.1.1(i): Krull–Schmidt and Maschke.

The paper leaves extensions to infinite semigroups, modular characteristic with nontrivial unit groups, the original spectral error formulas, subgroup-specific multiplicities and other listed integer sequences unresolved. Its finite computations cover specified sizes and exponents; the general conclusions rest on the written arguments.

## How to contribute

Choose a result in the table and join its linked request to coordinate a formalization. The [contribution guide](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md) explains how to submit a proof. Each completed contribution should identify the precise statement it proves, alongside credit for the original mathematics and the formalization.

<section hidden="hidden">

```{=typst}
#pagebreak()
```

</section>
