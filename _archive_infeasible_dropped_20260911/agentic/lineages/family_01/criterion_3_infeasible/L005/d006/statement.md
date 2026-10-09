# Problem C — Justifying the Roster Failure

Time limit: 2 s
Memory limit: 256 MB

The management wants to assign all personnel to two distinct working periods. They have collected a list of incompatibility logs, each indicating that two specific individuals are in conflict and cannot share a working period. 

However, management will only formally declare the two-period assignment impossible if they can pinpoint a specific failing group. They require a group of exactly three individuals $\{a, b, c\}$ that certifies this impossibility.

A group of exactly three individuals $\{a, b, c\}$ certifies that two periods are insufficient if all three individuals are mutually in conflict with one another—that is, the incompatibility logs contain a record for $a$ and $b$, a record for $a$ and $c$, and a record for $b$ and $c$.

The management guarantees that the provided records contain at least one such group of three individuals. Your task is to identify one such group.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of personnel and the total number of incompatibility logs, respectively. Personnel are numbered from 1 to $n$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating an incompatibility log involving individual $u$ and individual $v$. All logs are distinct (no pair of individuals is listed more than once).

It is guaranteed that at least one such group of three individuals exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, satisfying $a < b < c$, representing the three individuals in the group.

If there are multiple such groups, output the one that comes first lexicographically (minimize $a$; in case of a tie, minimize $b$; and finally minimize $c$).

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