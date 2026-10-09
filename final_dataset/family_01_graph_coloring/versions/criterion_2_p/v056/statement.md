# Vault Allocation Module

Time limit: 1 s
Memory limit: 256 MB

The automated pharmaceutical pipeline consists of three stages. You are programming the Vault Allocation Module (Phase B).
Phase A synthesizes a batch of $n$ volatile compounds, numbered $1$ to $n$. It also records $m$ specific pairs of these compounds that will aggressively degrade if placed in the same environment.

Your module must allocate each of the $n$ compounds to one of two climate-controlled vaults, designated as Vault 1 and Vault 2. 
To prevent degradation, if Phase A indicates that two compounds are incompatible, they must be assigned to different vaults.

Due to the stabilization properties of the Phase A synthesis chamber, the input is guaranteed to satisfy the following conditions:
- If you tally how many times each compound appears across all $m$ incompatible pairs, the sum of these tallies across all $n$ compounds is identically $2m$.
- There are at least $\max(0, n - 2m)$ compounds that do not appear in any incompatible pair.
- The $n$ compounds can always be partitioned into at least $\max(1, n - m)$ disjoint, non-empty subsets such that no incompatible pair contains compounds from two different subsets.

If there is no way to safely allocate all compounds into the two vaults without putting incompatible compounds together, your module must trigger an abort sequence.
If a safe allocation is possible, you must generate the final manifest for Phase C (Automated Retrieval). Phase C's routing logic is deterministic and requires a standardized manifest: among all safe allocations, the sequence of assignments $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$ is the vault assigned to compound $i$) must be the lexicographically smallest possible sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of synthesized compounds and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a pair of compounds that are incompatible and cannot share a vault.

## Output
If no safe allocation exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each either `1` or `2`), representing the lexicographically smallest valid vault assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
