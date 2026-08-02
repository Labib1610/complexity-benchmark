# Problem C — Critical Incompatibility Group

Time limit: 2 s   Memory limit: 256 MB

A factory manages $n$ workers, numbered $1$ through $n$. Due to operational constraints, certain pairs of workers are incompatible and cannot be assigned together. You are given a list of $m$ such incompatible pairs.

To perform a workforce audit, you need to identify three distinct workers $a, b, c$ who are all mutually incompatible with one another — meaning $a$ is incompatible with $b$, $a$ is incompatible with $c$, and $b$ is incompatible with $c$.

It is guaranteed that at least one such group of three mutually incompatible workers exists. Your task is to find the lexicographically smallest triple $(a, b, c)$ with $a < b < c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating an incompatible pair of workers.
It is guaranteed that at least one mutually incompatible triple exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$ such that all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are incompatible. Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
