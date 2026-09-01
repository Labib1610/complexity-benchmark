# Power Grid Synchronization

Time limit: 1 s
Memory limit: 256 MB

You are deploying a cluster of $n$ processing units. Each unit $i$ must be configured with a power state $s_i \in \{1, 2\}$.

The cluster contains $m$ bidirectional data links between units. When a link connects unit $u$ and unit $v$, the link's thermal footprint is calculated as $2^{s_u} + 2^{s_v} - 1$.

The total thermal footprint of the cluster is the product of the thermal footprints of all $m$ links. (If the cluster has no links, the total thermal footprint is considered to be 1). To prevent overheating while maintaining performance, the cluster achieves optimal equilibrium if and only if its total thermal footprint is exactly $5^m$.

Your task is to determine a valid power state configuration for all $n$ units such that the cluster reaches optimal equilibrium. If there are multiple valid configurations, you must output the one that produces the lexicographically smallest sequence of power states $s_1, s_2, \dots, s_n$. If it is impossible to satisfy the requirement, report that no such configuration exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a data link exists between unit $u$ and unit $v$.

## Output
If there is no valid configuration, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $s_1, s_2, \dots, s_n$, representing the lexicographically smallest valid sequence of power states.

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