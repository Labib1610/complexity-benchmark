# Problem C — Deployment Impossibility

Time limit: 2 s   Memory limit: 256 MB

A cloud application is built from $n$ microservices. A strict architectural rule requires partitioning all microservices into exactly two distinct server environments.

You are provided with $m$ resource contentions. Each contention specifies two microservices that access the same stateful database, meaning they cannot be placed in the same environment.

You must find a specific deployment impossibility caused by a group of three microservices. This impossibility occurs when all three microservices in the group have resource contentions with both of the other two members of the group. Let the identifiers of these three microservices be $x$, $y$, and $z$, sorted such that $x < y < z$.

If there are multiple such groups of three microservices, you must output the one that minimizes $x$. If there is still a tie, minimize $y$, and finally minimize $z$. You are guaranteed that at least one such group exists.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a resource contention between microservice $u$ and microservice $v$.
It is guaranteed that at least one group of three satisfying the conditions exists.

## Output
Print three integers $x$, $y$, and $z$ on a single line with $x < y < z$, representing the identifiers of the microservices in the chosen group (minimizing $x$, then $y$, then $z$).

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
