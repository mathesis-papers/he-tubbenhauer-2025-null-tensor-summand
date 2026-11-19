# 精确的 Lean 对照、来源与参与

## 公开定理究竟说了什么？

本书只给下面这个较窄的、与公开 Lean 陈述完全相同的结果使用 Lean 定理引用。它是原论文定理 2 的一个明确特例，不是整篇论文的验证。

::: {.theorem #original-conjecture title="原猜想 4.2 的公开 Lean 陈述" lean="D5/S3/HomologicalAlgebra/TensorNullSummand.result" mathesis="collected:he-tubbenhauer-2025-null-tensor-summand:2:s2"}
对任意代数闭域 $k$、任意非空有限半群 $S$、任意有限维 $k$-向量空间 $V$ 及乘法映射 $\rho:S\to\operatorname{End}_k(V)$，若 $S$ 没有双边单位元且每个 $\rho(s)$ 都不可逆，则：

1. 存在 $m\in\mathbb N$、$m\geq1$，使对角张量作用下的 $V^{\otimes m}$ 有一维零作用直和项，并且有不变补空间。
2. 存在序列 $b:\mathbb N\to\mathbb N$，对每个 $n\in\mathbb N$，$b(n)$ 计数 $V^{\otimes n}$ 的某个有限内部不可分解分解。
3. 对每个满足上一条计数条件的序列 $b$，都有 $b(n)/(\dim_k V)^n\to1$。
:::

这里第二、三条包括 $n=0$，采用零次张量幂为 $k$ 的约定。存在计数序列与所有计数序列满足极限是两项独立断言。零作用直和项是实际的一维子空间，并且有不变补空间。计数中的每个块非零、对所有操作不变，且不可再作非平凡不变直和分解；同一个操作作用于每个张量位置。这比“商空间里出现 $Z$”或“只选到一个好分解”要求更多。

读者可查看[所引修订](trureturing:)中的[公开定理源码](lean:D5/S3/HomologicalAlgebra/TensorNullSummand.result)。形式化陈述的假设与结论如上所列。

## 整篇论文与这一条定理的差别

| 原论文结果 | 与公开 Lean 的关系 | 同一共享请求 |
|---|---|---|
| 引理 1：最大零作用重数 | 已有补空间构造；公开定理没有最大性、可加性或准确重数公式 | [最大重数与秩界](https://github.com/the-omega-institute/trureturing-requests/issues/44) |
| 定理 2：任意域定量界 | 公开定理是其定性特例，完整定量陈述仍待形式化 | [任意域张量估计](https://github.com/the-omega-institute/trureturing-requests/issues/45) |
| 推论 3：组成长度与误差 | 没有匹配的公开组成因子声明 | [组成重数与长度](https://github.com/the-omega-institute/trureturing-requests/issues/46) |
| 推论 4：幺半群比较 | 不同于“所有元素都奇异”的半群结论 | [非模幺半群比较](https://github.com/the-omega-institute/trureturing-requests/issues/47) |
| 推论 5：右零分解及修正 | 没有匹配的公开准确分解与分类声明 | [右零分解](https://github.com/the-omega-institute/trureturing-requests/issues/48) |
| 推论 6：群并例子的准确计数 | 没有匹配的公开复特征标计数声明 | [群并例子](https://github.com/the-omega-institute/trureturing-requests/issues/49) |
| 命题 7：Jordan 张量重数 | 公开 Jordan 链及迭代秩定理是相关工具，未给出这些张量计数公式 | [Jordan 张量重数](https://github.com/the-omega-institute/trureturing-requests/issues/50) |
| 推论 8：已发表矩阵递推 | 没有匹配的公开矩阵递推声明 | [融合矩阵递推](https://github.com/the-omega-institute/trureturing-requests/issues/51) |

源码还含有假设更弱的组成结果，包括不要求代数闭或排除单位元的存在性与收敛结论，但它们没有给出上面的全部定量公式。相关的 [Jordan 链定理](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S1/Eigenstructure/NilpotentJordanChains.lean)提供一般的链分解与秩工具；从中推导本文准确的张量重数仍是独立任务。仓库保留了[逐结果的详细对照](https://github.com/mathesis-papers/he-tubbenhauer-2025-null-tensor-summand/blob/main/.mathesis/REVIEW.md)。

## 来源、DOI 与优先权

本讲解对应 Haobo Ma 与 Wenlin Zhang 的[公开版本 2](https://mathesis-omega-research.apps.chrono-ai.fun/papers/he-tubbenhauer-2025-null-tensor-summand?version=2)，论文日期为 2026 年 11 月 5 日，收录于 11 月 14 日。目前尚未记录本论文的 DOI。

以下按数学作用列出来源；原文各结论的准确证明见同仓库原论文。

- David He、Daniel Tubbenhauer，[Tensor powers of representations of (diagram) monoids](https://arxiv.org/abs/2508.04054v1)，2025，猜想 4.2、3A.2，命题 4.1、4.4，例 4.3。原问题与这些已有结果归原作者。
- 同两位作者，[Affine diagram categories, algebras and monoids](https://arxiv.org/abs/2512.05510v2)，2025 年 12 月 19 日版本，定理 4A.14(e)–(f) 已证明右幂等元生成情形；后续 v3 与原论文所引期刊版本不应倒写为首次证明日期。
- 同两位作者，[Growth problems for representations of finite monoids](https://arxiv.org/abs/2502.02849v1)，例 2.2；v2 例 1。本文的群并例子来自此处。
- D. B. McAlister，[The category of representations of a completely 0-simple semigroup](https://doi.org/10.1017/S1446788700009460)，1971，定义 1.4、推论 2.6：零作用直和项的先例。
- D. Juteau、C. Mautner、G. Williamson，[Parity sheaves](https://doi.org/10.1090/S0894-0347-2014-00804-3)，2009 年预印本、2014 年期刊版，引理 3.1：重数配对的先例。
- R. A. Brualdi，[Combinatorial verification of the elementary divisors of tensor products](https://doi.org/10.1016/0024-3795(85)90233-2)，1985，定理 4.6(4)：幂零张量块。
- K. Coulembier、V. Ostrik、D. Tubbenhauer，[Growth rates of the number of indecomposable summands in tensor powers](https://doi.org/10.1007/s10468-023-10245-7)，2024，定理 1.4(a)、注 1.5(a)：一般根增长率的背景；根极限不是此处的比值极限。
- P. Etingof 等，[Introduction to representation theory](https://math.mit.edu/~etingof/reprbook.pdf)，2011，定理 3.8.1 与 4.1.1(i)：Krull–Schmidt 与 Maschke 定理。

无限半群的推广、非平凡单位群的模特征情形、原文指定的谱误差公式、子群特定重数及其他所列数列仍待研究。论文的有限计算检查指定的大小与指数范围；一般结论由书面论证支持。

## 如何贡献

可以在上表选择一个结果，通过对应请求加入形式化工作并协调范围。[贡献指南](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)说明如何提交证明。每项完成的贡献都应指明所证明的准确陈述，并分别保留原数学成果与形式化工作的署名。

<section hidden="hidden">

```{=typst}
#pagebreak()
```

</section>
