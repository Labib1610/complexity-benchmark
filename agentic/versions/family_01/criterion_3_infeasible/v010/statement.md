# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

A factory operates with a collection of workers numbered from $1$ to $n$ and a list of $m$ pairwise worker conflicts. When two workers conflict, they cannot be assigned to the same shift. It is guaranteed that there exists at least one group of three distinct workers where every pair among the three conflicts with each other.

Your task is to identify such a triple of workers to serve as evidence that assigning all workers using at most two shifts is impossible. Among all such valid triples, output the lexicographically smallest one.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ $v$ — a conflicting pair of workers.
It is guaranteed that at least one such triple of mutual conflicts exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, $b$–$c$ are conflicts. Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
