# Problem A — Decentralized Ledger Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

A financial consortium oversees a network of **n** distinct data repositories, labeled 1 through **n**. To facilitate communication, there are **m** proposed bilateral sharing agreements available. Each agreement enables seamless, two-way data replication between a specific pair of repositories and incurs a fixed implementation overhead.

The repositories are divided into two categories: exactly **t** of them are designated as critical vaults, while the rest are standard vaults. Any repository (critical or standard) will automatically forward data across all active agreements it is part of. 

Your task is to establish a valid subset of the **m** proposed agreements so that all critical vaults are fully interconnected. Specifically, every critical vault must be able to share data with every other critical vault, either through a direct agreement or through a sequence of active agreements. You may utilize standard vaults as intermediaries to achieve this. Find the lowest possible sum of implementation overheads required to meet this condition. 

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers representing the labels of the critical vaults.
The following **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), describing a proposed sharing agreement between repository **u** and repository **v** that costs **w** to implement.
It is guaranteed that the provided agreements are sufficient to interconnect all critical vaults.

## Output

Print a single integer representing the minimum total implementation overhead needed to interconnect all critical vaults.

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

In Example 1, establishing agreements through the standard vault 4 (overhead 1+1+1 = 3) is cheaper than connecting the three critical vaults without using repository 4 (which would cost 2+2 = 4). In Example 3, there is only one critical vault, so no agreements are needed and the minimum total overhead is 0.