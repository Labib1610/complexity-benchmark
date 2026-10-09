# Problem A — Sequence Properties

Time limit: 2 s   Memory limit: 256 MB

You are tasked with finding an integer sequence $c_1, c_2, \dots, c_n$ where each element must be chosen from the set $\{1, 2, 3\}$.

You are provided with $m$ constraints. Each constraint is defined by a pair of distinct indices $(u, v)$. For the sequence to be valid, every given pair must satisfy the following mathematical property regarding their assigned values:
The $3 \times 3$ matrix constructed from their values, defined as
$$ \begin{pmatrix} 1 & 1 & 1 \\ c_u & c_v & 4 \\ c_u^2 & c_v^2 & 16 \end{pmatrix} $$
must be invertible. (A matrix is invertible if and only if its determinant is non-zero).

If there are multiple valid sequences that satisfy all $m$ constraints, you must determine the one that is lexicographically smallest. A sequence $A$ is lexicographically smaller than sequence $B$ if at the first index where they differ, sequence $A$ has a smaller value than sequence $B$.
If no sequence can satisfy all constraints, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$) — the length of the sequence and the number of constraints.
Each of the following $m$ lines contains two distinct integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) — indicating a constraint between the elements at index $u$ and index $v$.

## Output
If no valid sequence exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2, 3\}$), representing the lexicographically smallest valid sequence.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
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
NO
```