# Certifying Incompatibility

Time limit: 2 s   Memory limit: 256 MB

A system consists of $n$ items numbered $1$ to $n$. There are $m$ designated pairs of items that are directly linked with each other.

It is guaranteed that there exists at least one group of three distinct items where all three possible pairs among them are directly linked. Your task is to find the lexicographically smallest such group of three items.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ representing a link between items $u$ and $v$.
It is guaranteed that at least one valid group of three items exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are directly linked. Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
