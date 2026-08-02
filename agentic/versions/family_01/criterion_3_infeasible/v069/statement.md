# Distributed Network Topology Diagnostics — Primary Interlock Isolation

Time limit: 2 s   Memory limit: 256 MB

As part of an automated infrastructure assessment pipeline, modern network diagnostic engines execute a multi-stage reliability verification workflow:

1. **Ingestion & Topology Construction**: The network topology, consisting of $n$ distinct processing units (labeled $1$ through $n$) and $m$ bidirectional communication channels, is read and built into memory.
2. **Primary Interlock Isolation**: The diagnostic engine scans for mutual interlock clusters consisting of three distinct processing units where a direct bidirectional communication channel exists between every pair among the three. To ensure deterministic execution across redundant audit workers, the engine must isolate the lexicographically smallest triple of units $(a, b, c)$ with $a < b < c$.
3. **Mitigation Routing**: The isolated primary triple is forwarded to downstream routines for patch propagation.

Your task is to implement the computation for Stage 2. Given the parsed system topology from Stage 1, find and output the lexicographically smallest triple of units $a, b, c$ with $a < b < c$ such that direct communication channels exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$), representing the number of processing units and the number of communication channels, respectively.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating a direct bidirectional communication channel between unit $u$ and unit $v$. No communication channel is listed more than once.
It is guaranteed that at least one valid set of three mutually connected units exists in the network.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line, with $a < b < c$, representing the lexicographically smallest triple of processing units where communication channels exist between all three pairs.

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
