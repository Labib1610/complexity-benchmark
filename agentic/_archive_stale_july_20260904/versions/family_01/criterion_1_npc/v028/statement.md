# Problem A — Deployment Tiers

Time limit: 2 s   Memory limit: 256 MB

A software system consists of $n$ microservices, identified by integers from 1 to $n$. You must assign each microservice a security tier. A tier is represented by a positive integer strictly less than 4.

Extensive testing has revealed that certain pairs of microservices exhibit parallel execution flaws. If a pair with this flaw operates at the exact same security tier, the system becomes unstable. To guarantee stability, the two microservices in any such pair must be assigned to different tiers.

You must determine a valid tier assignment for all $n$ microservices. If there are several valid ways to assign the tiers, you must prefer the configuration that assigns the lowest possible tier to microservice 1. If ties remain, you must break them by minimizing the tier assigned to microservice 2, continuing this element-by-element comparison up to microservice $n$. If no such configuration is possible, you must report this failure.

## Input
The first line provides $n$ and $m$ — the number of microservices and the number of flawed pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, indicating that microservice $u$ and microservice $v$ share a parallel execution flaw.

## Output
If the system cannot be stabilized, output a single line with the word NO.
Otherwise, output YES on the first line. On the second line, output $n$ integers separated by spaces, representing the tiers assigned to microservices 1 through $n$ respectively, following the tie-breaking rules described above.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
