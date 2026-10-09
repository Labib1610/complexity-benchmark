# Problem B — Binary Variable Assignment

Time limit: 1 s
Memory limit: 256 MB

You are given $n$ variables $z_1, z_2, \dots, z_n$. Each variable must be assigned a value of either $1$ or $2$.

You are also given a sequence of $m$ pairs of indices. Let $(u, v)$ represent a pair in this sequence.

Determine whether there exists at least one valid assignment of values to all $n$ variables such that the following equality holds exactly:

$$ \sum_{(u, v)} \left( \frac{z_u}{z_v} + \frac{z_v}{z_u} \right) = \frac{5m}{2} $$

where the sum is taken over all $m$ given pairs.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the indices of the variables in a pair.

## Output
If no such assignment exists, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $z_1 \dots z_n$ (where each $z_i \in \{1,2\}$) representing the assignment. If there are multiple valid assignments that satisfy the equation, output the lexicographically smallest sequence $z_1 \dots z_n$.

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