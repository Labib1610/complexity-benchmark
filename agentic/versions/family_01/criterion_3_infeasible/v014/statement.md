# Problem C — Structural Obstruction Extraction

Time limit: 2 s   Memory limit: 256 MB

The state space of all possible two-shift assignments for $n$ workers is $2^n$, which can be astronomically large. Due to a severe number of mutual incompatibilities between workers, it has been mathematically proven that every single one of these $2^n$ assignments will fail.

Your task is not to attempt to schedule the workers or evaluate these assignments, but to isolate the root cause of this failure. To formally certify the infeasibility, you must extract a specific structural obstruction from the incompatibility data. 

A subset of workers forms a "complete obstruction" if every distinct pair of individuals within that subset is incompatible. Any complete obstruction of size exactly 3 forces the need for at least three shifts, thereby definitively proving that two shifts are insufficient.

Although there are $\frac{n(n-1)(n-2)}{6}$ possible triplets of workers to consider, it is guaranteed that at least one complete obstruction of size 3 exists in the provided data. You must search the combinations to find one.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of workers and the number of incompatible pairs.

The following $m$ lines each contain two integers $u$ and $v$, indicating that worker $u$ and worker $v$ are incompatible. It is guaranteed that there is at least one group of exactly three workers who are all mutually incompatible.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of three workers who form a complete obstruction of size 3 (i.e., the pairs $a-b$, $a-c$, and $b-c$ are all incompatible). Output the lexicographically smallest such group (minimize $a$; in case of a tie, minimize $b$; then minimize $c$).

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
