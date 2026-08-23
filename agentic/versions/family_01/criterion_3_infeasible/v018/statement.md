# Shift Allocation Audit

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant operates on exactly two daily shifts. A roster of worker incompatibilities has been drafted, but management suspects that it is logically impossible to divide the workforce into just two shifts without forcing incompatible workers to work together.

Your task is to audit the proposed roster and provide undeniable proof of this impossibility. You do not need to attempt a full schedule. Instead, you must identify a foundational contradiction: a group of exactly three workers where every individual in the group is incompatible with both of the others. The presence of such a triad means that no two-shift allocation could ever succeed, as at least two of these three workers would be forced into the same shift.

It is mathematically guaranteed that the provided roster contains at least one such triad. Furthermore, it is guaranteed that the total number of logged incompatibilities $m$ is strictly less than $n^2$, and that any valid triad of workers will have identifiers summing to at most $3n-3$.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), representing the number of workers (identified from $1$ to $n$) and the number of incompatible pairs.
Each of the subsequent $m$ lines contains two integers $u$ and $v$, indicating that worker $u$ and worker $v$ cannot be assigned to the same shift.
It is guaranteed that at least one mutually incompatible triad exists.

## Output
Output three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the identifiers of three workers who are all mutually incompatible with one another.
The identifiers must be ordered such that $a < b < c$.
If there are multiple such triads, you must output the one that is lexicographically smallest (i.e., minimize $a$; if tied, minimize $b$; if still tied, minimize $c$).

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
