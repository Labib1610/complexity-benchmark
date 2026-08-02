# Stage 2 Diagnostic: Incompatibility Triplet Extraction

Time limit: 2 s   Memory limit: 256 MB

As part of an automated data-auditing pipeline for distributed database transactions, processing proceeds through three distinct phases:

1. **Extraction Phase (Completed)**: The system parses transaction logs and extracts all pairwise data-race conflicts among $n$ indexed database operations (numbered $1$ through $n$).
2. **Diagnostic Certificate Phase (Current Task)**: Before escalating to manual resolution, the automated validator must generate an audit certificate. The certificate requires identifying three distinct operations $a, b, c$ ($a < b < c$) such that every pair among them—$(a,b)$, $(a,c)$, and $(b,c)$—suffers from a mutual conflict. To ensure deterministic reporting across pipeline runs, if multiple such triplets exist, the validator must report the lexicographically smallest one (the one with the smallest index $a$; breaking ties by smallest $b$; then by smallest $c$).
3. **Escalation Phase (Pending)**: The extracted triplet will be dispatched to the system administrator to demonstrate an unresolvable concurrency cycle.

Given the list of pairwise conflicts generated in Phase 1, implement the Diagnostic Certificate Phase to find and output this lexicographically smallest conflicting triplet. It is guaranteed that at least one such triplet exists in the input data.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of database operations and the number of pairwise conflicts, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a pairwise conflict between operation $u$ and operation $v$.
It is guaranteed that at least one set of three operations pairwise conflict with each other.

## Output
Print three space-separated integers $a\ b\ c$ on a single line satisfying $a < b < c$, representing the operations forming a mutual conflict triplet. The triplet must be lexicographically smallest among all valid triplets.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
