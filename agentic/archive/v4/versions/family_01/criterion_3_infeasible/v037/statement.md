# Problem C — Machine Triplet Identification

Time limit: 2 s   Memory limit: 256 MB

A production plant operates $n$ distinct machines, numbered $1$ to $n$. Certain pairs of machines interfere with each other when operated simultaneously. You are provided a list of $m$ mutually interfering pairs.

It is guaranteed that there exists at least one group of three distinct machines where every pair within the group interferes with each other. Your task is to find the lexicographically smallest such triplet.

Specifically, you must find three machine indices $a, b, c$ such that $a < b < c$ and all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are present in the list of interfering pairs. Among all valid triplets, select the one with the smallest $a$, breaking ties by the smallest $b$, and further ties by the smallest $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), denoting an interfering pair of machines.
It is guaranteed that at least one valid triplet exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the lexicographically smallest triplet of mutually interfering machines.

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
