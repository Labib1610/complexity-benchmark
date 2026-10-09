# Problem B — System Configuration

Time limit: 1 s   Memory limit: 256 MB

A cloud provider must configure the operation tier for $n$ database instances. The configuration requires assigning each instance $i$ a tier $s_i$, which must be chosen from the set $\{1, 2\}$.

The system includes $m$ shared backup storage arrays, each connecting two specific database instances. To ensure fault tolerance and balance the load, every backup array must connect instances operating in different tiers. Specifically, for every backup array connecting instances $u$ and $v$, one instance must be assigned Tier 1 and the other must be assigned Tier 2.

You must assign a tier to each instance to satisfy this requirement across all backup arrays, or determine that no such configuration exists. 

If multiple valid configurations exist, the automated deployment system requires the configuration whose sequence of assignments $s_1, s_2, \dots, s_n$ is lexicographically smallest. (A sequence $A$ is lexicographically smaller than a valid sequence $B$ if $A$ has a smaller value at the first position where they differ).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of database instances and the number of shared backup arrays.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that instances $u$ and $v$ share a backup array.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid configuration.

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