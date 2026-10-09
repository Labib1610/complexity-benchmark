# Problem C — Tri-Node Provisioning

Time limit: 2 s   Memory limit: 256 MB

A computing fabric contains $n$ compute modules, indexed 1 to $n$. A set of $m$ bidirectional data links provides direct hardware-level communication. Each link connects a distinct pair of modules; no module links to itself, and there is at most one link between any specific pair. The fabric topology guarantees that the sum of the degrees of all modules is exactly $2m$.

You must allocate a tri-node processing unit. This requires finding exactly three distinct modules that are mutually fully connected (i.e., each of the three modules has a direct data link to both of the other two). 
It is guaranteed that the fabric's topology allows at least one such tri-node unit to be formed. Furthermore, for any valid tri-node unit, the sum $S$ of its three module indices will always satisfy $6 \le S \le 3n-3$.

## Input
The first line provides $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each contain two integers $u$ and $v$ — representing a bidirectional data link between module $u$ and module $v$.
At least one valid tri-node unit is guaranteed to exist.

## Output
Output a single line containing three integers $a$, $b$, and $c$, which are the indices of the chosen modules. These must be printed in ascending order ($a < b < c$).
If multiple such units can be formed, you must output the one that is lexicographically smallest. (This means minimizing $a$; if there is a tie, minimize $b$; and if still tied, minimize $c$).

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
