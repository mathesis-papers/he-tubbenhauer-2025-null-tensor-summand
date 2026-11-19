# Larger tensor powers, more independent zero-action pieces

**Haobo Ma · Wenlin Zhang, version 2.** Haobo Ma: ChronoAI Pte Ltd, Singapore; Wenlin Zhang: National University of Singapore and ChronoAI Pte Ltd, Singapore. This bilingual explanation accompanies the original paper and retains its authors, version and CC BY 4.0 licence.

## Start with an operation that loses information

Think of a pair of numbers $(a,b)$ as a vector in a plane. The operation $J(a,b)=(b,0)$ squeezes the plane onto the horizontal axis; applying it twice gives zero. This is a **singular** operation: you cannot recover all the input information. Every vector on the horizontal axis is killed by $J$, yet that axis cannot be split off as an independent zero-action piece. Why? Any other line that completes the plane contains a vector outside the horizontal axis. Its image is a nonzero horizontal vector, outside that other line, so the other line is not preserved by the operation.

Finding a killed vector and splitting off an independent zero-action direct summand are therefore different achievements. The paper asks for the second.

Now keep two input slots. If $e_0,e_1$ are the original basis directions, give each combination $e_0\otimes e_0,e_0\otimes e_1,e_1\otimes e_0,e_1\otimes e_1$ its own coordinate. This is the **tensor square**, of dimension $2^2=4$; $n$ slots give dimension $2^n$. Apply the same operation in every slot: this is the diagonal tensor action. For $J$, only $e_1\otimes e_1$ has a nonzero image, namely $e_0\otimes e_0$. The other two directions each split off as independent zero-action summands. Something that could not split off in the original plane appears in its tensor square.

## Can we handle several operations at once?

The paper studies a finite set of operations closed under composition, with an associative multiplication rule. This is a **finite semigroup**. A representation assigns a linear operation $\rho(s)$ to each element $s$, with $\rho(st)=\rho(s)\rho(t)$. An identity is not required, and the representation need not preserve one.

Let $d$ be the original dimension and $r_s$ the rank of $\rho(s)$: the dimension spanned by all its outputs. Assume every operation is singular, so $r_s<d$. After taking $n$ tensor slots the total dimension is $d^n$, whereas the rank of each operation is only $r_s^n$. The dimensions that the operations can occupy become a shrinking fraction of the whole.

A large common zero space alone is still insufficient. The key is to separate it from all possible outputs. The [next chapter](mechanism.md) explains the cost of “two copies of the ranks.” The main conclusion is

$$
d^n-2\sum_{s\in S}r_s^n\leq\mu(V^{\otimes n})\leq b(n)\leq d^n.
$$

Here $\mu$ is the largest dimension of a zero-action direct summand; write $Z$ for a one-dimensional zero-action representation. To define $b(n)$, split the space into nonzero invariant pieces that admit no further invariant direct-sum splitting, then count those pieces, counting repeated isomorphic pieces separately. This counts neither basis vectors nor composition factors.

The short film follows the same example through common kernels, common images and rank decay.

::: {.film src="001-null-summands"}
From being killed to splitting off independently: a two-dimensional chain and its tensor basis explain null direct summands.
:::

## Why does the result matter?

Knowing only $b(n)^{1/n}\to d$ would not tell us that $b(n)$ is close to $d^n$: the sequence $d^n/\sqrt n$ has $n$th root tending to $d$, but its ratio to $d^n$ tends to zero. This result gives the stronger **ratio limit** $b(n)/d^n\to1$, with an explicit error. Most of the dimension eventually comes from one-dimensional zero-action pieces. It does not say that every finite tensor power has exactly $d^n$ pieces.

The question comes from David He and Daniel Tubbenhauer's [arXiv:2508.04054v1, Conjecture 4.2, p. 17](https://arxiv.org/abs/2508.04054v1). They proved the right-idempotent-generated case in 2025. This paper extends the finite singular-semigroup conclusion to every field and removes that generation hypothesis. The common-kernel/common-image splitting principle has antecedents in McAlister and Juteau–Mautner–Williamson; the application combines it with tensor-rank decay. The [examples chapter](examples.md) exhibits $b(n)=2^n-1$: always one short, yet with exactly the asserted ratio limit.

The academic talk follows the same story before giving precise hypotheses and sources.

::: {.slides src="null-summands"}
Aligned Chinese and English Beamer editions, with speaker notes explaining the proof mechanism and its scope.
:::

See [quantitative results](results.md) for complete statements and [evidence and sources](sources.md) for the exact public Lean coverage and contribution route.
