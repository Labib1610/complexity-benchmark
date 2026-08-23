# Problem B — Conduit Load

Time limit: 1 s   Memory limit: 256 MB

A data center contains $n$ servers. You must configure the power draw for each server to be exactly either 1 or 2 units. 

There are $m$ pairs of servers that share a local conduit. To maintain strict load balancing, the sum of the power draws of the two servers in any such pair must be exactly 3 units. 

Assign each server a power draw to satisfy this condition, or report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of servers sharing a conduit.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $z_1 \dots z_n$ (each in $\{1,2\}$), the lexicographically smallest valid assignment.

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