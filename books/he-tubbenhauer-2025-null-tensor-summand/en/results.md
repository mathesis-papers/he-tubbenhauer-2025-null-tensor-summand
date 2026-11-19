# Quantitative results and their boundaries

The following results are proved in the paper. Some still await formalization; the corresponding contribution tasks are linked in [evidence and sources](sources.md).

::: {.remark #tensor-bound title="Manuscript Theorem 2: tensor bounds over any field" mathesis="collected:he-tubbenhauer-2025-null-tensor-summand:2:s2"}
Let $S$ be a nonempty finite semigroup, let $V$ be finite dimensional over any field $k$, and let $\rho:S\to\operatorname{End}_k(V)$ be multiplicative, with every $\rho(s)$ singular. Put $d=\dim V$, $r_s=\operatorname{rank}\rho(s)$ and $t=|S|$. Then $d\geq1$. For every $n\geq1$, the diagonal action on $V^{\otimes n}$ has a finite indecomposable decomposition, and every such decomposition, with $b(n)$ pieces, satisfies

$$
d^n-2\sum_sr_s^n\leq\mu(V^{\otimes n})\leq b(n)\leq d^n.
$$

Consequently $b(n)/d^n\to1$. Whenever $n\geq1$ and $2\sum_sr_s^n<d^n$, a copy of $Z$ is a direct summand. Such an exponent always exists. Source: Section 2, Theorem 2 of the paper.
:::

The preceding chapter gives the main mechanism. For existence of indecomposable decompositions, induct on dimension: use the empty decomposition for zero; stop at a nonzero indecomposable space; otherwise split into two nonzero invariant summands of smaller dimension and continue. Each nonzero piece has dimension at least one, so there are at most $d^n$ pieces. Additivity of maximal null multiplicity gives the middle inequality; the rank formula and splitting estimate give the first.

Why is a separate assumption $V\ne0$ unnecessary? The unique endomorphism of the zero space is its identity and is invertible. Since $S$ is nonempty and every action is singular, dimension zero is excluded.

Divide by $d^n$ to obtain an explicit error:

$$
\begin{aligned}0\leq1-\frac{b(n)}{d^n}&\leq E(n),\\ E(n):=2\sum_s\left(\frac{r_s}{d}\right)^n&\leq2t\left(\frac{d-1}{d}\right)^n.\end{aligned}
$$

Each $r_s/d<1$, so this finite sum tends to zero. If $d=1$, all actions already vanish. If $d\geq2$, one sufficient exponent is

$$
m=1+\left\lfloor\frac{\log(2t)}{\log(d/(d-1))}\right\rfloor.
$$

It guarantees the strict inequality $2t(d-1)^m<d^m$; using the actual ranks can improve the test. This is not a claim of a minimal exponent. The semigroup may have an identity, but then its action must also be singular and the representation is nonunital. Ordinary nonzero unital monoid modules do not satisfy that hypothesis.

## Composition factors are different from direct summands

A **composition series** repeatedly takes invariant subspaces and quotients until the successive quotients have no proper nonzero invariant subspace. These composition factors need not split back into the original space. The opening two-dimensional chain $J$ has two zero-action composition factors but no zero-action direct summand.

::: {.remark #composition-length title="Manuscript Corollary 3: composition length approaches dimension" mathesis="collected:he-tubbenhauer-2025-null-tensor-summand:2:s3"}
Under Theorem 2's hypotheses, let $\ell(n)$ be the composition length of $V^{\otimes n}$ and $c_Z(n)$ the composition-factor multiplicity of $Z$. For each $n\geq1$,

$$
\begin{gathered}\mu(V^{\otimes n})\leq c_Z(n)\leq\ell(n)\leq d^n,\\ b(n)\leq\ell(n).\end{gathered}
$$

The ratios $\mu(V^{\otimes n})/d^n$, $c_Z(n)/d^n$ and $\ell(n)/d^n$ all tend to $1$, each with normalized deficit at most $E(n)$. Source: Section 2, Corollary 3.
:::

Finite dimension gives a composition series, with every simple factor of positive dimension. The $\mu$ null direct summands supply that many composition factors; every nonzero indecomposable piece supplies at least one factor. These observations give all the inequalities, and the main estimate squeezes the ratios to one. The composition-length asymptotic was already He–Tubbenhauer's Proposition 4.1. The addition here is a rank-based error bound; it does not recover their $\mathcal L$-class bound.

## Monoids with invertible operations

A monoid has an identity $1$, and its invertible elements form a group $G$. A unital representation sends $1$ to the identity operation, so the all-singular theorem cannot apply directly. Instead, use only the nonunits, the ideal $S=M\setminus G$, to form the common kernel and image, and require the complements to respect $G$ as well.

::: {.remark #monoid-comparison title="Manuscript Corollary 4: the nonmodular monoid comparison" mathesis="collected:he-tubbenhauer-2025-null-tensor-summand:2:s4"}
Let $M$ be a finite monoid with unit group $G$ and $V\ne0$ a finite-dimensional unital $kM$-module. Suppose only $1$ acts as the identity and $|G|$ is invertible in $k$. Put $S=M\setminus G$, $d=\dim V$ and $r_s=\operatorname{rank}\rho(s)$. For every $n\geq1$, there is an $M$-invariant decomposition

$$
\begin{gathered}V^{\otimes n}=L_n\oplus U_n,\quad SL_n=0,\\ \dim U_n\leq2\sum_{s\in S}r_s^n.\end{gathered}
$$

Thus the original Conjecture 3A.2 holds under these hypotheses: some tensor power has a nonzero direct summand obtained from a $G$-module by making all nonunits act as zero. If $b_M(n)$ and $b_G(n)$ count indecomposable pieces over $M$ and after restriction to $G$, then

$$
\begin{gathered}0\leq b_G(n)-b_M(n)\leq2\sum_{s\in S}r_s^n,\\ \frac{b_M(n)}{b_G(n)}\to1.\end{gathered}
$$

When $G=\{1\}$, over every field, $b_M(n)/d^n\to1$ without the composition-ratio hypothesis of the original Proposition 3C.2. Source: Section 3, Corollary 4.
:::

If a nonunit $s$ acted invertibly, finiteness would provide a positive idempotent power $e$ of $s$. Its action would be both invertible and idempotent, hence the identity. The hypothesis forces $e=1$, making $s$ a unit: a contradiction. Thus every nonunit has rank smaller than $d$.

Multiplication by units permutes $S$, so $K$ and $I$ are $G$-invariant. When $|G|$ is invertible, Maschke's theorem allows $G$-invariant complements: first choose $L_n$ inside $K$, then choose a complement $U_n$ containing $I$. Nonunits kill the former and send the latter into $I$, making both $M$-invariant with the same dimension bound.

The pieces of $L_n$ are the same over $M$ and $G$. Group modules here are semisimple; the number of pieces contributed by restricting $U_n$ is at most $\dim U_n$, which bounds the difference of counts. Each simple $kG$-module has dimension at most $|G|$, so $b_G(n)\geq d^n/|G|$. Division still gives geometric decay. If $S$ is empty, simply take $L_n=V^{\otimes n}$ and $U_n=0$.

In a field of prime characteristic $p$, integers are computed modulo $p$, so invertibility of $|G|$ requires that $p$ not divide the group order. In characteristic zero, as for rational, real or complex numbers, this condition always holds.

This does not settle the case where the field characteristic divides a nontrivial $|G|$. The source's $\operatorname{Ind}$ means extension by zero on nonunits, not tensor induction. The comparison supplies a leading asymptotic for total counts, not the source's specified spectral error formulas or subgroup-specific exact multiplicities.
