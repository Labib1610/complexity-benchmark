# Problem C — Mutually Incompatible Group

Time limit: 2 s   Memory limit: 256 MB

A facility tracks operational incompatibility between $n$ individuals, numbered $1$ through $n$. You are given $m$ specified pairs of individuals who are mutually incompatible.

Your task is to identify a group of three individuals who are all mutually incompatible with one another. That is, you must find three distinct IDs $a, b, c$ with $a < b < c$ such that $a$ and $b$ are incompatible, $a$ and $c$ are incompatible, and $b$ and $c$ are incompatible.

It is guaranteed that at least one such group of three exists. If multiple such triples exist, output the lexicographically smallest triple $(a, b, c)$—that is, the one with the smallest $a$, breaking ties with the smallest $b$, and further ties with the smallest $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \ne v$), indicating that individual $u$ and individual $v$ are mutually incompatible.
It is guaranteed that at least one valid triple exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are incompatible. Output the lexicographically smallest such triple.

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
