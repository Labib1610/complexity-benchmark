# Network Subsystem Triplet Validation

Time limit: 2 s   Memory limit: 256 MB

## Description
A distributed communications framework comprises $n$ numbered relay nodes. Direct bidirectional communication channels exist between specific pairs of nodes. System auditors are evaluating network topology to locate any set of three distinct nodes that form a fully interconnected triad—that is, every node in the set shares a direct communication channel with the remaining two nodes in the set.

Due to the size of the infrastructure, the configuration search space encompasses over a billion potential node combinations. However, network telemetry guarantees that at least one such mutually interconnected triad exists.

Your task is to identify the lexicographically smallest triad of nodes $(a, b, c)$ with $a < b < c$. Lexicographical comparison evaluates $a$ first; if two triads share the same $a$, $b$ is evaluated; if $b$ is also equal, $c$ is evaluated.

## Input
The first line contains two space-separated integers $n$ and $m$.

The node count $n$ satisfies $3 \le n \le 2000$. The line count $m$ satisfies $3 \le m \le \min(n(n-1)/2, 200000)$.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a direct two-way line between node $u$ and node $v$. No pair of nodes is listed more than once.

## Output
Print three space-separated integers $a$, $b$, $c$ on a single line with $1 \le a < b < c \le n$, representing the three nodes of the lexicographically smallest fully interconnected triad.

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
