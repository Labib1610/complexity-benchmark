# Chemical Containment

Time limit: 1 s   Memory limit: 256 MB

A research facility needs to store $n$ distinct chemical samples, numbered $1$ through $n$, across two isolated containment chambers, labeled 1 and 2.

Certain pairs of samples are volatile when placed together and must be stored in different chambers. You are given $m$ such incompatible pairs.

Determine whether it is possible to assign every sample to a containment chamber (either 1 or 2) such that no incompatible pair shares a chamber. If a valid assignment exists, output `YES` followed by the lexicographically smallest assignment sequence $s_1, s_2, \dots, s_n$ where $s_i \in \{1, 2\}$ denotes the chamber assigned to sample $i$. If no valid assignment is possible, output `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the number of chemical samples and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that sample $u$ and sample $v$ cannot be placed in the same chamber.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid chamber assignment.

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
