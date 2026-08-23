# Pipeline Stage 2 — Shift Partitioning

Time limit: 1 s   Memory limit: 256 MB

In an automated industrial workforce pipeline, scheduling operates in three distinct stages: constraint collection, shift partitioning, and dispatch.

Stage 1 has already ingested the workforce roster, identifying $n$ workers (numbered $1$ through $n$) and $m$ pairwise incompatibility constraints. Two workers bound by an incompatibility constraint cannot be assigned to the same working shift.

Your task is to execute Stage 2: Shift Partitioning. You must assign every worker to either Shift 1 or Shift 2 such that no two incompatible workers share the same shift. To ensure determinism for downstream Stage 3 processing, if multiple valid shift assignments exist, you must select the one that yields the lexicographically smallest sequence of shift numbers $s_1, s_2, \dots, s_n$. If no valid assignment can satisfy all constraints, Stage 2 must report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the total number of workers and the number of incompatibility constraints, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that worker $u$ and worker $v$ cannot share the same shift.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line, followed by a second line with $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), denoting the shift assigned to worker $i$, chosen to be the lexicographically smallest valid assignment.

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
