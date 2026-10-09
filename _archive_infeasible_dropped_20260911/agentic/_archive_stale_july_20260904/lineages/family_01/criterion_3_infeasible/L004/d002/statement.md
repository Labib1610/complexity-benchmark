# Critical Interference

Time limit: 2 s
Memory limit: 256 MB

A proposed security protocol attempts to assign $n$ communication nodes (numbered 1 to $n$) to one of two distinct channels. However, there are $m$ specific bidirectional connections between nodes that cause severe interference.

The protocol's requirements are known to be fundamentally impossible to satisfy. Your task is to certify this impossibility. You must identify a group of three distinct nodes such that all three nodes are mutually connected to each other (i.e., a connection exists between every pair of nodes in the group).

Any such group of three nodes demonstrates that two channels are insufficient. It is guaranteed that at least one such group exists.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a connection between node $u$ and node $v$.
It is guaranteed that at least one group of three mutually connected nodes exists.

## Output
Print three integers on one line, representing the identifiers of the three nodes that form the mutually connected group. The three identifiers must be printed in ascending order.
If there are multiple such groups, output the one whose sorted sequence of identifiers is lexicographically smallest (i.e., smallest first identifier; in case of a tie, smallest second identifier; then smallest third identifier).

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