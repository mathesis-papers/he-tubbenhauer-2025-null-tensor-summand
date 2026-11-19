# 论文版本 2 与公开 Lean 声明的精确对照

本表是陈述对应记录，不是新的审稿或 Lean 编译凭据。所有原目录身份、状态与哈希保持不变。八项原论文结论均已对照；额外 original-conjecture 与定理 2 共用目录节点，但仅陈述明确标出的定性特例。无 DOI 的未覆盖结果用注明来源的 remark，不获书面证明徽章，且保留规范共享请求。

| Result | Verdict | Compared declaration | Commit | Scope |
|---|---|---|---|---|
| null-multiplicity | none | — | 15070fa5f71c4237050acc7ebe058958cbc04e6e | 任意域、任意有限操作族（无需半群关系）；最大零作用直和项维数等式、秩下界、可加性与任意不可分解分解中的 Z 重数。私有 split_common_null 给构造维数关系，但未公开最大性及可加性接口；未找到陈述完整结论的公开声明。 |
| tensor-bound | special case | D5/S3/HomologicalAlgebra/TensorNullSummand.result | 15070fa5f71c4237050acc7ebe058958cbc04e6e | 定理 2 对任意域与可有单位元的非空有限半群成立，逐个 n>=1 给出最大零作用重数与每种分解的定量夹逼、秩特定阈值及比值极限。公开 result 只陈述代数闭域且无单位元的定性特例。私有 any-field 辅助结果与秩上界不等于完整公开定理。 |
| composition-length | none | — | 15070fa5f71c4237050acc7ebe058958cbc04e6e | 定理 2 假设下的组成因子重数、组成长度、各归一化误差与极限；公开 result 的内部直和计数不陈述组成列或这些界。 |
| monoid-comparison | none | — | 15070fa5f71c4237050acc7ebe058958cbc04e6e | 有限保单位幺半群，只有 1 作用为恒等，单位群阶可逆；含非单位元零作用的 M-不变分裂、余项维数界与限制到单位群前后的计数比较，含空非单位元理想及平凡单位群边界。与全部元素奇异的公开半群定理不同；无匹配公开声明。 |
| right-zero | none | — | 15070fa5f71c4237050acc7ebe058958cbc04e6e | 任意域右零半群的准确张量分解，所有不可分解模的分类给出非 Z 的组成比例<=1/2，从而满足 c=3/4 假设并修正逐点等式。公开 result 不陈述这个分类、准确分解或修正。 |
| group-union | none | — | 15070fa5f71c4237050acc7ebe058958cbc04e6e | 复数域 C2 与 S3 并零的指定表示；所有 n>=1 的准确零重数与总块数，含 S3 特征标计算。公开 result 没有匹配的准确计数声明。 |
| jordan-counts | variant | D5/S1/Eigenstructure/NilpotentJordanChains.nilpotent_jordan_chains_rank | 15070fa5f71c4237050acc7ebe058958cbc04e6e | 任意域 d>=2,n>=1；正幂含零半群的 b、mu 以及各块大小 j 的公式。公开 nilpotent_jordan_chains_rank 给任意幂零算子的链基与迭代秩，是相关工具；未陈述 J_d 张量幂秩、不可分解计数或二阶差分重数。 |
| fusion-counts | none | — | 15070fa5f71c4237050acc7ebe058958cbc04e6e | 仅针对既有四阶融合矩阵，列向量约定、起始 v0 与所有 n>=2 的归纳递推，得总计数及第三顶点 Z 重数；不声称重建表示或覆盖 n=1。未找到匹配公开声明。 |
| original-conjecture | same | D5/S3/HomologicalAlgebra/TensorNullSummand.result | 15070fa5f71c4237050acc7ebe058958cbc04e6e | 明确标注为定理 2 的定性特例：任意代数闭域、非空有限无双边单位元半群、有限维空间、乘法映射且每个作用不可逆；存在正指数实际一维零作用直和项及不变补空间，存在对所有自然数含零的内部不可分解计数序列，且每个这样的序列均有比值极限 1。逐项与 claim 及 result 相同，不代表完整定理 2。 |

检查范围：上述修订的完整 TensorNullSummand.lean、Golden/Frozen/state 对应片、Blueprint、HomologicalAlgebra 目录、公开 NilpotentJordanChains 源码与状态片。目录树关键字检索只是辅助，递归响应有截断，不声称穷尽全库。result 在状态片中种类为 theorem；split_common_null、exists_summand_count、exists_null_tensor_power、tensor_counts_tendsto、tensor_power_range_le 等是私有声明，不能当作公开 GID。最后一个给的是秩上界。HasNullSummand、IsSummandCount、IsIndecomposableSummand 与 tensorAction 的定义均已逐项阅读。
