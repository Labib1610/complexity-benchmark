# Critical Interference

Time limit: 2 s
Memory limit: 256 MB

A proposed security protocol attempts to assign $n$ communication nodes (numbered 1 to $n$) to one of two distinct channels. However, there are $m$ specific connections between nodes that cause severe interference. For each connection, the interference is strictly directional: the node with the smaller identifier transmits a disruptive signal to the node with the larger identifier, regardless of the order they are listed in the input.

The protocol's requirements are known to be fundamentally impossible to satisfy. Your task is to certify this impossibility. You must identify a sequence of three distinct nodes $a$, $b$, and $c$, with $a < b < c$, such that:
- Node $a$ transmits a disruptive signal to node $b$.
- Node $a$ transmits a disruptive signal to node $c$.
- Node $b$ transmits a disruptive signal to node $c$.

Any such sequence of three nodes demonstrates that two channels are insufficient. It is guaranteed that at least one such sequence exists.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a connection between these two nodes. The disruptive signal flows from $\min(u, v)$ to $\max(u, v)$.
It is guaranteed that at least one sequence of three nodes satisfying the condition exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$, representing the identifiers of the three nodes. 
Output the lexicographically smallest such sequence (smallest $a$; ties broken by smallest $b$; then smallest $c$).

## Example 1
### Input
```
4 5
1 2
1 3
2 3
2 4
3 4
```
### Output
```
1 2 3
```

## Example 2
### Input
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
### Output
```
1 2 4
```