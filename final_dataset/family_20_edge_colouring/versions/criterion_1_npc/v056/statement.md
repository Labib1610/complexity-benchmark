# Problem A — Regulatory Oversight Allocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A regulatory body is auditing a batch of financial records. The batch contains $n$ entities and $m$ bilateral transfers. The batch data is guaranteed to satisfy the following strict structural constraints:
1. **Sparse density**: The total number of transfers $m$ is exactly $1.5n$, and $m$ never exceeds 3000.
2. **Irreflexivity**: Every transfer occurs between two strictly distinct entities.
3. **Bounded degree**: No entity is involved in more than 3 transfers.
4. **Global bandwidth limit**: For any transfer between entity $u$ and entity $v$, the absolute difference $|u - v|$ is strictly less than $n$.
5. **Checksum validity**: The total sum of all entity identifiers across all endpoints of all $m$ transfers is exactly $1.5n(n+1)$.

The regulatory body must assign each transfer to one of three inspectors (labeled 1, 2, and 3). To prevent conflict of interest, the following oversight rules must be strictly followed:
- **Per-entity limit**: No inspector is permitted to review more than one transfer involving the same entity. (Because the checksum and degree constraints ensure each entity is involved in exactly three transfers, the three transfers associated with any single entity must be distributed among the three different inspectors).
- **Balanced workload**: Each of the three inspectors must be assigned exactly $m/3$ transfers in total.

Determine if there is a valid assignment of the $m$ transfers to the three inspectors that satisfies these oversight rules.

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), representing a transfer between entity $u$ and entity $v$.
It is guaranteed that every entity identifier from 1 to $n$ appears exactly three times in the input.

## Output
If a valid assignment exists, print `YES`, followed by a line with $m$ integers in $\{1, 2, 3\}$ representing the inspector assigned to each transfer in input order. If there are multiple valid assignments, any may be output.
Otherwise, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
