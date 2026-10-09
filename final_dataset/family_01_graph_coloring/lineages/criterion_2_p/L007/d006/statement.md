# Problem B — Network Configurations

Time limit: 1 s
Memory limit: 256 MB

A communication grid consists of $n$ radio towers. The available protocol suite consists of exactly two protocols, designated 1 and 2. 
You need to assign each tower $i$ a primary active protocol $f_i \in \{1, 2\}$. The protocol not chosen by tower $i$ automatically becomes its inactive backup protocol.

There are $m$ critical links between specific pairs of towers. 

To establish a successful bidirectional handshake across a critical link between tower $u$ and tower $v$, the hardware requires a strict cross-protocol allocation. Specifically, the primary active protocol of tower $u$ must exactly match the inactive backup protocol of tower $v$. (Because the link is symmetric, this simultaneously ensures the primary active protocol of tower $v$ matches the inactive backup protocol of tower $u$).

Determine if a valid assignment of primary protocols exists for all towers such that all critical links successfully establish their handshakes. If no such assignment is possible, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of towers connected by a critical link.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $f_1 \dots f_n$ (each in $\{1,2\}$). 
If multiple valid assignments exist, you must resolve ties by choosing the assignment that assigns the smallest possible protocol to tower 1. If ties remain, among those, choose the one that assigns the smallest possible protocol to tower 2, and continue this sequential preference for smaller protocols up to tower $n$ (this is equivalent to the lexicographically smallest valid assignment).

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```