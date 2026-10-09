# Problem A — Sequence Properties

Time limit: 2 s   Memory limit: 256 MB

You are tasked with determining the properties of a sequence of $n$ chemical additives. Each additive $i$ in the sequence must be assigned a concentration level $c_i \in \{1, 2, 3\}$.

You are provided with $m$ constraints. Each constraint is defined by a pair of distinct indices $(u, v)$, representing two additives that are reactive when mixed. For the sequence of additives to form a stable compound, every given pair must satisfy a specific energy condition regarding their assigned concentration levels. 

The interaction energy between the additive at index $u$ and the additive at index $v$ is modeled by the quadratic function:
$E(x) = x^2 - (c_u + c_v)x + c_u c_v$
where $x$ is a real number representing a continuous reaction parameter.

To prevent destabilization, the global minimum value of this interaction energy function $E(x)$ (over all real numbers $x$) must be strictly negative. If the minimum energy is zero or positive, the pair will destabilize the sequence.

If there are multiple valid sequences of concentration levels that satisfy all $m$ constraints, you must determine the one that is lexicographically smallest. A sequence $A$ is lexicographically smaller than sequence $B$ if, at the first index where they differ, sequence $A$ has a smaller concentration level than sequence $B$.
If no sequence can satisfy all constraints, you must report that it is impossible.

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