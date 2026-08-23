# Critical Interference

Time limit: 2 s
Memory limit: 256 MB

A proposed security protocol attempts to assign $n$ communication nodes (numbered 1 to $n$) to one of two distinct channels. However, there are $m$ specific pairs of nodes that will experience severe interference if they are placed in the same channel. 

The protocol's requirements are known to be fundamentally impossible to satisfy. Your task is to certify this impossibility. You must identify a set of three nodes such that every pair of nodes within this set is known to interfere. Any such group of three mutually interfering nodes demonstrates that two channels are insufficient. It is guaranteed that at least one such set of three nodes exists.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of nodes that interfere with each other. 
It is guaranteed that at least one set of three mutually interfering nodes exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$, representing the identifiers of the three nodes, such that all three pairs $a$ and $b$, $a$ and $c$, and $b$ and $c$ interfere. 
Output the lexicographically smallest such set (smallest $a$; ties by smallest $b$; then smallest $c$).

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
