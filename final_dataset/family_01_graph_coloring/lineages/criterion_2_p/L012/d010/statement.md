# Problem B — Set Configuration

Time limit: 1 s
Memory limit: 256 MB

You are given $n$ variables, $h_1, h_2, \dots, h_n$. Each variable must be assigned a value from the set $\{1, 2\}$.

You must satisfy $m$ constraints. Each constraint is provided as a pair of indices $u$ and $v$. For every constraint, the set of values assigned to these two specific variables, $\{h_u, h_v\}$, must contain exactly two distinct elements.

Your task is to determine if there exists a valid assignment for all $n$ variables such that every constraint is met. If a valid assignment exists, you must output it.

If there are multiple valid assignments, you must output the one that is lexicographically smallest when represented as a sequence of integers $h_1, h_2, \dots, h_n$. A sequence $A$ is lexicographically smaller than sequence $B$ if, at the first index $i$ where they differ, the value in $A$ is strictly less than the value in $B$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a constraint between variables $h_u$ and $h_v$.

## Output
If there is no valid assignment, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $h_1, h_2, \dots, h_n$ (each either `1` or `2`), representing the lexicographically smallest valid assignment.

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