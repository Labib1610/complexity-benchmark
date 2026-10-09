# Problem A — Decentralized Ledger Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

A financial consortium manages an ecosystem of **n** distinct data repositories, labeled uniquely from 1 to **n**. Within this ecosystem, there are **m** proposed two-way synchronization channels that can be implemented. Each proposed channel allows data to be seamlessly mirrored between a specific pair of repositories and carries a known implementation overhead.

Among the **n** repositories, a specific subset of **t** repositories are designated as primary ledgers. The remaining repositories are auxiliary. Any repository, whether primary or auxiliary, will automatically relay updates between any implemented synchronization channels it participates in.

The consortium must guarantee that all primary ledgers are fully synchronized. This requires that every primary ledger can exchange updates with every other primary ledger, either directly or via some chain of implemented channels. You must select a subset of the **m** proposed channels to implement such that this synchronization requirement for the primary ledgers is satisfied. You may only select from the **m** proposed channels listed; selected channels may involve auxiliary repositories. Your goal is to keep the sum of the implementation overheads as low as possible. Determine this minimum total overhead.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the labels of the primary ledgers.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): indicating a proposed synchronization channel between repository **u** and repository **v** with an implementation overhead of **w**.
It is guaranteed that the listed proposed channels are sufficient to synchronize all primary ledgers.

## Output

Print a single integer: the minimum total implementation overhead required to synchronize all primary ledgers.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, implementing channels through the auxiliary repository 4 (overhead 1+1+1 = 3) is cheaper than directly connecting the three primary ledgers (which would cost 2+2 = 4). In Example 3, there is only one primary ledger, so no channels need to be implemented.