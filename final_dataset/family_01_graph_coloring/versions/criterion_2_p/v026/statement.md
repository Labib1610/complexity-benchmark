# Storage Pipeline: Phase B

Time limit: 1 s   Memory limit: 256 MB

The automated pharmaceutical pipeline consists of three stages. Phase A synthesizes a batch of $n$ volatile compounds, numbered 1 to $n$, and runs interaction simulations to identify $m$ pairs of compounds that are highly reactive.

Your software module is responsible for Phase B: Storage Allocation. The facility has exactly two climate-controlled vaults, designated as Vault 1 and Vault 2. You must allocate each of the $n$ compounds to one of these two vaults. To ensure stability, no two compounds that form a reactive pair (as identified by Phase A) may be allocated to the same vault. 

If there is no way to safely allocate all compounds into just two vaults, your module must trigger an abort sequence. If a safe allocation is possible, you must generate the final manifest for Phase C (Automated Retrieval). Because Phase C's routing logic is deterministic, it requires a standardized manifest: among all safe allocations, the sequence of assignments $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$ is the vault assigned to compound $i$) must be the lexicographically smallest possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of compounds synthesized in Phase A and the number of reactive pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a pair of compounds that are highly reactive when stored together.

## Output
If no safe allocation exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each either `1` or `2`), representing the lexicographically smallest valid storage allocation.

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
