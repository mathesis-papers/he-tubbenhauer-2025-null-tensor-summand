# Four examples we can calculate exactly

## Always one piece short, still asymptotically equal

Consider two plane operations: $P(a,b)=(a,0)$ and $Q(a,b)=(a+b,0)$. Both put their outputs on the horizontal axis but kill different directions. They satisfy $P^2=P$, $Q^2=Q$, $PQ=Q$, $QP=P$, giving a representation of a right-zero semigroup.

::: {.remark #right-zero title="Manuscript Corollary 5: right-zero example and finite-exponent correction" mathesis="collected:he-tubbenhauer-2025-null-tensor-summand:2:s5"}
Over any field, let $S=\{x,y\}$ with $st=t$ and

$$
\rho(x)=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
\rho(y)=\begin{pmatrix}1&1\\0&0\end{pmatrix}.
$$

For every $n\geq1$,

$$
V^{\otimes n}\cong V\oplus Z^{\oplus(2^n-2)},\qquad b(n)=2^n-1.
$$

Every indecomposable $kS$-module other than $Z$ has null composition-factor fraction at most $1/2$. Thus the hypothesis of He–Tubbenhauer's Proposition 4.4 holds with $c=3/4$, while its printed literal finite-exponent equality fails. Its asymptotic replacement holds. Source: Section 4, Corollary 5.
:::

In an arbitrary representation write the actions as $P,Q$. The relations force them to share the same image $E$. Using $W=E\oplus\ker P$, their matrices become

$$
P=\begin{pmatrix}1_E&0\\0&0\end{pmatrix},\qquad Q=\begin{pmatrix}1_E&C\\0&0\end{pmatrix}.
$$

Independent changes of basis in the domain and codomain of $C$ put it in rank normal form. The representation splits into three kinds of pieces: the displayed two-dimensional $V$, a one-dimensional $T$ on which both elements act as one, and $Z$. The common kernel of $V$ is zero, excluding $Z$ as a summand; $P\ne Q$ excludes $T\oplus T$. Thus $V$ is indecomposable. Its horizontal axis is $T$ and its quotient is $Z$, so the non-$Z$ indecomposables have null composition fractions zero and one half.

In a tensor power the image remains $ke_0^{\otimes n}$, and the output coefficients are the covectors $(e_0^*)^{\otimes n}$ and $(e_0^*+e_1^*)^{\otimes n}$. They are independent. The common kernel has dimension $2^n-2$ and meets the image trivially. The remaining two-dimensional piece, on $e_0^{\otimes n},e_1^{\otimes n}$, is again $V$. This proves the exact decomposition.

| $n$ | Dimension $2^n$ | Null direct summands | Total pieces $b(n)$ | $b(n)/2^n$ |
|---|---|---|---|---|
| 1 | 2 | 0 | 1 | $1/2$ |
| 2 | 4 | 2 | 3 | $3/4$ |
| 3 | 8 | 6 | 7 | $7/8$ |
| 4 | 16 | 14 | 15 | $15/16$ |

The count is one short each time; the relative deficit is $2^{-n}$ and tends to zero. This corrects a pointwise equality, rather than contradicting the valid asymptotic conclusion.

## Two group actions: all mixed words vanish

::: {.remark #group-union title="Manuscript Corollary 6: exact counts for the earlier group-union example" mathesis="collected:he-tubbenhauer-2025-null-tensor-summand:2:s6"}
In He–Tubbenhauer's arXiv:2502.02849v1, Example 2.2 (v2, Example 1, p. 3), let $S=C_2\cup S_3\cup\{0\}$, with cross-products between the groups zero. Over the complex numbers take the specified module $V=X\oplus Y$, where $X$ is the nontrivial one-dimensional $C_2$-representation and $Y$ the standard two-dimensional $S_3$-representation; the other group acts by zero on each respective part. For every $n\geq1$,

$$
\begin{aligned}\mu(V^{\otimes n})&=3^n-2^n-1,\\ b(n)&=3^n-\frac{2^n-(-1)^n}{3}.\end{aligned}
$$

Source: Section 5, Corollary 6. The example and its earlier asymptotic belong to the original authors.
:::

Expand $(X\oplus Y)^{\otimes n}$. Every basis word mixing $X$ and $Y$ is killed by every semigroup element; these words have total dimension $3^n-1-2^n$. The relevant group identity acts as the identity on each pure word, excluding null summands there. The pure $X$ word contributes one piece.

For the pure $Y$ word use characters, which record traces of the operations. On the identity, transpositions and three-cycles of $S_3$, the character of $Y$ is $(2,0,-1)$, and the sum of the three irreducible characters is $(4,0,1)$. Their inner product, weighted by class sizes $1,3,2$, gives $b_{S_3}(n)=(2^{n+1}+(-1)^n)/3$. Add the pure $X$ and mixed-word counts to get the displayed formula. At $n=1$, $\mu=0,b=2$; at $n=2$, $\mu=4,b=8$.

## Exact counts for downward chains

::: {.remark #jordan-counts title="Manuscript Proposition 7: nilpotent tensor-chain formulas" mathesis="collected:he-tubbenhauer-2025-null-tensor-summand:2:s7"}
For $d\geq2$, let $J_de_i=e_{i-1}$ for $1\leq i<d$ and $J_de_0=0$. Let the semigroup of its positive powers, including zero, act on $k^d$ over any field. For every $n\geq1$,

$$
\begin{aligned}b(n)&=d^n-(d-1)^n,\\ \mu(V^{\otimes n})&=d^n-2(d-1)^n\\ &\quad +(d-2)^n.\end{aligned}
$$

More precisely, the number of blocks of size exactly $j$ is

$$
\begin{aligned}m_j(n)&=(d-j+1)^n-2(d-j)^n\\ &\quad+\max(d-j-1,0)^n,\\ &\qquad 1\leq j\leq d.\end{aligned}
$$

Source: Section 5, Proposition 7 and equation (6) in its proof. These are explicit consequences of classical nilpotent Jordan theory; Brualdi gave the two-factor decomposition in 1985.
:::

Label the tensor basis by $\{0,\ldots,d-1\}^n$. The operation $B=J_d^{\otimes n}$ lowers every coordinate by one, sending the whole vector to zero when some coordinate is zero. Distinct nonzero basis images stay distinct, so the basis graph is a disjoint union of finite chains. Each chain span is invariant under every power of $B$.

A chain of length $h$ is indecomposable: its commuting endomorphisms form $k[x]/(x^h)$, whose only idempotents are zero and one. A nontrivial invariant splitting would supply another idempotent projection. Each chain contributes one to dimension minus rank, giving $d^n-(d-1)^n$ chains. Singleton chains are exactly $Z$. A chain of length $h$ contributes one to

$$
\dim W-2\operatorname{rank}B+\operatorname{rank}B^2
$$

when $h=1$, and zero otherwise. Since $\operatorname{rank}B^q=\max(d-q,0)^n$, the same second-difference calculation gives every $m_j(n)$.

There are no singleton chains at $n=1$ and exactly two at $n=2$, independently of $d$. Taking $d=2,n=1$ gives $\mu=0$ and total rank one, showing that the constant $2$ in the universal estimate cannot be decreased.

## Reading a recurrence from the printed matrix

::: {.remark #fusion-counts title="Manuscript Corollary 8: the published fusion-matrix recurrence" mathesis="collected:he-tubbenhauer-2025-null-tensor-summand:2:s8"}
The matrix in He–Tubbenhauer's arXiv:2508.04054v1, Example 4.3 and Figure 9, p. 17, using column vectors and ordered vertex dimensions $(1,6,1,8)$ with the third vertex equal to $Z$, yields for every $n\geq2$

$$
b(n)=6^n-7,\qquad [V^{\otimes n}:Z]_b=6^n-8.
$$

Source: Section 5, Corollary 8. The conclusion concerns the recurrence of the published matrix.
:::

Explicitly,

$$
\begin{gathered}A=\begin{pmatrix}0&0&0&0\\1&0&0&0\\0&28&6&40\\0&1&0&1\end{pmatrix},\\ v_0=(1,0,0,0)^T,\quad v_{n+1}=Av_n.\end{gathered}
$$

Direct multiplication gives $v_2=(0,0,28,1)^T$. If $v_n=(0,0,6^n-8,1)^T$, the next third coordinate is $6(6^n-8)+40=6^{n+1}-8$, and the fourth stays one. Induction gives the null multiplicity in the third coordinate and the total count by summing coordinates. Weighting by dimensions recovers $(6^n-8)+8=6^n$. At $n=2$ there are $28$ null pieces and $29$ pieces in total; the formula does not claim to hold at $n=1$.
