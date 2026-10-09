# Problem A — Sequence Properties

Time limit: 2 s
Memory limit: 256 MB

You must configure the concentration levels for a linear sequence of $n$ chemical additives. For each additive $i$, you must select a concentration level $c_i$ from the set $\{1, 2, 3\}$.

The chemical mixture is subject to $m$ known reactive constraints. Each constraint is given as a pair of distinct indices $(u, v)$, indicating that the additives at positions $u$ and $v$ have the potential to react. A sequence is considered stable if and only if all $m$ specified pairs meet a strict compatibility requirement based on their chosen concentrations.

Specifically, the stability of a pair $(u, v)$ depends on the harmonic mean of their concentration levels, defined mathematically as:
$H(u, v) = \frac{2 c_u c_v}{c_u + c_v}$

A reaction is triggered—thereby destabilizing the entire sequence—if this harmonic mean $H(u, v)$ evaluates to a whole number (an integer). Therefore, to maintain stability, $H(u, v)$ must strictly be a non-integer value for every given constraint.

When multiple stable configurations exist, you must find the one that is lexicographically smallest. Configuration $A$ is lexicographically smaller than configuration $B$ if $A$ contains a smaller concentration level at the first sequence position where the two configurations differ. If it is impossible to stabilize the sequence under the given constraints, you must report this failure.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$) — the length of the sequence and the number of constraints.
Each of the following $m$ lines contains two distinct integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) — indicating a constraint between the additives at index $u$ and index $v$.

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