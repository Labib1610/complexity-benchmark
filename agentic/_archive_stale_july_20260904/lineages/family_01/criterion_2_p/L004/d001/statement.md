# Problem B — Zone Isolation

Time limit: 1 s
Memory limit: 256 MB

A data center contains $n$ servers. You must assign a security tier to each server. The only permitted tiers are 1 and 2. 

The system has $m$ active synchronization links. Each link connects a specific pair of servers. For the network to remain stable, the tiers assigned to any two servers connected by a synchronization link must have different parities.

Determine if a valid tier assignment exists for all $n$ servers.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the indices of a pair of servers connected by a synchronization link.

## Output
If no valid tier assignment is possible, print a single line NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $z_1 \dots z_n$ (where each $z_i \in \{1,2\}$) representing the valid assignment. If multiple valid assignments exist, output the one that is lexicographically smallest.

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