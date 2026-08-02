# Problem C — Operational Conflict Audit

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant maintains records of pairs of workers who cannot be assigned to work concurrently due to operational safety regulations. To audit the facility's scheduling constraints across all potential worker assignments, management requires a certified proof of scheduling infeasibility.

A valid proof consists of three distinct workers $a, b, c$ such that every pair chosen from these three workers is listed as an incompatible pair. Evaluating all potential worker triplets across a large facility can involve scanning an enormous state space of possible combinations. However, your goal is simply to identify the first such conflicting triplet in canonical order. Specifically, find a triplet of worker identifiers $(a, b, c)$ with $1 \le a < b < c \le n$ where all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are mutually incompatible, choosing the one that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of workers and the total number of incompatible pairs, respectively. Workers are numbered from $1$ to $n$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that worker $u$ and worker $v$ are mutually incompatible. No pair of workers will be listed more than once.

It is guaranteed that at least one group of three workers exists where every pair among them is incompatible.

## Output
Print three space-separated integers $a, b, c$ on a single line such that $a < b < c$ and all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are incompatible. If multiple such triplets exist, output the lexicographically smallest one (minimizing $a$, then $b$, then $c$).

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
