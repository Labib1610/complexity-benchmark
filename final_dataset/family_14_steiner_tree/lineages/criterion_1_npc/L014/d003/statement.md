# Problem A — Decentralized Ledger Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

A financial consortium oversees an infrastructure of **n** distinct data repositories, labeled 1 through **n**. There are **m** proposed integration protocols available. Each protocol targets a specific pair of repositories and incurs a fixed implementation overhead.

The repositories are divided into two categories: exactly **t** of them are designated as critical vaults, while the rest are standard vaults. 

Activating a protocol seamlessly merges the data streams of its two target repositories, ensuring any information present at one is instantaneously mirrored at the other. Because this mirroring is automatic, information cascades across all activated protocols: any sequence of active protocols linking a set of repositories will synchronize their contents entirely. 

Your task is to select a valid subset of the **m** proposed protocols so that all critical vaults end up sharing a single, unified data pool. You may activate protocols involving standard vaults to help achieve this. Find the lowest possible sum of implementation overheads required to meet this condition.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers representing the labels of the critical vaults.
The following **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), describing a proposed protocol that merges the data streams of repository **u** and repository **v** for an overhead of **w**.
It is guaranteed that the provided protocols are sufficient to synchronize all critical vaults.

## Output

Print a single integer representing the minimum total implementation overhead needed to synchronize all critical vaults.

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

In Example 1, synchronizing through the standard vault 4 (overhead 1+1+1 = 3) is cheaper than unifying the three critical vaults without using repository 4 (which would cost 2+2 = 4). In Example 3, there is only one critical vault, so no protocols are needed and the minimum total overhead is 0.