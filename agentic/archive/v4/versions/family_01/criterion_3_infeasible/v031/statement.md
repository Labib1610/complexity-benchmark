# Problem C — Interlock Protocol Audit

Time limit: 2 s   Memory limit: 256 MB

A distributed system consists of $n$ processing nodes numbered $1$ through $n$. Certain pairs of nodes are connected by direct high-bandwidth communication lines. Communication is symmetric, meaning a line between two nodes allows data to flow in both directions.

During a system audit, engineers are looking for closed three-node feedback loops. A feedback loop consists of three distinct nodes such that a direct communication line exists between every pair among the three.

It is guaranteed that the current network configuration contains at least one such three-node loop. Your task is to identify the lexicographically smallest group of three nodes forming a closed loop. Specifically, if the three nodes are $a$, $b$, and $c$ with $a < b < c$, you must select the valid triple that minimizes $a$ first, then $b$, and finally $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$), representing the number of processing nodes and the number of communication lines, respectively.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating a direct communication line between node $u$ and node $v$. No communication line is listed more than once.
It is guaranteed that at least one valid set of three nodes exists.

## Output
Print three space-separated integers $a$, $b$, $c$ on a single line, satisfying $a < b < c$, representing the lexicographically smallest triple of nodes where lines exist between $a$ and $b$, $a$ and $c$, and $b$ and $c$.

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
