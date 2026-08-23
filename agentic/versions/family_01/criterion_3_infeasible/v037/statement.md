# Problem C — Deployment Deadlock

Time limit: 2 s   Memory limit: 256 MB

A software system consists of $n$ microservices. The architecture guidelines state that the services must be deployed across exactly two distinct server environments.

You are given $m$ dependency records. Each record identifies a pair of microservices that share a stateful resource and therefore must be deployed in different environments. 

Your task is to identify a deployment deadlock involving exactly three microservices, $a$, $b$, and $c$ (with $a < b < c$). A deadlock of this size is formed when the provided records contain:
- A record between $a$ and $b$.
- A record between $b$ and $c$.
- A record between $a$ and $c$.

Output the lexicographically smallest such triplet $a, b, c$ (smallest $a$; ties by smallest $b$; then smallest $c$). It is guaranteed that the given input contains at least one such triplet.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a dependency record between microservice $u$ and microservice $v$.
It is guaranteed that at least one triplet satisfying the conditions exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the lexicographically smallest triplet that forms a deadlock (smallest $a$; ties by smallest $b$; then smallest $c$).

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
