# Problem C — Justifying the Roster Failure

Time limit: 2 s
Memory limit: 256 MB

The management wants to assign all personnel to two distinct working periods. They have collected a list of incompatibility logs, each indicating that two specific individuals are in conflict and cannot share a working period. 

However, management will only formally declare the two-period assignment impossible if they can pinpoint a specific failing configuration. They require a proof of impossibility consisting of exactly three distinct incompatibility logs chosen from the provided records. 

This set of three logs is considered a valid proof if it satisfies the following condition: when you count the unique individuals mentioned across these three logs, there must be exactly three unique individuals in total.

The management guarantees that the provided records contain at least one such set of three logs. Your task is to identify the three unique individuals involved in this proof.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of personnel and the total number of incompatibility logs, respectively. Personnel are numbered from 1 to $n$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating an incompatibility log involving individual $u$ and individual $v$. All logs are distinct (no pair of individuals is listed more than once).

It is guaranteed that at least one valid set of three logs exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, satisfying $a < b < c$, representing the three unique individuals involved in the valid set of logs.

If there are multiple valid groups of three individuals that can be formed this way, output the one that comes first lexicographically (minimize $a$; in case of a tie, minimize $b$; and finally minimize $c$).

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