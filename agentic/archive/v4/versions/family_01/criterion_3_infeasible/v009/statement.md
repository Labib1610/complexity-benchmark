# Phase 2 Certificate Generation

Time limit: 2 s   Memory limit: 256 MB

As part of an automated workforce auditing pipeline, shift assignment proceeds in three distinct phases:
- Phase 1: Incompatibility logs are aggregated from worker preferences into paired conflict records.
- Phase 2: A certificate of impossibility is extracted from the conflict records to prove that two shifts (1 and 2) cannot fulfill the constraints.
- Phase 3: The pipeline consumes this certificate to halt the automated scheduler and escalate to management.

You are responsible for implementing Phase 2. The factory roster is guaranteed to contain at least one set of three workers who all pairwise conflict with each other. To produce a standardized certificate, you must isolate and output the lexicographically smallest such triple.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n\cdot(n-1)/2, 2\cdot 10^5)$), representing the number of workers and the number of conflicting pairs, respectively.
Each of the next $m$ lines contains two integers $u$ $v$ — a pair of conflicting workers.
It is guaranteed that at least one triple of pairwise conflicting workers exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are recorded conflicts. Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
