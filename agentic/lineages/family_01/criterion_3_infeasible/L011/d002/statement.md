# Audit of Entangled Assets

Time limit: 2 s   Memory limit: 256 MB

A forensic accounting firm is analyzing a registry of corporate entities. The goal is to partition the entities into two distinct regulatory zones such that no direct financial exchanges exist between any two entities assigned to the same zone. The current registry cannot be partitioned in this way.

The analysts have determined that this failure is caused by a structural anomaly: a group of exactly three entities where a direct financial exchange exists between every possible pair within the group. Because all three entities directly exchange assets with each other, it is impossible to assign them to just two zones without at least two exchanging entities sharing a zone.

Your task is to pinpoint such a group. If there are multiple such groups, you must isolate the one that minimizes the anomaly fingerprint. For a group of three entities with identification numbers $a, b,$ and $c$ (ordered so that $a < b < c$), the anomaly fingerprint is defined by the formula: $a \cdot 10^8 + b \cdot 10^4 + c$.

## Input
The first line of the input contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of corporate entities and the number of recorded financial exchanges. The entities are assigned integer IDs from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that a direct financial exchange exists between entity $u$ and entity $v$. 

The provided records are guaranteed to contain at least one group of three entities where a direct exchange exists between every pair in the group.

## Output
Output a single line containing three space-separated integers $a$, $b$, and $c$ ($a < b < c$) representing the IDs of the three entities in the group. You must output the group that yields the minimum anomaly fingerprint as described.

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