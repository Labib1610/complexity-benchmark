# Shift Partition Search

Time limit: 1 s   Memory limit: 256 MB

A facility operates across two distinct operational shifts, designated as 1 and 2. Given $n$ employees and $m$ pairwise incompatibility constraints, we must evaluate the space of $2^n$ possible shift assignments to determine whether any configuration satisfies all constraints simultaneously.

An assignment is valid if no pair of mutually incompatible employees is assigned to the same operational shift. If one or more valid configurations exist, find the lexicographically smallest assignment sequence $s_1, s_2, \dots, s_n$ where each $s_i \in \{1, 2\}$. If no valid assignment exists among all choices, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) representing an incompatible pair of employees.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
