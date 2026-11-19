# Why subtract two copies of the ranks?

## Kernels, images and the obstruction to splitting

A **field** is a number system with the usual addition, subtraction, multiplication and division by nonzero numbers: for example the rationals, reals or complex numbers, or arithmetic modulo a prime. A **linear** operation respects vector addition and scalar multiplication. A subspace is **invariant** if applying an operation to any vector in it keeps the vector inside it. The notation $W=L\oplus U$ means every vector has a unique expression as one vector from $L$ plus one from $U$.

For the moment the operations need not come from a semigroup. Let $W$ be a finite-dimensional vector space over any field $k$, with a finite family of linear operations $(A_s)_{s\in F}$. The **kernel** consists of inputs sent to zero; the **image** consists of possible outputs. Intersect all kernels and add all images:

$$
\begin{aligned}K&=\bigcap_s\ker A_s,\\ I&=\sum_s\operatorname{im}A_s,\\ R&=\sum_s\operatorname{rank}A_s.\end{aligned}
$$

Every vector of $K$ is killed, while $I$ contains every output. Their intersection $K\cap I$ is the obstruction: these vectors no longer move, but other vectors can move into them. Splitting all of them into a zero-action piece may leave a complement that is not invariant.

For the opening operation $J$, we have $K=I=ke_0$, so $K\cap I=K$ and no zero-action summand splits off. A nonzero common kernel is far from sufficient.

::: {.remark #null-multiplicity title="Manuscript Lemma 1: maximal null multiplicity" mathesis="collected:he-tubbenhauer-2025-null-tensor-summand:2:s1"}
Section 1, Lemma 1 of the paper proves, for the arbitrary finite operator family above, an invariant decomposition $W=L\oplus U$ with $L\subseteq K$, $I\subseteq U$ and

$$
\begin{aligned}\mu(W)=\dim L&=\dim K-\dim(K\cap I)\\ &\geq\dim W-2R.\end{aligned}
$$

The quantity $\mu$ is additive on invariant direct sums and equals the number of copies of $Z$ in every indecomposable decomposition. Here $\mu$ means the maximal dimension of a zero-action invariant direct summand.
:::

## Read the construction directly

Inside $K$, choose a complement $L$ to $K\cap I$. This is a basis choice: start with a basis of the intersection, extend it to one of $K$, and let the added vectors span $L$. Then $L\cap I=0$. Combine bases of $L$ and $I$ and extend them to a basis of $W$; let $U$ contain $I$ and the final extra basis vectors. This gives $W=L\oplus U$.

Every $A_s$ kills $L$ and sends $U$ into $I\subseteq U$, so both pieces are invariant. This explains why we deliberately place every possible output in the complement.

Conversely, for any invariant splitting $W=L'\oplus U'$ with zero action on $L'$, all outputs lie in $U'$, so $L'\cap I=0$. Consequently $L'$ injects into $K/(K\cap I)$ and cannot have dimension larger than the constructed $L$. The formula really is a maximum.

How big is it? The map $w\mapsto(A_sw)_s$ has kernel $K$, giving $\dim W-\dim K\leq R$. Also $\dim I\leq R$, hence $\dim(K\cap I)\leq R$. Lose at most $R$ dimensions to reach the common kernel, then at most another $R$ to remove the obstruction. At least $\dim W-2R$ remain.

On an invariant direct sum the operations are block diagonal, and $K$, $I$ and their intersection also split as direct sums. The dimension formula is therefore additive. If an indecomposable block has positive $\mu$, the construction splits off a nonzero zero-action piece inside it. Indecomposability forces the whole block to have zero action; such a space is indecomposable only in dimension one. This identifies the exact number of $Z$ copies.

## Why do tensor powers improve the balance?

Choose a $d$-element basis of the original space. Basis words in $n$ slots number $d^n$. For a single operation $A$, factor it as a surjection onto $\operatorname{im}A$ followed by inclusion into $V$. Over a field, tensoring preserves these surjections and injections, as bases and linear sections show. Thus

$$
\operatorname{rank}(A^{\otimes n})=(\operatorname{rank}A)^n.
$$

Apply the splitting estimate to the tensor operations to obtain the main inequality. The exact rank identity and maximal-multiplicity formula follow from the written arguments above. Their current formalization status is explained in [evidence and sources](sources.md).

A hand calculation: for $d=2$ and $S=\{0,J\}$, the ranks are $0,1$, and the lower bound is $2^n-2$. At $n=1$ it is zero; at $n=2$ it is two, matching the two independent zero-action directions in the opening tensor square. A general lower bound can be negative: that means the estimate gives no positive information, not that multiplicity is negative.
