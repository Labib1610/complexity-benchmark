# Problem C — Shift Constraint Certification

Time limit: 2 s   Memory limit: 256 MB

A facility assigns staff members numbered $1$ through $n$ to work duties. Certain pairs of staff members are declared mutually incompatible, meaning they cannot share an assignment block.

It is known that the given incompatibilities make a two-block schedule impossible. The fundamental reason for this impossibility is the presence of three distinct staff members where every pair among the three is mutually incompatible. Your task is to identify one such set of three staff members. If multiple such sets exist, choose the one that is lexicographically smallest when its members are listed in ascending numerical order.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$), representing the number of staff members and the total number of incompatible pairs, respectively.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that staff member $u$ and staff member $v$ are mutually incompatible. Each pair is listed at most once.

It is guaranteed that at least one such mutually incompatible group of three staff members exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line satisfying $1 \le a < b < c \le n$ such that all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are mutually incompatible. Output the lexicographically smallest triple (minimizing $a$, then $b$, then $c$).

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
